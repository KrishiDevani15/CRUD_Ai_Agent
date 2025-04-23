from langchain.tools import tool
import httpx
import os

API_URL = os.getenv("INVENTORY_API_URL")

@tool("add_stock")
async def add_stock_tool(category: str, item: str, quantity: int):
    """Add a new stock item to the inventory (e.g., category=clothes, item='jeans', quantity=20)"""
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_URL}/stock/add", json={
            "category": category,
            "item": item,
            "quantity": quantity
        })
        return response.json()

@tool("read_stock")
async def read_stock_tool(category: str):
    """Fetch stock info for a given category (e.g., 'clothes', 'tea')"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/stock/categories/{category}")
        return response.json()

@tool("get_all_stock")
async def get_all_stock_tool():
    """Fetch all stock items in the inventory"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/stock/all")
        return response.json()

@tool("delete_stock")
async def delete_stock_tool(stock_id: str):
    """Delete a stock item by its UUID"""
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_URL}/stock/delete/{stock_id}")
        return response.json()
