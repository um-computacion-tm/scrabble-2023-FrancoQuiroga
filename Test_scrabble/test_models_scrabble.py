import unittest
from Game.models import (
    BagTiles,
    Tile,
    Board,
    Cell,
   Calculatewordvalue

)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

"""class TestCalculateWordValue(unittest.TestCase):
    def test_word_nomult(self):
        

        word = [Cell().add_letter(Tile('C', 1)), 
                Cell(letter = Tile('A', 1)),
                 Cell(letter = Tile('S', 2)),
                 Cell(letter = Tile('A', 1)) 
        ]
        value = Calculatewordvalue.calculatewordvalue(word)
        self.assertEqual(value, 5)
    """#def test_word_mult_value(self):
        #word = [Cell(letter = Tile('C', 1)), 
         #       Cell(letter = Tile('A', 1), multiplier=3, multiplier_type= 'letter'),
          #       Cell(letter = Tile('S', 2)),
           #      Cell(letter = Tile('A', 1)) 
#
 #       ]
  #      value = calculatewordvalue(word)
   #     self.assertEqual(value, 7)

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
    def test_calculatevalue0(self):
        celda2 = Cell(1,'')
        self.assertEqual(celda2.calculate_value(), 0)
    def test_calculatevaluemultilpierletter(self):
        celda3 = Cell(2, 'letter')
        celda3.add_letter(Tile('P', 3))
        self.assertEqual(celda3.calculate_value(), 6)
    def test_calculatevaluemultilpierword(self):
        celda4 = Cell(2, 'Word')
        celda4.add_letter(Tile('P', 3))
        self.assertEqual(celda4.calculate_value(), 3)

if __name__ == '__main__':
    unittest.main()
