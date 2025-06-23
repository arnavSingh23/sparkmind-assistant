from sentence_transformers import SentenceTransformer
from functools import lru_cache

"""
This file:
    Embeds user query as a numerical embedding vector and returns that vector for similarity search
"""

@lru_cache()
def get_embedder():
    """Load model once and reuse using LRU cache"""
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_query(text: str) -> list[float]:
    """
    Takes in a text string and returns its embedding as a list of floats.

    Parameters:
        text (str): Text to embed

    Returns:
        list[float]: Embedding vector
    """
    model = get_embedder()
    embedding = model.encode(text)
    return embedding.tolist()
