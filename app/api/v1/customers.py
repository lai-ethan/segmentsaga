from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_async_session
from app.models.models import Customer
from app.schemas.customers import CustomerCreate, CustomerRead

# --- Customer router setup ---
# This router handles all customer-related API endpoints
# It uses FastAPI's APIRouter to define a set of routes under the '/customers' prefix
# The 'tags' parameter is used to group these endpoints in the API documentation
router = APIRouter(prefix='/customers', tags=['Customer'])

# --- POST: Create customer ---
# This endpoint allows creating a new customer
# It expects a CustomerCreate schema in the request body
# The session is injected using the get_async_session dependency
# This ensures that the database session is available for the operation
# The response model is CustomerRead, which defines the structure of the response
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
# This endpoint retrieves all customers from the database
# It uses the session to execute a query that selects all Customer records
# The results are returned as a list of CustomerRead schemas
# If no customers are found, it returns an empty list
# This is a common pattern for listing resources in RESTful APIs
@router.get('/', response_model=list[CustomerRead])
async def get_customers(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Customer).order_by(Customer.id))
    customers = result.scalars().all()
    return customers

