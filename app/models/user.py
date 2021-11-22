from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base, ID_and_Timestamps


class User(Base, ID_and_Timestamps):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    public = Column(Boolean, default=True, index=True)
    
    # TODO read about security
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    groups = relationship("Group", back_populates="user") # many-to-many
    hunters = relationship("Hunter") # one-to-many
    custom_moves = relationship("Move", back_populates="user") # one-to-many
    custom_gear = relationship("Gear", back_populates="user") # one-to-many

    def __init__(self, input):
        email = input['email']
        username = input['username']
        hashed_password = input['hashed_password']
        
    
        
    def __repr__(self):
        print(f"primary key (id): {self.id}, username: {self.username}, email: {self.email}")
        