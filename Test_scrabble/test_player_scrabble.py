import unittest
from Game.models import (Player, BagTiles)
class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(len(player_1.tiles), 7)

if __name__ == '__main__':
    unittest