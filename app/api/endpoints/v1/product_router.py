from fastapi import APIRouter,HTTPException
from app.orm.product_db import *
from app.database.connection import get_db
from app.orm import product_db
from app.schemas.stocks_schema import StockCreate
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter(prefix="/stock",tags=["Product"])

@router.get("/all")
async def get_product(db: AsyncSession = Depends(get_db)):
    user= await product_db.get_all_stocks(db)
    return user

@router.get("/categories/{category}")
async def get_product_categories(categories: str,db: AsyncSession = Depends(get_db)):
    user= await product_db.get_single_item(categories,db)
    return user

@router.post("/add")
async def read_stock(stock: StockCreate,db: AsyncSession = Depends(get_db)):
    user= await product_db.add_stock(stock,db)
    return user

@router.delete("/delete/{stock_id}")
async def delete_stock(stock_id: UUID, db: AsyncSession = Depends(get_db)):
    deleted = await product_db.delete_stock(db, stock_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Stock not found")
    return {"detail": f"Stock with deleted Successfully"}
