from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relation, relationship

from app.database import Base, ID_and_Timestamps
from .association_tables import hunters_to_moves, hunters_to_gear


class Move(Base, ID_and_Timestamps):
    __tablename__ = 'moves'
    
    playbook_id: Column(Integer, ForeignKey('playbooks.id'), nullable=True)
    
    homebrew = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    
    hunters: relationship('Hunter', secondary=hunters_to_moves)
    
    name: Column(String, nullable=False)
    description_short: Column(Text)
    description_long: Column(Text)
    
    choices_num: Column(Integer, default=0)
    choices_list: Column(Text, nullable=True)
    
    
class MoveOption(Base, ID_and_Timestamps):
    __tablename__ = 'move_options'
    