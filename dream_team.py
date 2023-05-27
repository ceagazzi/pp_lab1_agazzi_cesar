import re
import json
from functions import*

player_list = parse_json("/Users/CEA/Programacion/pp_lab1_agazzi_cesar/dt.json")
finish = True
while(finish):
    answer = int(input("\n\nPor favor ingrese una opción:\n"
                        "1-Mostrar la lista de todos los jugadores del Dream Team.\n"
                        "2-Mostrar estadisticas completas de un jugador:\n"
                        "3-Generar archivo CSV del jugador elegido"))
     
    match(answer):
        case 1:
            print_player_position(player_list)
        
        case 2:
             print_player(player_list)
             answer_player = int(input("\nSeleccione un jugador de la lista:"))
             print_complete_statistics(player_list,answer_player)

        case 3:
            generate_player_csv("jugador.csv", player_list, answer_player)
