from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.expression import null

from app.database import Base, ID_and_Timestamps
from .association_tables import hunters_to_moves, hunters_to_gear

class Group(Base):
    
    __tablenames__ = "groups"
    
    game_master: relationship()
    users: relationship()
    moves: relationship()
    gear: relationship()
    playbooks: relationship()
    hunters: relationship()
   
            
    def __init__(self,input): 
        pass   
        
    def __repr__(self):
        pass
