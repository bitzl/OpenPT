from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from openpt.model import Base
from sqlalchemy.orm import relationship


class Site(Base):
    __tablename__ = 'sites'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    players = relationship('Player')

    def __init__(self, name):
        self.name = name
