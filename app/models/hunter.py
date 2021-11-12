from sqlalchemy import Boolean, Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from app.database import Base, ID_and_Timestamps


class Hunter(Base, ID_and_Timestamps):
    __tablename__ = "hunters"

    user_id = Column(Integer, ForeignKey('user.id'))

    name = Column(String, nullable=False)
    playbook = relationship("Playbook")

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