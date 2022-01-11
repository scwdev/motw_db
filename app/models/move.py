from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relation, relationship

from app.database import Base, ID_and_Timestamps
from .association_tables import hunters_to_moves, hunters_to_gear


class Move(Base, ID_and_Timestamps):
    __tablename__ = 'moves'
    
    hunters: relationship('Hunter', secondary=hunters_to_moves)
    
    playbook: Column(Integer, ForeignKey('playbooks.name'), nullable=True)
    name: Column(String, nullable=False)
    description_short: Column(Text)
    description_long: Column(Text)
    has_options: Column(Boolean)
    options: relationship('MoveOption')
    options_num_bases: Column(Integer, nullable=True)
    options_num_choices: Column(Integer, nullable=True)
    
    homebrew = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    
    def __init__(self,input): 
        pass   
        
    def __repr__(self):
        pass


class MoveOption(Base, ID_and_Timestamps):
    __tablename__ = 'move_options'
    
    move_id = Column(Integer, ForeignKey('moves.id'))
    
    
        
    def __init__(self,input): 
        pass   
        
    def __repr__(self):
        pass
