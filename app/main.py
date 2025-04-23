from fastapi import FastAPI
from app.api.endpoints.v1.product_router import router as product_router
from app.api.endpoints.v1.agents_router import router as agent_router
from app.database.connection import create_database 
from app.models.products_model import Stocks
app = FastAPI(title="LangChain Agent API")
app.include_router(product_router)
app.include_router(agent_router)



@app.on_event("startup")
async def on_startup():
    await create_database()