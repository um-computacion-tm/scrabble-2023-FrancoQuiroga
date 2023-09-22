import random


class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
class BagTiles:
    def __init__(self):
        self.finaltiles = []
        self.tiles = [
            ('', 0, 2), ('A', 1, 12), ('E', 1, 12),
            ('I', 1, 6), ('L', 1, 4), ('N', 1, 5),
            ('O', 1, 9), ('R', 1, 5), ('S', 1, 6),
            ('T', 1, 4), ('U', 1, 5), ('D', 2, 5),
            ('G', 2, 2), ('B', 3, 2), ('C', 3, 4),
            ('M', 3, 2), ('P', 3, 2), ('F', 4, 1),
            ('H', 4, 2), ('V', 4, 1), ('Y', 4, 1),
            ('CH', 5, 1), ('Q', 5, 1), ('J', 8, 1),
            ('LL', 8, 1), ('Ñ', 8, 1), ('RR', 8, 1),
            ('X', 8, 1), ('Z', 10, 1),
        ]
        self.finaltiles += self.calculatetiles()        
        random.shuffle(self.tiles)
    def calculatetiles(self):
        totaltiles = []
        for letter,value, total in self.tiles:
            totaltiles.extend([(letter,value)] * total)
        return totaltiles
    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.finaltiles.pop())
        return tiles

    def put(self, tiles):
        self.finaltiles.extend(tiles)
class Player:
    def __init__(self, id):
        self.INITIALTILES = 7
        self.tiles = BagTiles().take(self.INITIALTILES)
        self.playerid = id
    def taketilesfromtilebag(self):
        tiletoswap = self.tiles.pop()
        BagTiles().put(tiletoswap)
        self.tiles.append(BagTiles().take(1))
    def refreshtiles(self, tiles_to_add):
        while tiles_to_add > 0:
            self.tiles.append(BagTiles().take(tiles_to_add))
            tiles_to_add -= 1
class ScrabbleGame:
    def __init__(self, players_count: int):
       self.board = Board()
       self.bag_tiles = BagTiles()
       self.current_player = 0
       self.players:list[Player] = []
       self.turncounter = 0
       for index in range(players_count):
           self.players.append(Player(id=index))
    def next_turn(self):
        
        if self.current_player == len(self.players)-1:
          self.current_player = 0 
        else:
            self.current_player += self.current_player + 1 
        self.turncounter += 1
    def validate_word(self, word, location, orientation):
        self.wordisvalid = False
        self.wordisvalid = self.board.validate_word_inside_board(word, location, orientation)
        '''
            1- Validar que usuario tiene esas letras
            2- Validar que la palabra entra en el tablero
            '''
        
    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''
    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''
class Cell:
    def __init__(self, multiplier, multiplier_type, letter = ('',0)):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = Tile(*letter)
    def add_letter(self, letter):
        self.letter = Tile(*letter) #(Tile with letter and points)
    def calculate_value(self):
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '', ('',0)) for _ in range(15) ]
            for _ in range(15)]
        self.is_empty = True
    def validate_boardnotempty(self):
        for row in self.grid:
            for cell in row:
                if cell.letter.letter != '':
                    self.is_empty = False
                    return
    def validate_word_inside_board(self, word, location, orientation):
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        if orientation == "H":
            if (position_x - 1) + len_word > 15:
                return False
#            if (position_x + 1) - len_word < 0:
#                return False
# Esta verificación es necesaria o no?
        if orientation == "V":
            if (position_y - 1) + len_word > 15:
                return False
#            if (position_y + 1) - len_word < 0:
#                return False
        else:
            return True
    def validate_word_has_space(self, word, location, orientation):
        pass
    @staticmethod
    def calculatewordvalue(word = list[Cell]):
        wordvalue = 0
        wordmultiplier = 1
        for cell in word:            
            lettervalue = 0
            lettervalue += cell.calculate_value()
            wordvalue += lettervalue
            if cell.multiplier_type == 'word':
                wordmultiplier = cell.multiplier
        wordvalue = wordvalue * wordmultiplier
        return wordvalue
    
    