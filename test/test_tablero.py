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
        board.validate_word_correct_placement(word, location, orientation)
        word_is_valid = board.word_is_valid
        self.assertTrue(word_is_valid)
    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        board.validate_boardnotempty()
        board.validate_word_correct_placement(word, location, orientation)
        word_is_valid = board.word_is_valid
        assert word_is_valid == False
    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (8, 7)
        orientation = "V"
        board.validate_boardnotempty()
        board.validate_word_correct_placement(word, location, orientation)
        word_is_valid = board.word_is_valid
        self.assertTrue(word_is_valid)
    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        board.validate_word_correct_placement(word, location, orientation)
        word_is_valid = board.word_is_valid
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
    def test_board_multiplier_type_word(self):
        tablero = Board()
        tablero.get_multiplier()
        WORDx3 = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        for coordinate in WORDx3:
            self.assertEqual(tablero.grid[coordinate[0]][coordinate[1]].multiplier_type, 'word')

    def test_board_multiplier_type_letter(self):
        tablero = Board()
        tablero.get_multiplier()
        LETTERx3 = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        for coordinate in LETTERx3:
            self.assertEqual(tablero.grid[coordinate[0]][coordinate[1]].multiplier_type, 'letter')

    def test_board_multiplier_wordx2(self):
        tablero = Board()
        tablero.get_multiplier()
        WORDx2 = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), 
                  (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        for coordinate in WORDx2:
            self.assertEqual(tablero.grid[coordinate[0]][coordinate[1]].multiplier, 2)

    
    def test_board_multiplier_letterx3(self):
        tablero = Board()
        tablero.get_multiplier()
        LETTERx3 = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        
        for coordinate in LETTERx3:
            self.assertEqual(tablero.grid[coordinate[0]][coordinate[1]].multiplier, 3)
    
    def test_board_set_multiplier(self):
        tablero = Board()
        tablero.set_multiplier((1,1),2,'word')
        self.assertEqual(tablero.grid[1][1].multiplier, 2)
        self.assertNotEqual(tablero.grid[1][1].multiplier_type, 'letter')


        