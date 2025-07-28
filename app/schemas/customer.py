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