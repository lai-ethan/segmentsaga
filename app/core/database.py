from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from settings import settings

# --- Base class for SQLAlchemy models ---
Base = declarative_base()

# --- Database URL ---
DATABASE_URL = settings.database_url

# --- Async SQLAlchemy engine ---
# This engine is used to connect to the database asynchronously
# The echo=True flag is useful for debugging, it logs all the SQL statements
engine = create_async_engine(DATABASE_URL, echo=True)

# --- Async session local class ---
# This session local class is used to create new sessions for each request
# It uses the async_sessionmaker to create sessions that are compatible with async operations
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False, # prevents the session from expiring/data available after commit
    class_=AsyncSession
)

# --- Dependency for FastAPI routes ---
# This function provides a session to be used in FastAPI routes
# It yields a session that can be used in the route, and ensures that the session is closed after the request is completed
from fastapi import Depends
async def get_async_session():
    async with AsyncSessionLocal() as session: 
        yield session
