import re
import json
from functions import*

player_list = parse_json("/Users/CEA/Programacion/pp_lab1_agazzi_cesar/dt.json")
finish = True
flag_case = 0
while(finish):
    answer = int(input("\n\nPor favor ingrese una opción:\n"
                        "1-Mostrar la lista de todos los jugadores del Dream Team.\n"
                        "2-Mostrar estadisticas completas de un jugador:\n"
                        "3-Generar archivo CSV del jugador elegido.\n"
                        "4-Buscar jugador y mostrar sus logros.\n"
                        "5-Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team.\n"
                        "6-Buscar jugador y mostrar si es miembro del salon de la fama.\n"
                        "7-Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n"
                        "8-Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.\n"
                        "9-Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.\n"
                        "10-Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.\n"
                        "11-Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n"
                        "12-Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n"
                        "13-Calcular y mostrar el jugador con la mayor cantidad de robos totales.\n"
                        "14-Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.\n"
                        "15-Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor\n"
                        "16-Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n"
                        "17-Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.\n"
                        "18-Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n"
                        "19-Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.\n"
                        "20-Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n"
                        "23-BONUS Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking: (Exportar a CSV)\n\tPuntos\n\tRebotes\n\tAsistencias\n\tRobos\n"
                        "24-Determinar la cantidad de jugadores que hay por cada posición.\n"
                        "25-Salir del programa.\n\n"
                        "Opcion: \n"))
     
    match(answer):
        case 1:
            print_player_position(player_list)
        case 2:
             print_player(player_list)
             answer_player = int(input("\nSeleccione un jugador de la lista:"))
             print_complete_statistics(player_list,answer_player)
             flag_case = 1
        case 3:
            if flag_case == 0:
                print("Primero debe seleccionar la opcion 2\n")
            else:                    
                generate_player_csv("jugador.csv", player_list, answer_player)
                print("\nEl archivo CSV del jugador elegido fue generado correctamente\n")        
        case 4:
            show_player_prizes(player_list)
        case 5:
            calculate_and_show_average_ppg_sort(player_list)
        case 6:
            search_player_by_name_hall_of_fame(player_list)
        case 7:
            calculate_and_show_most_rebounds(player_list)
        case 8:
            calculate_and_show_max_percentage_field_goals(player_list)
        case 9:
            calculate_and_show_most_assists(player_list)
        case 10:
            print(show_players_average_points_comparison(player_list))
        case 11:
            print(show_players_average_rebounds_comparison(player_list))
        case 12:
            print(show_players_average_assists_comparison(player_list))
        case 13:
            calculate_and_show_highest_total_robberies(player_list)
        case 14:
            calculate_and_show_highest_total_blocks(player_list)
        case 15:
            print(show_players_free_throw_percentage_comparison(player_list))
        case 16:
            calculate_and_show_ppg_average(player_list)
        case 17:
            calculate_and_show_highest_prizes(player_list)
        case 18:
            show_players_3points_shooting_percentage_comparison(player_list)
        case 19:
            calculate_and_show_most_seasons(player_list)
        case 20:
            show_players_field_goals_comparison(player_list)
        case 23:
            position_in_ranking(player_list)
        case 24:
            position_quantity(player_list)
        case 25:
            finish = False
            print("\n***** Usted ha salido del programa *****\n")