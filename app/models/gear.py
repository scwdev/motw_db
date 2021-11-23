from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.expression import null

from app.database import Base, ID_and_Timestamps
from .association_tables import hunters_to_moves, hunters_to_gear


class Gear(Base, ID_and_Timestamps):
    
    __tablename__ = "gear"
    
    name: Column(String, nullable=False)
    description: Column(String, nullable=False)
    does_harm: Column(Boolean)
    harm: Column(Integer, nullable=True)
    homebrew: Column(Boolean, default=True)
    public: Column(Boolean, default=True)
    
    
    # tags: relationship()
    # playbooks: relationship()
    # hunters: relationship()
    # users: relationship()
    # groups: relationship()
    
    def __init__(self,input): 
        pass   
        
    def __repr__(self):
        pass

    