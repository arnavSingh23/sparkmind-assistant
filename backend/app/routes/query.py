from fastapi import APIRouter, HTTPException
from app.models.query_request import QueryRequest
from app.services.qa_pipeline import run_qa_pipeline

"""
This file:
    Defines the /query route
"""
router = APIRouter()

@router.post("/")
async def handle_query(request: QueryRequest):
    """ Routes and handles incoming user questions

        Parameters:
            request(QueryRequest): A QueryRequest Object

        Returns:
            result: Final LLM response with citations
    """
    try:
        result = run_qa_pipeline(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))