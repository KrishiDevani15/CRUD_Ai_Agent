from unicodedata import category
from app.database.connection import Base
from sqlalchemy import Column,Integer,String,UUID,Text,DateTime,func
from sqlalchemy.sql import text
import uuid

class Stocks(Base):
    __tablename__ = "stocks"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
        default=uuid.uuid4,
    )
    category = Column(String,nullable= False)
    item = Column(Text,nullable=False)
    quantity = Column(Integer,default=1)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())