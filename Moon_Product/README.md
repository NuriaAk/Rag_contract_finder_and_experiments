![moon logo](https://drive.google.com/uc?export=view&id=1WiQWrc3bD_dn11NhajC_Fxz8og-HLxCp)

Our product simplifies the objection management process for electronic Nomination Agreements (eNA) by consolidating it onto a single platform. This streamlines negotiation on eNA points, saving time for purchasers and facilitating reaching agreement with suppliers.

## **Module Documentation: AI suggested final agreement RAG module Documentation**

**Overview**
Large Language Models (LLMs) are trained on vast datasets, yet they lack training on your specific data. Retrieval-Augmented Generation (RAG) addresses this gap by incorporating your data alongside the existing datasets accessible to LLMs.
The RAG module is an important component of our system, focusing on generating contextually relevant responses by combining retrieval and generation techniques. Leveraging the LlamaIndex library, it integrates advanced text processing capabilities with an external AI model (OpenAI's GPT-3.5 Turbo) to generate contextually relevant answers. RAG is particularly suitable for scenarios requiring precise and informative responses, such as negotiations or inquiries within a corporate environment.


**Functionality**

The RAG module consists of the following functionalities:

1. **Contextual Response Synthesis**
   - The module accepts incoming queries along with contextual information.
   - It leverages LlamaIndex's capabilities to synthesize responses based on the provided context and query.

2. **Integration with OpenAI**
   - Utilizes the GPT-3.5 Turbo model from OpenAI to generate responses.
   - Configurable parameters such as model settings and temperature ensure flexibility in response generation.
   - OpenAI places a high priority on data security and privacy. According to the information provided in the extracts: Data sent to the OpenAI API is not used to train or improve OpenAI models.

3. **Knowledge Retrieval** 
   - Retrieves relevant knowledge from a knowledge base or corpus based on the provided context.
   - Incorporates retrieved knowledge into the response generation process, enriching the generated responses.
   - Input context is represented as a document using LlamaIndex's `Document` class.

4. **Response Refinement**
   - Custom response prompts are generated to provide clear and concise answers to queries.
   - Configurable parameters such as model settings and temperature enable customization of response generation.

**Usage**

1. **Initialization**
   - Upon receiving a request, the RAG module initializes the OpenAI model with specified settings.
   - It creates a document object representing the provided context.

2. **Response Synthesis**
   - Combines retrieved knowledge with generative techniques to produce contextually relevant responses.
   - A custom prompt is generated based on the context and query, guiding the AI model to produce relevant responses.
   - LlamaIndex's ResponseSynthesizer orchestrates the response generation process, ensuring coherence and accuracy.

3. **Query Execution**
   - The document, along with the generated prompt which contains the Supplier name, eNA point number and Reason for objection, is passed to the OpenAI model for eNA final agreement text generation.
   - The model processes the input and generates a response based on the context and query.

4. **Error Handling**
   - Robust error handling mechanisms are implemented to handle exceptions gracefully.
   - Errors encountered during response synthesis or query execution are logged and appropriate error responses are returned.

**Integration**

The RAG module seamlessly integrates with existing Express.js applications:
- It exposes an endpoint '/rag' to receive HTTP POST requests containing context and queries (Supplier name, eNA point number and Reason for objection).
- Upon receiving a request, it invokes the response synthesis process and returns the generated response to the client.

**Deployment**

- The RAG module can be deployed as part of the broader application stack.
- It relies on external dependencies such as LlamaIndex and OpenAI's GPT-3.5 Turbo model.
- Deployment configurations, including port settings and environment variables, can be managed using tools like dotenv.
**Note:** Ensure compatibility with Node.js version 18 or higher for optimal functionality, as required by LlamaIndex.


## **Maintaining the Local text.ts File for RAG**

The local text.ts file serves as a crucial resource for the retrieval part of the Retrieval-Augmented Generation (RAG) module. It contains essential data points such as 'Supplier', 'eNApoint number', 'Reason for objection', 'Comments', and 'Final agreement text', formatted as paragraphs. Regular updates, ideally 1-2 times a month, ensure that the RAG module suggests pre-defined and approved final agreement wordings for a wide range of cases. 

For privacy and compliance purposes, sensitive data such as 'Comments' and 'Final agreement text' can be anonymized either manually or through automated processes. Tools like Google's De-identification API, Microsoft Presidio, or open-source models for Personally Identifiable Information (PII) masking such as ai4privacy can assist in this process.

**Next Steps**

* Consider implementing a data pipeline that automatically transforms information stored in the database into the text file format. This pipeline would extract relevant data fields ('Supplier', 'eNApoint number', 'Reason for objection', 'Comments', and 'Final agreement text') from the database and organize them into paragraphs within text file(s). In this case the ingestion function should be updated according to the format of the text file. Automating this process streamlines data management and ensures the text file remains updated with the latest information from the database.
* Storing the indexes in the vector database such as Pinecone or ChromaDB can be considered as the next step of updating the RAG module.
* Consider exploring cost-saving opportunities by transitioning to open-source Large Language Models (LLMs) such as `open-mistral-7b` from Mistral AI or `gemma-1.1-7b-it` from Google. These open-source LLMs offer powerful language processing capabilities while potentially reducing maintenance costs associated with proprietary solutions. Evaluate the suitability of these models for your application's requirements and budget constraints to make an informed decision about the transition.


## Database Diagram

<img src="https://drive.google.com/uc?export=view&id=1UKJzPodaoHNQy9ITEyEtlMMvgvquSaCZ" width=800>

# Solution Diagram

<img src="https://drive.google.com/uc?export=view&id=1PcEoG_uzhAVaiSz7VxDSnBwk2PKPI0NZ" width=500>

## Secrets and local data
- Do not commit API keys, tokens, or `.env` files; use `.env.example` for required variables.
- Clear Jupyter outputs before publishing and avoid embedding real customer data in notebooks.
