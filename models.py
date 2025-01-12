import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import declarative_base

# Database URL
DATABASE_URL = "sqlite:///skillsync.db"

Base = declarative_base() # Base class for declarative models


class User(Base):
    """User model."""
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)
    expertise = Column(String)