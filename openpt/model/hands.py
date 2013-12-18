from openpt.model import Base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table, ForeignKey, Column
from sqlalchemy.types import Integer

players_hands = Table(
    'players_hands',
    Base.metadata,
    Column('player', Integer, ForeignKey('players.id')),
    Column('hand', Integer, ForeignKey('handss.id'))
)


class Hand(Base):
    __table__ = "hands"

    id = Column('id', Integer, primary_key=True)
    big_blind = Column('big_blind', Integer)
    small_blind = Column('small_blind', Integer)

    players = relationship('Player', secondary=players_hands)

    def __init__(self):
        pass
