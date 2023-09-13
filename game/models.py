import random
class Calculatewordvalue():
    def __init__(self,word):
        self.word = word
        self.wordvalue = 0
    def calculatewordvalue(self):
        for i in self.word:
            if i.multipliertype == 'letter':
                self.wordvalue += i.Tile().value * i.multiplier


class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
class BagTiles:
    def __init__(self):
        self.finaltiles = []
        self.tiles = [
            ('', 0, 2),
            ('A', 1, 12),
            ('E', 1, 12),
            ('I', 1, 6),
            ('L', 1, 4),
            ('N', 1, 5),
            ('O', 1, 9),
            ('R', 1, 5),
            ('S', 1, 6),
            ('T', 1, 4),
            ('U', 1, 5),
            ('D', 2, 5),
            ('G', 2, 2),
            ('B', 3, 2),
            ('C', 3, 4),
            ('M', 3, 2),
            ('P', 3, 2),
            ('F', 4, 1),
            ('H', 4, 2),
            ('V', 4, 1),
            ('Y', 4, 1),
            ('CH', 5, 1),
            ('Q', 5, 1),
            ('J', 8, 1),
            ('LL', 8, 1),
            ('Ñ', 8, 1),
            ('RR', 8, 1),
            ('X', 8, 1),
            ('Z', 10, 1),
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
    def __init__(self):
        self.INITIALTILES = 7
        self.tiles = BagTiles().take(self.INITIALTILES)
    def taketilesfromtilebag(self):
        self.tiles.pop(BagTiles().put(1))
        self.tiles.append(BagTiles().take(1))
        

    def refreshtiles(self, tiles_to_add):
        while tiles_to_add > 0:
            self.tiles.append(BagTiles().take(tiles_to_add))
            tiles_to_add -= 1

class ScrabbleGame:
    pass
class Cell:
    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None
    def add_letter(self, letter:Tile):
        self.letter = letter #(Tile with letter and points)
    def calculate_value(self):
        if self.letter == None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '') for _ in range(15) ]
            for _ in range(15)]