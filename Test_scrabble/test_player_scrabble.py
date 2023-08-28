import unittest
from Game.models import (Player, BagTiles)
class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(len(player_1.tiles), 7)
    def test_refreshtiles(self):
        player_2 = Player()
        player_2.refreshtiles(2)
        self.assertEqual(len(player_2.tiles), 8)

if __name__ == '__main__':
    unittest