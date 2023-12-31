import unittest
from game.models import ScrabbleGame


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    
    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(players_count=3)


        self.assertEqual (scrabble_game.current_player, scrabble_game.players[0].playerid)


    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0].playerid

        scrabble_game.next_turn()
        self.assertEqual (scrabble_game.current_player, scrabble_game.players[1].playerid)

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 2, le toca al jugador 0
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2].playerid

        scrabble_game.next_turn()
        self.assertEqual (scrabble_game.current_player, scrabble_game.players[0].playerid)


if __name__ == '__main__':
    unittest.main()
