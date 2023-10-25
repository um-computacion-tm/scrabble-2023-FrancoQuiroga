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
    #Tomar el input de X e Y
    position = []
    try:
        x_input = int(input('Ingrese la coordenada X de la palabra: '))
        y_input = int(input('Ingrese la coordenada Y de la palabra: '))

        position.append(x_input)
        position.append(y_input)

    except Exception as e:
        print('Elija un número, en lo posible entre 0 y 15.')
    
    try:
        #Tomar el input de la orientación
        orientacion = str(input('Seleccione la orientación de la palabra ( H/V )'))
        if (orientacion == 'h') or (orientacion=='v') or (orientacion=='H') or (orientacion=='V'):
            orientacion.upper

        else:
            print('Porfavor elija (V o H)')
    except Exception as e:
        print('Ingrese una letra correcta (H,V)')


#    inputs = [input(print("Seleccione las coordenadas de la letra inicial (X / Y): ",)),
#              input(print("Seleccione la orientación de la palabra ( H / V ): ",)),   
#              input(print("Seleccione la palabra a colocar: ",)),
#              ]
#    return inputs

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