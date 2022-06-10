import sys
import unittest
sys.path.append("..")

from src.character import *
from src.item import *


class TestCharacter(unittest.TestCase):
    def test_isdead(self):
        item1 = Item()
        item2 = Item()
        torch = Item('Torch', 1, 'Desc')
        lantern = Item('Lantern', '2', 'Desc')

        char = new_character('Jane', ['skill1', 'skill2'], [item1, item2])
        self.assertEqual(char.isdead(), False, 'The character should not be dead.')

        char = new_character('Jane', ['skill1', 'skill2'], [item1, item2])
        char.corruption = 5
        self.assertEqual(char.isdead(), True, 'The character should be dead (corruption).')

        char = new_character('Jane', ['skill1', 'skill2'], [item1, item2])
        char.conditions = ['condition1', 'condition2']
        self.assertEqual(char.isdead(), True, 'The character should be dead.')

        char = new_character('Jane', ['skill1', 'skill2'], [torch, item2])
        self.assertEqual(char.isdead(), True, 'The character should be dead.')

        char = new_character('Jane', ['skill1', 'skill2'], [lantern, item2])
        self.assertEqual(char.isdead(), True, 'The character should be dead.')


if __name__ == '__main__':
    unittest.main()
