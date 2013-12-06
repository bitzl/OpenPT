from openpt.model import Base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Enum


class Card(Base):
    __tablename__ = 'cards'
    _ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    _colors = [u'h', u's', u'd', u'c']
    id = Column(Integer, primary_key=True)
    color = Column(Enum(_colors))
    rank = Column(Enum(_ranks))

    def __init__(self, rank, color=None):
        if color == None:
            # Allow single string like Card('4h')
            rank, color = rank[0], rank[1]
        self.rank = rank
        self.color = color

    def set_color(self, value):
        if type(value) == 'string':
            self.value = Card._colors.index(value)
        else:
            self.value = value

    def __str__(self, ):
        return "Card(%s%s)" % (self.rank, self.color)

    @staticmethod
    def convert_name_to_value(name):
        return Card._ranks.index(name) + 2

    @staticmethod
    def convert_value_to_name(value):
        return Card._ranks[value - 2]


def generate_deck():
    '''Generates all cards in a deck to initialize the database.'''
    deck = []
    for color in Card._colors:
        for rank in Card._ranks:
            deck.append(Card(rank, color))
    return deck
