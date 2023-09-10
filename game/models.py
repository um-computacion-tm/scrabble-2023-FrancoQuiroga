import random
class Calculatewordvalue():
    def __init__(self,word):
        self.word = word
        self.wordvalue = 0
    def calculatewordvalue(self):
        for i in self.word:
            currentcell = i
            self.wordvalue += currentcell.calculate_value
        return self.wordvalue



class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
class BagTiles:
    def __init__(self):
        self.tiles = []
        self.tiles.append(Tile('', 0) for x in range  (2))
        self.tiles.append(Tile('A', 1) for x in range(12))
        self.tiles.append(Tile('E', 1) for x in range(12))
        self.tiles.append(Tile('I', 1) for x in range(6))
        self.tiles.append(Tile('L', 1) for x in range(4))
        self.tiles.append(Tile('N', 1) for x in range(5))
        self.tiles.append(Tile('O', 1) for x in range(9))
        self.tiles.append(Tile('R', 1) for x in range(5))
        self.tiles.append(Tile('S', 1) for x in range(6))
        self.tiles.append(Tile('T', 1) for x in range(4))
        self.tiles.append(Tile('U', 1) for x in range(5))
        self.tiles.append(Tile('D', 2) for x in range(5))
        self.tiles.append(Tile('G', 2) for x in range(2))
        self.tiles.append(Tile('B', 3) for x in range(2))
        self.tiles.append(Tile('C', 3) for x in range(4))
        self.tiles.append(Tile('M', 3) for x in range(2))
        self.tiles.append(Tile('P', 3) for x in range(2))
        self.tiles.append(Tile('F', 4))
        self.tiles.append(Tile('H', 4) for x in range(2))
        self.tiles.append(Tile('V', 4))
        self.tiles.append(Tile('Y', 4))
        self.tiles.append(Tile('CH', 5))
        self.tiles.append(Tile('Q', 5))
        self.tiles.append(Tile('J', 8))
        self.tiles.append(Tile('LL', 8))
        self.tiles.append(Tile('Ñ', 8))
        self.tiles.append(Tile('RR', 8))
        self.tiles.append(Tile('X', 8))
        self.tiles.append(Tile('Z', 10))
        for element1 in self.tiles:
            if type(element1) == list:
                for element2 in element1:
                    self.tiles.append(element2)
                self.tiles.remove(element1)
            else:
                continue
        
        
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
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