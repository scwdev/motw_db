from sqlalchemy import Table, Column, ForeignKey

from app.database import Base


hunters_to_moves = Table('association', Base.metadata,
    Column('hunter_id', ForeignKey('hunters.id'), primary_key=True),
    Column('move_id', ForeignKey('moves.id'), primary_key=True)
)

hunters_to_gear = Table('association', Base.metadata,
    Column('hunter_id', ForeignKey('hunters.id'), primary_key=True),
    Column('gear.id', ForeignKey('gear.id'), primary_key=True))