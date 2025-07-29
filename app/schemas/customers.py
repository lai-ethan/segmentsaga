# creates our pydantic models/schemas for the Customer model (data validation/serialization from sql to json)
from pydantic import BaseModel

# --- CustomerCreate Schema ---
class CustomerCreate(BaseModel):
    name: str
    email: str
    budget: float | None = None
    interests: str | None = None
    segment_id: int | None = None

# --- SegmentRead Schema (for nested return) ---
class SegmentRead(BaseModel):
    id: int
    name: str

    # lets pydantic convert from sqlalchemy models (from models.py) into pydantic JSON; required when reading from the database
    class Config:
        orm_mode = True

# --- CustomerRead Schema (output) ---
class CustomerRead(BaseModel):
    id: int
    name: str
    email: str
    budget: float | None = None
    interests: str | None = None
    segment: SegmentRead | None = None

    class Config:
        orm_mode = True