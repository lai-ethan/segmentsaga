import asyncio
from app.core.database import Base, engine
from app.models.models import Segment, Customer # Importing models to ensure they are registered with SQLAlchemy

async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print('✅ Tables created successfully.')

if __name__ == '__main__':
    asyncio.run(create_all_tables())