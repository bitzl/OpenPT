from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from openpt.model import Base


class Site(Base):
    __tablename__ = 'sites'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
