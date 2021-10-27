from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_mixin

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date

SQLALCHEMY_DATABASE_URL = "postgresql://scwd:ofekdekel@localhost:5432/test_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@declarative_mixin
class ID_and_Timestamps:
    id = Column(Integer, primary_key=True, index=True)
    created = Column(Date, nullable=False, default=datetime.utcnow)
    updated = Column(Date, onupdate=datetime.utcnow)