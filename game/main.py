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

    
    while True:
        try:
            orientacion = str(input('Seleccione la orientación de la palabra ( H/V )'))
            if (orientacion == 'h') or (orientacion=='v') or (orientacion=='H') or (orientacion=='V'):
            #Tomar el input de la orientació
                orientacion.upper
            else:
                raise Exception
        except Exception as e:
            print('Ingrese una letra correcta (H,V)')

        try:
            palabra = str(input('Coloque la palabra deseada: '))
        except Exception as e:
            print('Coloque solo letras porfavor: ')
            #Tomar el input de X e Y
        try:
            position = []
            x_input = int(input('Ingrese la coordenada X de la palabra: '))
            y_input = int(input('Ingrese la coordenada Y de la palabra: '))
            if (0 <= x_input > 14) and (0 <= y_input > 14):
                position.append(x_input)
                position.append(y_input)
#            else :
 #               print('Ingrese un número entre 0 y 14')
        except Exception as e:
            print('Elija un número, entre 0 y 15.')

        return  position, orientacion, palabra

def show_menu(game):
    print('Elija una opción: ')
    print('1) Jugar una palabra')   
    print('2) Cambiar una ficha')
    print('3) Terminar Juego')
    #   print('4) Guardar juego')  
    exit = False
    while not exit:
        try:
            opcion = int(input(('Su opción:')))
            if opcion == 1:
                break
            elif opcion == 2:
                game.players[game.current_player].taketilesfromtilebag
                break
            elif opcion == 3:
                game.finish_game()
                exit = True
            else:
                print('Ingrese un número válido(1-2-3)')
        
        except Exception as e:
            print('Ingrese un número válido (1-2-3)')
            

def show_board(game):
    game # game.get_board

def show_player(game):
    game # game.get_current_player

def show_info(game):
    show_board(game.get_board())
    show_player(game.get_current_player())

def main():
    player_count = get_player_count()
    game = ScrabbleGame(player_count)
    while game.is_playing():
        show_info
#        show_menu(game)
        coords ,word ,orientation  = get_inputs()
        try:
            game.play(word, coords, orientation)
        except Exception as e:
            print(e)
        game.next_turn

if __name__ == '__main__':
    main()