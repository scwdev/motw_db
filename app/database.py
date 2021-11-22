from os import environ as env

from dotenv import load_dotenv
load_dotenv()

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_mixin

from sqlalchemy import Column, Integer , Date


engine = create_engine(env.get("PGRES_URI") or "sqlite:///motw")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@declarative_mixin
class ID_and_Timestamps:
    id = Column(Integer, primary_key=True, index=True)
    created = Column(Date, nullable=False, default=datetime.utcnow)
    updated = Column(Date, onupdate=datetime.utcnow)