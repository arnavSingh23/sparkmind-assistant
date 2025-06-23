from app.services.embedder import embed_query
from app.services.vector_store import retrieve_relevant_chunks
from app.services.llm import generate_answer_with_citations

def run_qa_pipeline(query: str, top_k: int = 5) -> dict:
    """
    Runs the full RAG pipeline:
    1. Embed the query
    2. Search vector DB for top-k similar chunks
    3. Generate answer using LLM + those chunks

    Parameters:
        query (str): User question
        top_k (int): Number of relevant chunks to retrieve

    Returns:
        dict: Final answer with citations
    """
    query_embedding = embed_query(query)
    chunks = retrieve_relevant_chunks(query_embedding, top_k=top_k)
    answer = generate_answer_with_citations(query, chunks)
    return answer