from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="all-minilm"
)

retrive_data = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    embedding=embeddings,
    collection_name="node_pdf",
)

search_result = retrive_data.similarity_search(
    query="what is node js?"
)

print("relevant  chunks :",search_result)

SYSTEM_PROMPT = f"""
You are a helpful assistant that can answer questions about the document.

CONTEXT:
{search_result}
"""





