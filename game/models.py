import random
#from pyrae import dle

class DictionaryConnectionError(Exception):
    pass
class InvalidWordException(Exception):
    pass
class InvalidPlaceWordException(Exception):
    pass
#dle.set_log_level(log_level='CRITICAL')

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
    def __repr__(self):
        return f"{self.letter}:{self.value}"

class BagTiles:
    def __init__(self):
        self.finaltiles = []
        self.tiles = [
            ('', 0, 2), ('A', 1, 12), ('E', 1, 12),
            ('I', 1, 6), ('L', 1, 6), ('N', 1, 5),
            ('O', 1, 9), ('R', 1, 7), ('S', 1, 6),
            ('T', 1, 4), ('U', 1, 5), ('D', 2, 5),
            ('G', 2, 2), ('B', 3, 2), ('C', 3, 5),
            ('M', 3, 2), ('P', 3, 2), ('F', 4, 1),
            ('H', 4, 3), ('V', 4, 1), ('Y', 4, 1),
            ('Q', 5, 1), ('J', 8, 1),
            ('Ñ', 8, 1),
            ('X', 8, 1), ('Z', 10, 1),
        ]
        self.finaltiles += self.calculatetiles()        
        random.shuffle(self.finaltiles)
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

    def has_letters(self, tiles):
        neededtiles = len(tiles)
        actualtiles = 0
        has_letter = True
        checkingtiles = self.tiles.copy()
        for i in checkingtiles:
            if i in tiles and (neededtiles > len(checkingtiles)):
                actualtiles += 1
                checkingtiles.remove(i)
            if i not in tiles and (neededtiles > actualtiles): #Verifies that you dont checks for more tiles than you need
                has_letter = False
                return has_letter
        return has_letter
                
class ScrabbleGame:
    def __init__(self, players_count: int):
       self.board = Board()
       self.bag_tiles = BagTiles()
       self.current_player = 0
       self.players:list[Player] = []
       self.turncounter = 0
       for index in range(players_count):
           self.players.append(Player(id=index))

    def is_playing(self):
        return True
    
    def finish_game(self):
        return False

    def play(self, word, location, orientation):
            self.validate_word(word, location, orientation)
            words = self.board.put_words(word, location, orientation)
            total = self.board.calculatewordvalue(words)
            self.players[self.current_player].score += total
            self.next_turn()

    def get_board(self):
        self.board.show_board()

    def get_current_player(self):
        print(self.current_player)

    def next_turn(self):
        
        if self.current_player == len(self.players)-1:
          self.current_player = 0 
        else:
            self.current_player += self.current_player + 1 
        self.turncounter += 1

    def validate_word(self, word, location, orientation):
            self.board.validate_boardnotempty()
            if not self.board.dict_validate_word(word):
                raise InvalidWordException("Su palabra no existe en el diccionario")
            if not self.board.validate_word_inside_board(word, location, orientation):
                raise InvalidPlaceWordException("Su palabra excede el tablero")
            if not self.board.validate_word_correct_placement(word, location, orientation):
                raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")
    '''
            1- Validar que usuario tiene esas letras 
            2- Validar que la palabra entra en el tablero y que si el tablero está vacio la palabra esté en medio
            2.1-Validar que la palabra este junto a otra
            3-Validar que la palabra existe

            '''
        
    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion position_y orientacion 
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
    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '
        
class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '', ('',0)) for _ in range(15) ]
            for _ in range(15)]
        self.is_empty = True
        self.word_is_valid = False

    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )

    def validate_boardnotempty(self): #Verifica si el tablero está vacio o no.
        for row in self.grid:
            for cell in row:
                if cell.letter.letter != '':
                    self.is_empty = False
                    return

    def validate_word_inside_board(self, word, location, orientation):
        #Esta función verifica que la palabra entre en el tablero
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        if orientation == "H":
            if (position_x - 1) + len_word > 15:
                return False
        if orientation == "V":
            if (position_y - 1) + len_word > 15:
                return False
        else:
            return True

    def validate_word_correct_placement(self, word, location, orientation):
    #Esta función verifica que la palabra este colocada en el centro(Con el tablero vacío), o
    #adyacente a otra palabra, o que intersecte otra palabra
        position_x = location[0]
        position_y = location[1]

        if self.is_empty == True and (position_x == 8 or position_y == 8):
            self.word_is_valid = True

        if self.is_empty == False:
            for i in range(len(word)):
                if (position_x + i > 0 and self.grid[position_x + i][position_y].letter.letter != '') or \
                (position_x + i < 14 and self.grid[position_x + i + 1][position_y].letter.letter != ''):
                    self.word_is_valid = True
            return self.word_is_valid
                
       

        return self.word_is_valid

#    def dict_validate_word(word):
#        search = dle.search_by_word(word=word)
#        if search is None:
#            raise DictionaryConnectionError()
#        return search.meta_description != 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'


    @staticmethod
    def calculatewordvalue(word = list[Cell]):
        #Calcula el valor de la palabra
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