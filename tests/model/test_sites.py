from unittest import TestCase
from openpt.model.sites import Site


class SiteTest(TestCase):

    def test_init(self):
        site = Site('Pokerstars')
        self.assertEqual(site.name, 'Pokerstars')
