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


def orientacion_input():
    while True:
        try:
            orientacion = str(input('Seleccione la orientación de la palabra ( H/V )'))
            if (orientacion == 'h') or (orientacion=='v') or (orientacion=='H') or (orientacion=='V'):
            #Tomar el input de la orientación y hacerlo uppercase
                orientacion.upper
                return orientacion
            else:
                raise Exception
        except Exception as e:
            print('Ingrese una letra correcta (H,V)')

def word_input():
    while True:
        try:
            palabra = str(input('Coloque la palabra deseada: '))
            return palabra        
        except Exception as e:
            print('Coloque solo letras porfavor: ')
            #Tomar el input de X e Y


def position_input():
    while True:
        try:
            
            position = []
            x_input = int(input('Ingrese la coordenada X de la palabra: '))
            y_input = int(input('Ingrese la coordenada Y de la palabra: '))
            if (0 <= x_input < 14) and (0 <= y_input < 14):
                position.append(x_input)
                position.append(y_input)
                return position 
            else:
               raise Exception
            
        except Exception as e:
            print('Elija un número, entre 0 y 15.')
        

def get_inputs():
        return  position_input(), word_input(), orientacion_input(), 

def menu_input_swaptiles(game):
    game.players[game.current_player].taketilesfromtilebag
    try:
        tileswap = int(input('Elija si quiere seguir jugando (1), o terminar el turno(2)'))
        if tileswap == 1:
            
            print ('Fichas Intercambiadas, Vuelva a elegir otra opción.')
            return 5
        if tileswap == 2:
            game.next_turn()
            return 4
        else:
            print('Elija un número correcto (1-2)')
    #print (FICHAS INTERCAMBIADAS)
    except Exception as e:
        print ('Elija un número porfavor')

def show_menu(game):
    print('Elija una opción: ')
    print('1) Jugar una palabra')   
    print('2) Cambiar una ficha')
    print('3) Terminar Juego')
    #print('4) Guardar juego')  
    while True:
        
        try:
            opcion = int(input())
            if opcion == 1:
                return 1
            elif opcion == 2:
               return menu_input_swaptiles(game)
                
            elif opcion == 3:
                return 3
            else:
                print('Ingrese un número válido(1-2-3)')
        
        except Exception as e:
            print('Ingrese un número válido (1-2-3)')
            

def show_board(game):
    game # game.get_board

def show_hand(game):
    game #game.get_player_hand

def show_player(game):
    game # game.get_current_player

def show_info(game):
    show_board(game.get_board())
    show_player(game.get_current_player())
    show_hand(game.get_player_hand())


def main():
    player_count = get_player_count()
    game = ScrabbleGame(player_count)
    while game.is_playing():
        show_info(game)
        exit_check = show_menu(game)

        if exit_check == 1:
            while True:
                try:
                    coords ,word ,orientation  = get_inputs()
                    game.play(word, coords, orientation)
                    return False
                except Exception as e:
                    print(e)
            
        if exit_check == 3:
                return False

        if exit_check == 4: #Por si el player quiere terminar su turno
            show_info(game)
            return show_menu(game)

        while exit_check == 5: #Por si el player quiere seguir jugando
            show_info(game)
            exit_check = show_menu(game)
        game.next_turn()


if __name__ == '__main__':
    main()