from openpt.model import Base
from openpt.model.sites import Site
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    site_id = Column(Integer, ForeignKey('site.id'))

    site = relationship(Site)

    def __init__(self, name, site):
        self.name = name
