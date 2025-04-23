from unicodedata import category
from pydantic import BaseModel
class StockCreate(BaseModel):
    category: str
    item: str
    quantity: int = 1
