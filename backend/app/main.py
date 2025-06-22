from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import query 

"""
This file: 
    Instantiates the FastAPI app
    Enables CORS
    Registers the app routes
    Provides a rootendpoint for health checks
"""

app = FastAPI(
    title="SparkMind Assistant",
    description="RAG-based assistant for querying internal knowledge base",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],  # Remember to change to actual frontend url when complete 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router, prefix="/query", tags=["Query"])

@app.get("/")
def read_root():
    """Health Check route"""
    return {"message": "Welcome to SparkMind!"}

