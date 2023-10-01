import unittest
from game.models import (
    BagTiles,
    Tile,
    Board,
    Cell,


)

class Testwordinsideword(unittest.TestCase):

    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True
    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(word_is_valid)
    def test_already_empty(self):
        board = Board()
        board.validate_boardnotempty()
        self.assertTrue(board.is_empty)
    def test_board_is_empty(self):
        board = Board()
        board.validate_boardnotempty()
        assert board.is_empty == True
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(('C', 1))
        board.validate_boardnotempty()
        self.assertEqual(board.is_empty, False)
    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 8)
        orientation = "H"
        board.validate_boardnotempty()
        word_is_valid = board.validate_word_correct_placement(word, location, orientation)
        assert word_is_valid == True
    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        board.validate_boardnotempty()
        word_is_valid = board.validate_word_correct_placement(word, location, orientation)
        assert word_is_valid == False
    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (8, 7)
        orientation = "V"
        board.validate_boardnotempty()
        word_is_valid = board.validate_word_correct_placement(word, location, orientation)
        assert word_is_valid == True
    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_correct_placement(word, location, orientation)
        assert word_is_valid == False
    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(('C', 1))
        board.grid[8][7].add_letter(('A', 1)) 
        board.grid[9][7].add_letter(('S', 1)) 
        board.grid[10][7].add_letter(('A', 1)) 
        word = "Facultad"
        location = (7, 6)
        orientation = "H"
        board.validate_boardnotempty()
        word_is_valid = board.validate_word_correct_placement(word, location, orientation)
        self.assertTrue(word_is_valid)