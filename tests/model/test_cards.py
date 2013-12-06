from openpt.model.cards import Card, generate_deck
from unittest import TestCase


class CardTest(TestCase):

    def test_convert_name_to_value_for_numbers(self):
        for value in range(2, 11):
            self.assertEqual(Card.convert_name_to_value(str(value)), value)

    def test_convert_name_to_value_for_pictures(self):
        expected_pairings = [(11, 'J'), (12, 'Q'), (13, 'K'), (14, 'A')]
        for value, name in expected_pairings:
            self.assertEqual(Card.convert_name_to_value(name), value)

    def test_convert_value_to_namefor_numbers(self):
        for value in range(2, 11):
            self.assertEqual(Card.convert_value_to_name(value), str(value))

    def test_convert_value_to_name_for_pictures(self):
        expected_pairings = [(11, 'J'), (12, 'Q'), (13, 'K'), (14, 'A')]
        for value, name in expected_pairings:
            self.assertEqual(Card.convert_value_to_name(value), name)

    def test_single_argument_constructor(self):
        card = Card('4d')
        self.assertEqual(card.rank, '4')
        self.assertEqual(card.color, 'd')

    def test_two_argument_constructor(self):
        card = Card('4', 'd')
        self.assertEqual(card.rank, '4')
        self.assertEqual(card.color, 'd')

    def test_generate_deck(self):
        deck = generate_deck()
        self.assertEqual(len(deck), 52)
