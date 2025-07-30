# creates our pydantic models/schemas for the Customer model (data validation/serialization from sql to json)
from pydantic import BaseModel

# --- CustomerCreate Schema ---
# This schema is used for creating a new customer
# It defines the fields required when creating a customer
# The fields are name, email, budget, interests, and segment_id
# The segment_id is optional and can be used to associate the customer with a specific segment
# The model_dump() method is used to convert the Pydantic model to a dictionary format
# which is compatible with SQLAlchemy's model creation
# This schema is used in the POST request to create a new customer
# this is different from the models defined in models.py, which are SQLAlchemy models
# this schema is used to validate incoming data and ensure it meets the requirements before creating a new customer in the database
class CustomerCreate(BaseModel):
    name: str
    email: str
    budget: float | None = None
    interests: str | None = None
    segment_id: int | None = None

# --- SegmentRead Schema (for nested return) ---
# this is different from the Segment model in models.py
# this schema is used to return a segment when reading a customer
# it includes only the id and name of the segment
# this is useful for returning a simplified version of the segment when fetching customer data
# we need to convert the SQLAlchemy model to a Pydantic model because FastAPI uses Pydantic for data validation and serialization
# serialization is the process of converting complex data types (like SQLAlchemy models) into JSON-compatible formats
# json is the format used for API responses which looks like {"id": 1, "name": "Segment A"}
class SegmentRead(BaseModel):
    id: int
    name: str

    # lets pydantic convert from sqlalchemy models (from models.py) into pydantic JSON; required when reading from the database
    class Config:
        orm_mode = True

# --- CustomerRead Schema (output) ---
# This schema is used for reading a customer
# It includes all fields from CustomerCreate plus the segment information
# The segment field is of type SegmentRead, which allows us to return the segment details along with the customer
# This schema is used in the GET request to return customer data
# it allows us to return a customer with its associated segment in a structured format
# it also uses the orm_mode to allow Pydantic to read data from SQLAlchemy models
class CustomerRead(BaseModel):
    id: int
    name: str
    email: str
    budget: float | None = None
    interests: str | None = None
    segment: SegmentRead | None = None

# this allows us to return the segment details when reading a customer
# it ensures that the segment data is included in the response when fetching customer information
    # this is necessary because FastAPI uses Pydantic to serialize the response data
    # and we need to tell Pydantic how to handle SQLAlchemy models
    # orm_mode=True allows Pydantic to read data from SQLAlchemy models directly
    # this is important for converting SQLAlchemy models to JSON responses in FastAPI
    # it allows us to return complex nested structures like Customer with its Segment
    # this is useful for APIs that need to return related data in a single response
    # for example, when fetching a customer, we can also include the segment they belong to
    # this makes the API more efficient by reducing the number of requests needed to get related data    
    class Config:
        orm_mode = True