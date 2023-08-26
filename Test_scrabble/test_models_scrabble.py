import unittest
from Game.models import (
    BagTiles,
    Tile,
    Board,
    Cell
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            100,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )


    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            102,
        )
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.grid), 15 )
    def test_cell(self):
        celda = Cell(2, 'letter')
        letra = Tile('A', 1)
        self.assertEqual(celda.multiplier, 2)
        self.assertEqual(celda.multiplier_type, 'letter')
        
        celda.add_letter(letra)
        self.assertEqual(celda.letter, letra)
    def test_calculatevalue(self):
        pass
if __name__ == '__main__':
    unittest.main()
