from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relation, relationship

from app.database import Base, ID_and_Timestamps
from .association_tables import hunters_to_moves, hunters_to_gear


class Tag(Base, ID_and_Timestamps):
      
    name: Column(String, nullable=False)
    description: Column(String, nullable=False)
    
    
    def __init__(self,input): 
        pass   
        
    def __repr__(self):
        pass
