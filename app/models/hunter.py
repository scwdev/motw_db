from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relation, relationship

from app.database import Base, ID_and_Timestamps
from .association_tables import hunters_to_moves, hunters_to_gear


class Hunter(Base, ID_and_Timestamps):
    __tablename__ = "hunters"

    # many-to-one
    user_id = Column(Integer, ForeignKey('users.id'))
    playbook_id = Column(Integer, ForeignKey('playbooks.id'))
    
    # many-to-many
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
    notes = Column(Text)
    
    
    

    # email = Column(String, unique=True, index=True)
    # username = Column(String, unique=True, index=True)
    # public = Column(Boolean, index=True)
    
    # # TODO read about security
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)

    # groups = relationship("Group", back_populates="user") # many-to-many
    # hunters = relationship("Hunter", back_populates="user") # many-to-one
    # custom_moves = relationship("Move", back_populates="user") # many-to-one
    # custom_gear = relationship("Gear", back_populates="user") # many-to-one




    # items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")