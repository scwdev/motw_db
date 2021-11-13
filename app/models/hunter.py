from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relation, relationship

from app.database import Base, ID_and_Timestamps
from .association_tables import hunters_to_moves, hunters_to_gear


class Hunter(Base, ID_and_Timestamps):
    __tablename__ = "hunters"

    user_id = Column(Integer, ForeignKey('users.id'))
    playbook_id = Column(Integer, ForeignKey('playbooks.id'))
    
    moves_num = Column(Integer)
    moves_req = Column(Integer)
    moves = relationship("Move", secondary=hunters_to_moves)
    gear = relationship("Gear", secondary=hunters_to_gear)

    name = Column(String, nullable=False)
    
    charm = Column(Integer)
    cool = Column(Integer) 
    sharp = Column(Integer) 
    tough = Column(Integer)
    weird = Column(Integer) 
    
    luck = Column(Integer)
    harm = Column(Integer)
    experience = Column(Integer)
    
    pronouns = Column(String)
    description = Column(Text)
    history = Column(Text)
    notes = Column(Text)
    