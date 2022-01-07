from typing_extensions import Required
from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.expression import null

from app.database import Base, ID_and_Timestamps
from .association_tables import hunters_to_moves, hunters_to_gear

class Playbook(Base):
    
    name: Column(String, nullable=False)
    description: Column(String)
    luck_special: Column(String)
     
    # ratings: relationship()
    
    # appearance: relationship()
    # history: relationship()
    
    # moves: relationship()
    # gear: relationship()
    
            
    def __init__(self,input): 
        pass   
        
    def __repr__(self):
        pass
