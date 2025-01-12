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

class Meeting(Base):
    """Meeting model."""
    __tablename__ = "meetings"

    meeting_id = Column(Integer, primary_key=True)
    mentor_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    mentee_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    time = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String)

class Workshop(Base):
    """Workshop model"""
    __tablename__ = "workshops"

    workshop_id = Column(Integer, primary_key=True)
    requestor_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    topic = Column(String, nullable=False)
    date_requested = Column(DateTime, default=datetime.datetime.utcnow)

# Function to create the database and tables
def create_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database()