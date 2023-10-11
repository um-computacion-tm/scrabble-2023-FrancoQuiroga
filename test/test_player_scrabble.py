import unittest
from game.models import (Player, BagTiles)
class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(1)
        self.assertEqual(len(player_1.tiles), 7)
    def test_refreshtiles(self):
        player_2 = Player(2)
        player_2.refreshtiles(2)
        self.assertEqual(len(player_2.tiles), 9)
    def test_taketiletilebag(self):
        player_3 = Player(0)
        bolsaactual = BagTiles()
        player_3.taketilesfromtilebag()
        self.assertEqual(len(player_3.tiles), 7)
        self.assertEqual(len(bolsaactual.finaltiles), 100)
    def test_inicial(self):
        player_1 = Player(1)
        self.assertEqual(
            len(player_1.tiles),
            7,
        )
    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        player = Player(1)
        player.tiles = [
            ('H', 1),
            ('O', 1),
            ('L', 1),
            ('A', 1),
            ('C', 1),
            ('U', 1),
            ('M', 1),]
        tiles = [
            ('H', 1),
            ('O', 1),
            ('L', 1),
            ('A', 1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)
    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.finaltiles = [
            ('P', 1),
            ('O', 1),
            ('L', 1),
            ('A', 1),
            ('C', 1),
            ('U', 1),
            ('M', 1),
        ]
        tiles =  [('P', 1),
            ('O', 1),
            ('L', 1),
            ('A', 1),
            ('C', 1),
            ('U', 1),
            ('M', 1),
]
        player = Player(1)
        player.tiles = [
            ('H', 1),
            ('O', 1),
            ('L', 1),
            ('A', 1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, False)



    def test_validate_user_has_letters_dobleletter(self):
        bag_tile = BagTiles()
        player = Player(1)
        player.tiles = [
            ('O', 1),
            ('O', 1),
            ('LL', 1),
            ('A', 1),
            ('C', 1),
            ('U', 1),
            ('M', 1),]
        tiles = [
            ('O', 1),
            ('L', 1),
            ('L', 1),
            ('A', 1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_validate_user_has_letters_2(self):
        bag_tile = BagTiles()
        player = Player(1)
        player.tiles = [
            ('O', 1),
            ('L', 1),
            ('L', 4),
            ('A', 1),
            ('C', 1),
            ('U', 1),
            ('M', 1),]
        tiles = [
            ('O', 1),
            ('LL', 1),
            ('A', 1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_validate_user_has_not_letters(self):
        bag_tile = BagTiles()
        player = Player(1)
        player.tiles = [
            ('H', 1),
            ('O', 1),
            ('LL', 1),
            ('A', 1),
            ('C', 1),
            ('U', 1),
            ('M', 1),]
        tiles = [
            ('H', 1),
            ('O', 1),
            ('L', 1),
            ('A', 1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, False)

if __name__ == '__main__':
    unittest