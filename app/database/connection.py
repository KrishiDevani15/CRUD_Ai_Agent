from curses import echo
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
	raise ValueError("DATABASE_URL environment variable is not set")
print(DATABASE_URL)

# 1) Create connection
engine = create_async_engine(DATABASE_URL,echo=True)

# 2) Base
Base = declarative_base()

# 3) Create Session
SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession)

# 4) get db
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

