from pydantic import BaseModel, Field

"""
This File:
    Validates the incoming query, and ensures that the shape of the data being passed is expected
"""

class QueryRequest(BaseModel):
    query: str = Field(..., description="User's natural language question to the assistant")
    top_k: int = Field(default=5, description="Number of top matching chunks to retrieve from vector store")
