import faiss
import numpy as np
from typing import List

"""
This file: 
    Builds a vector database using FAISS to store document embeddings in memory
    Lets one search by semantics over keywords given a query
"""

VECTOR_DIM = 384 # This is the embedding size in MiniLM-V6-v2
index = faiss.IndexFlatL2(VECTOR_DIM)

stored_texts = [] # In memory "store" of documents for POC

def add_to_index(embeddings: list[np.ndarray], texts: list[str]):
    """Add embeddings and corresponding texts to the FAISS index."""
    global stored_texts
    index.add(np.array(embeddings).astype("float32"))
    stored_texts.extend(texts)

def search_index(query_embedding: np.ndarray, top_k: int = 5):
    """Search FAISS index for top_k closest vectors."""
    query_embedding = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    
    results = []
    for idx in indices[0]:
        if idx < len(stored_texts):
            results.append(stored_texts[idx])
    return results
