# RAG Contract Finder - Deployable Version

import os
import sys
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone as PineconeClient

# Environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENV = os.environ.get("PINECONE_ENV", "gcp-starter")
PDF_DIR = os.environ.get("PDF_DIR", "./PDFs")  
INDEX_NAME = os.environ.get("INDEX_NAME", "depo")

# Check for required environment variables
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required")
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY environment variable is required")

# Initialize Pinecone
pc = PineconeClient(api_key=PINECONE_API_KEY)

# Embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# LLM
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

def load_documents(pdf_dir):
    """Load PDF documents from directory"""
    loader = DirectoryLoader(pdf_dir, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

def split_texts(documents, chunk_size=1000, chunk_overlap=200):
    """Split documents into chunks"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    return texts

def setup_vectorstore(texts, index_name):
    """Create or load vector store"""
    if index_name not in [idx.name for idx in pc.list_indexes()]:
        print(f"Creating new index: {index_name}")
        docsearch = PineconeVectorStore.from_documents(texts, embeddings, index_name=index_name)
    else:
        print(f"Loading existing index: {index_name}")
        docsearch = PineconeVectorStore.from_existing_index(index_name, embeddings)
    return docsearch

def create_qa_chain(docsearch):
    """Create RetrievalQA chain"""
    retriever = docsearch.as_retriever(include_metadata=True, metadata_key='source')
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def parse_response(response):
    """Parse and print the response with sources"""
    print("Answer:", response['result'])
    print('\nSources:')
    for source_doc in response["source_documents"]:
        source = source_doc.metadata.get('source', 'Unknown')
        page = source_doc.metadata.get('page', 'Unknown')
        print(f"- {source}, page: {page}")

def query_documents(query, qa_chain):
    """Query the documents"""
    response = qa_chain(query)
    return response

def main():
    if len(sys.argv) < 2:
        print("Usage: python rag_deploy.py 'your query here'")
        sys.exit(1)

    query = sys.argv[1]

    # Load and process documents
    documents = load_documents(PDF_DIR)
    texts = split_texts(documents)

    # Setup vector store
    docsearch = setup_vectorstore(texts, INDEX_NAME)

    # Create QA chain
    qa_chain = create_qa_chain(docsearch)

    # Query
    response = query_documents(query, qa_chain)

    # Parse and print response
    parse_response(response)

if __name__ == "__main__":
    main()