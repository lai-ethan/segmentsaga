from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_async_session
from app.models.models import Customer
from app.schemas.customers import CustomerCreate, CustomerRead

# --- Customer router setup ---
router = APIRouter(prefix='/customers', tags=['Customer'])

# --- POST: Create customer ---
@router.post('/', response_model=CustomerRead)
async def create_customer(
    customer: CustomerCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_customer = Customer(**customer.model_dump())
    session.add(new_customer)
    await session.commit()
    await session.refresh(new_customer)
    return new_customer

# --- GET: List all customers ---
@router.get('/', response_model=list[CustomerRead])
async def get_customers(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Customer).order_by(Customer.id))
    customers = result.scalars().all()
    return customers

