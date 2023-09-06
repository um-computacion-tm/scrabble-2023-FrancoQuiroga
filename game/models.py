import random
class Calculatewordvalue():
    def __init__(self):
        pass
    def calculatewordvalue(word):
        finalvalue = 0
        for i in word:
            finalvalue += word[i].calculate_value



class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
class BagTiles:
    def __init__(self):
        self.tiles = [
            #tiles de 0 puntos
            Tile('', 0), Tile('', 0),
            #tiles de 1 punto
            Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1),
            Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1),
            Tile('E', 1),Tile('E', 1),Tile('E', 1),Tile('E', 1),
            Tile('E', 1), Tile('E', 1),Tile('E', 1),Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('I', 1),Tile('I', 1),Tile('I', 1),Tile('I', 1),Tile('I', 1),Tile('I', 1),
            Tile('L', 1), Tile('L', 1), Tile('L', 1), Tile('L', 1),
            Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1),
            Tile('O', 1), Tile('O', 1),Tile('O', 1),Tile('O', 1),Tile('O', 1),Tile('O', 1),
            Tile('O', 1),Tile('O', 1),Tile('O', 1),
            Tile('R', 1),Tile('R', 1),Tile('R', 1),Tile('R', 1),Tile('R', 1),
            Tile('S', 1),Tile('S', 1),Tile('S', 1),Tile('S', 1),Tile('S', 1),Tile('S', 1),
            Tile('T', 1),Tile('T', 1),Tile('T', 1),Tile('T', 1),
            Tile('U', 1),Tile('U', 1),Tile('U', 1),Tile('U', 1),Tile('U', 1),
            #Tile de 2 puntos
            Tile('D', 2), Tile('D', 2),Tile('D', 2),Tile('D', 2),Tile('D', 2),
            Tile('G', 2), Tile('G', 2),
            #Tile de 3 puntos
            Tile('B', 3), Tile('B', 3),
            Tile('C', 3), Tile('C', 3),Tile('C', 3),Tile('C', 3),
            Tile('M', 3),Tile('M', 3),
            Tile('P', 3),Tile('P', 3),
            #Tile de 4 puntos
            Tile('F', 4),
            Tile('H', 4),Tile('H', 4),
            Tile('V', 4),
            Tile('Y', 4),
            #Tiles de 5 puntos
            Tile('CH', 5), Tile('CH', 5),
            #Tiles de 8 puntos
            Tile('J', 8),Tile('LL', 8),Tile('RR', 8),Tile('Ñ', 8),Tile('X', 8),
            #Tiles de 10 púntos
            Tile('Z', 10),
        ]
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