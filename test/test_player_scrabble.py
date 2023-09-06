import unittest
from game.models import (Player, BagTiles)
class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(len(player_1.tiles), 7)
    def test_refreshtiles(self):
        player_2 = Player()
        player_2.refreshtiles(2)
        self.assertEqual(len(player_2.tiles), 9)
 #   def test_taketiletilebag(self):
  #      player_3 = Player()
#        player_3.taketilesfromtilebag()
 #       self.assertEqual(len(player_3.tiles), 7)
  #      self.assertEqual(len(BagTiles.tiles), 100)
if __name__ == '__main__':
    unittest