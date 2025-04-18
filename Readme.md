# RAG with Ollama and Qdrant

This project implements a Retrieval-Augmented Generation (RAG) system using Ollama for embeddings and Qdrant as the vector store.

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Ashisharjun12/rag_pdf.git
cd rag
```

2. **Start Docker containers**
```bash
docker-compose up -d
```

3. **Pull the required Ollama model**
```bash
docker exec -it rag-ollama-1 ollama pull all-minilm
```

## Project Structure
- `chat.py`: Main script for processing PDF and creating embeddings
- `docker-compose.yaml`: Docker configuration for Qdrant and Ollama services
- `node.pdf`: Source PDF file for RAG system

## Dependencies
- Docker and Docker Compose
- Python packages:
  - langchain-community
  - langchain-text-splitters
  - langchain-ollama
  - langchain-qdrant

## Usage
1. Place your PDF file named `node.pdf` in the project root
2. Run the script:
```bash
python chat.py
```

## Services
- Qdrant: Running on `http://localhost:6333`
- Ollama: Running on `http://localhost:11434`
