'''
Defines SQLAlchemy models for both Customer and Segment.
These models describe how our tables are structured in the PostgreSQL database.
'''

# --- Imports ---
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


# --- Segment Model ---
class Segment(Base):
    __tablename__ = 'segments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    criteria = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # One-to-many relationship: one segment → many customers
    customers = relationship('Customer', back_populates='segment', lazy='selectin')


# --- Customer Model ---
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    budget = Column(Float, nullable=True)
    interests = Column(String, nullable=True)  # Could be extended to JSON later

    # Foreign key to Segment
    segment_id = Column(Integer, ForeignKey('segments.id'), nullable=True)

    # Many-to-one relationship: each customer belongs to one segment
    segment = relationship('Segment', back_populates='customers', lazy='selectin')
