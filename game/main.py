from game.models import ScrabbleGame

def get_player_count():
    while True:
        try:
            player_count = int(input('Ingrese la cantidad de jugadores (1-4): '))
            if  0 < player_count <= 4 :
                break
            else:
                print('Ingrese un número correcto')

        except Exception as e:
            print('Ingrese un número por favor')

    return player_count

def get_inputs():
    
    inputs = [input(print("Seleccione las coordenadas de la letra inicial (X / Y): ",)),
              input(print("Seleccione la orientación de la palabra ( H / V ): ",)),   
              input(print("Seleccione la palabra a colocar: ",)),
              ]
    return inputs

def show_board(game):
    game # game.get_board

def show_player(game):
    game # game.get_current_player

def main():
    player_count = get_player_count()
    game = ScrabbleGame(player_count)
    while game.is_playing():
        show_board(game.get_board())
        show_player(game.get_current_player())
        word, coords, orientation = get_inputs()
        try:
            game.play(word, coords, orientation)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()