import asyncio
from app.core.database import Base, engine
from app.models.models import Segment, Customer # Importing models to ensure they are registered with SQLAlchemy

# This script is used to create all tables in the database
# It uses SQLAlchemy's async capabilities to create tables defined in the Base metadata
# these tables are defined in the models imported above
async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print('✅ Tables created successfully.')

# This is the entry point for the script to create tables
# what that means is that when you run this script, it will execute the create_all_tables function
# This is useful for setting up the database schema before running the application
# It ensures that all necessary tables are created in the database
# You can run this script using the command: python create_tables.py
# Make sure to have the database connection details set up in your environment variables or .env file
# This script is typically run once to set up the database schema
# after that, you can run your FastAPI application which will use these tables
if __name__ == '__main__':
    asyncio.run(create_all_tables())