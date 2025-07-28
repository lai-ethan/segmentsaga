from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    budget = Column(Float, nullable=True)
    interests = Column(String, nullable=True)  # could be a comma-separated list or JSON later
   
    segment_id = Column(Integer, ForeignKey('segments.id'), nullable=True)
    segment = relationship('Segment', back_populates='customers')
