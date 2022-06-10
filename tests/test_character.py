import unittest

from src.character import *
from src.item import *


class TestCharacter(unittest.TestCase):
    def test_isdead(self):
        item1 = Item()
        item2 = Item()
        torch = Item('Torch', 1, 'Desc')
        lantern = Item('Lantern', '2', 'Desc')

        char = new_character('Jane', ['skill1', 'skill2'], {'key': item1, 'key2': item2})
        self.assertEqual(char.isdead(), False, 'The character should not be dead.')

        char = new_character('Jane', ['skill1', 'skill2'], {'key': item1, 'key2': item2})
        char.corruption = 5
        self.assertEqual(char.isdead(), True, 'The character should be dead (corruption).')

        char = new_character('Jane', ['skill1', 'skill2'], {'key': item1, 'key2': item2})
        self.assertEqual(char.isdead(), True, 'The character should be dead.')
        self.assertEqual(char.isdead(), True, 'The character should be dead.')
        self.assertEqual(char.isdead(), True, 'The character should be dead.')
