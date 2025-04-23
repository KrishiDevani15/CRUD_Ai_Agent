from re import escape
from app.models.products_model import Stocks
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
async def get_all_stocks(db:AsyncSession):
    result = await db.execute(select(Stocks))
    result = result.scalars().all()
    if result:
        return result
    else:
        return "Inventory is Empty"
    
async def get_single_item(categories: str,db:AsyncSession):
    result = await db.execute(select(Stocks).filter(Stocks.category == categories))
    result = result.scalars().all()
    if result:
        return result
    else:
        return "No Categories Exists"
    
async def add_stock(stocks,db:AsyncSession):
    category = stocks.category.strip().lower()
    item = stocks.item.strip().lower()

    result = await db.execute(select(Stocks).filter(Stocks.category == category, Stocks.item == item))
    existing_stock = result.scalars().one_or_none()

    if existing_stock:
        existing_stock.quantity += stocks.quantity
        await db.commit()
        await db.refresh(existing_stock)
        return {"message": "Stock updated", "data": existing_stock}
    else:
        new_stock = Stocks(category = stocks.category,item=stocks.item,quantity=stocks.quantity)
        db.add(new_stock)
        await db.commit()
        await db.refresh(new_stock)
        return {"message": "Stock updated", "data": new_stock}

async def delete_stock(db: AsyncSession, stock_id: UUID):
    result = await db.execute(select(Stocks).filter(Stocks.id == stock_id))
    stock = result.scalars().first()
    if stock:
        await db.delete(stock)
        await db.commit()
    return stock

