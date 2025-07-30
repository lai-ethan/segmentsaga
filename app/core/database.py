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
# this creates the actual database connection that will be used by the application
engine = create_async_engine(DATABASE_URL, echo=True)

# --- Async session local class ---
# This session local class is used to create new sessions for each request
# It uses the async_sessionmaker to create sessions that are compatible with async operations   
# a session is necessary because it allows us to interact with the database
# it provides a context for executing queries and managing transactions
# without a session, we cannot perform any database operations b ecause SQLAlchemy needs a session to track changes and manage the connection
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False, # prevents the session from expiring/data available after commit
    class_=AsyncSession
)

# --- Dependency for FastAPI routes ---
# This function provides a session to be used in FastAPI routes
# It yields a session that can be used in the route, and ensures that the session is closed after the request is completed
# a dependency is a function that FastAPI calls to provide data to your route handlers
# this is useful for managing database connections in a clean way
# it allows us to use the session in our route handlers without having to manage it manually
# this is different from async_sessionmaker because it provides a session for each request
# it ensures that the session is properly closed after the request is completed
# what async_sessionmaker does is create a session factory that can be used to create new sessions
# this is necessary for FastAPI to handle requests asynchronously
# these are the sessions created from the session factory async_sessionmaker
from fastapi import Depends
async def get_async_session():
    async with AsyncSessionLocal() as session: 
        yield session
