# app/langchain_api.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.agents import agent

router = APIRouter(tags=["AI Agents"])

class QueryRequest(BaseModel):
    query: str

@router.post("/agent/query")
async def query_agent(request: QueryRequest):
    response = await agent.arun(request.query)
    return {"response": response}
