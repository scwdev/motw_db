from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relation, relationship

from app.database import Base, ID_and_Timestamps
from .association_tables import hunters_to_moves, hunters_to_gear


class Gear(Base, ID_and_Timestamps):
    
    name: Column(String, nullable=False)
    description: Column(String, nullable=False)
    
    