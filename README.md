# RAG Module – Automated eNA Agreement Generation

# Moon_Product
This project implements a **Retrieval-Augmented Generation (RAG)** service to automatically generate final eNA agreement texts by combining LLM-based text generation with company-specific knowledge retrieval.

## Overview
- Context-aware generation based on **supplier data**, **eNA clauses**, and **objection reasons**
- Integrated into an existing backend and exposed via a **`/rag` API endpoint**

## Tech Stack
- **LlamaIndex** (document ingestion, chunking, retrieval)
- **OpenAI API** (GPT-3.5 Turbo)
- **Node.js / Express.js**

# RAG_python_experiments
- QA & retrieval experiments using **Recursive Chunking** and **Markdown Node Parser**
- Documented in `RAG_experiments`
- Uses **only public, non-sensitive data**

## Secrets and local data
- Do not commit API keys, tokens, or `.env` files; use `.env.example` for required variables.
- Clear Jupyter outputs before publishing and avoid embedding real customer data in notebooks.
