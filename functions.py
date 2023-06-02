import re
import json

def parse_json(file_name:str) -> list:
    lista= []
    with open (file_name, "r") as file:
         dict = json.load (file)
         lista = dict ["jugadores"]
    return lista

def print_player_position(una_lista:list):
    for player in una_lista:
        print ("  {0} - {1}".format(player["nombre"], player["posicion"]))

def print_player(una_lista:list):
    for index, player in enumerate(una_lista):
        print ("  {0} - {1}".format(index, player["nombre"]))

def print_complete_statistics(una_lista:list, indice:int):
    print("\nNombre: {0}\nTemporadas: {1}\nPuntos totales: {2}\nPromedio puntos por partido: {3}\nRebotes totales: {4}\n"
            "Promedio rebotes por partido: {5}\nAsistencias totales: {6}\nPromedio asistencias por partido: {7}\n"
            "Robos totales: {8}\nBloqueos totales: {9}\nPorcentaje tiros de campo: {10}\n"
            "Porcentaje tiros libres: {11}\nPorcentaje tiros triples: {12}\n".format(una_lista[indice]["nombre"],
            una_lista[indice]["estadisticas"]["temporadas"],
            una_lista[indice]["estadisticas"]["puntos_totales"],
            una_lista[indice]["estadisticas"]["promedio_puntos_por_partido"],
            una_lista[indice]["estadisticas"]["rebotes_totales"],
            una_lista[indice]["estadisticas"]["promedio_rebotes_por_partido"],
            una_lista[indice]["estadisticas"]["asistencias_totales"],
            una_lista[indice]["estadisticas"]["promedio_asistencias_por_partido"],
            una_lista[indice]["estadisticas"]["robos_totales"],
            una_lista[indice]["estadisticas"]["bloqueos_totales"],
            una_lista[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
            una_lista[indice]["estadisticas"]["porcentaje_tiros_libres"],
            una_lista[indice]["estadisticas"]["porcentaje_tiros_triples"]))

def generate_player_csv(file_name:str, una_lista:list, indice:int):
    with open(file_name, "w") as file:
        text = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}\n".format(una_lista[indice]["nombre"],
                  una_lista[indice]["posicion"],
                  una_lista[indice]["estadisticas"]["temporadas"],
                  una_lista[indice]["estadisticas"]["puntos_totales"],
                  una_lista[indice]["estadisticas"]["promedio_puntos_por_partido"],
                  una_lista[indice]["estadisticas"]["rebotes_totales"],
                  una_lista[indice]["estadisticas"]["promedio_rebotes_por_partido"],
                  una_lista[indice]["estadisticas"]["asistencias_totales"],
                  una_lista[indice]["estadisticas"]["promedio_asistencias_por_partido"],
                  una_lista[indice]["estadisticas"]["robos_totales"],
                  una_lista[indice]["estadisticas"]["bloqueos_totales"],
                  una_lista[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
                  una_lista[indice]["estadisticas"]["porcentaje_tiros_libres"],
                  una_lista[indice]["estadisticas"]["porcentaje_tiros_triples"],)
        file.write(text)

def search_player_by_name(una_lista:list):
    player_name_list = []
    name = input("Ingrese el nombre del jugador:\n")
    pattern = r".*" + name + r".*"
    for player in una_lista:
        if re.search(pattern, player["nombre"], re.IGNORECASE):
            player_name_list.append(player)
    return player_name_list

def show_player_prizes(una_lista:list):
    player_prizes = search_player_by_name(una_lista)
    for player in player_prizes:
        print("\n{}".format(player["nombre"]))
        prizes = player["logros"]
        for prize in prizes:
           print(prize)

def quick_sort (lista:list, clave )->list:
    lista_izquierda = []
    lista_derecha = []
    if (len(lista) <= 1):
        return lista
    else:
        pivote = lista[0][clave]
        for elemento in lista[1:]:
            if elemento[clave] > pivote:
                lista_derecha.append(elemento)
            else:
                lista_izquierda.append(elemento)
    lista_izquierda = quick_sort(lista_izquierda, clave)
    lista_izquierda.append(lista[0])
    lista_derecha = quick_sort(lista_derecha, clave)
    lista_izquierda.extend(lista_derecha)
    return lista_izquierda

def calculate_and_show_average_ppg_sort(una_lista:list):
    player_ppg_list = []
    for player in una_lista:
        player_dict = {"nombre" : player["nombre"], "ppg" : player["estadisticas"]["promedio_puntos_por_partido"]}
        player_ppg_list.append(player_dict) 
    for player in player_ppg_list:
        print(player)
    sort_key = "nombre"
    print("\n\n")
    player_list_sort = quick_sort(player_ppg_list, sort_key)
    for player in player_list_sort:
        print("Nombre: {0} - Promedio puntos por partido: {1}".format(player["nombre"], player["ppg"]))
    print("\n\n")

def search_player_by_name_hall_of_fame(una_lista:list):
    hall_of_fame_list = search_player_by_name(una_lista)
    for player in hall_of_fame_list:
        if "Miembro del Salon de la Fama del Baloncesto" in player["logros"]:
               print("Nombre: {0} es Miembro del Salon de la Fama del Baloncesto".format(player["nombre"]))
        else:
            print("\nNo pertenece al salon de la fama\n")

def calculate_and_show_most_rebounds(una_lista:list):
    max_rebounds = una_lista[0]["estadisticas"]["rebotes_totales"]
    player_max_rebounds = una_lista[0]["nombre"]
    for player in una_lista:
        if player["estadisticas"]["rebotes_totales"] > max_rebounds:
            max_rebounds = player["estadisticas"]["rebotes_totales"]
            player_max_rebounds = player["nombre"]
    print("El jugador con mas rebotes ({0}) es {1}".format((max_rebounds),(player_max_rebounds)))

def calculate_and_show_max_percentage_field_goals(una_lista:list):
    max_field_goals = una_lista[0]["estadisticas"]["porcentaje_tiros_de_campo"]
    player_max_field_goals = una_lista[0]["nombre"]
    for player in una_lista:
        if player["estadisticas"]["porcentaje_tiros_de_campo"] > max_field_goals:
            max_field_goals = player["estadisticas"]["porcentaje_tiros_de_campo"]
            player_max_field_goals = player["nombre"]
    print("El jugador con el mayor promedio de tiros de campo ({0}) es {1}".format((max_field_goals),(player_max_field_goals)))

def calculate_and_show_most_assists(una_lista:list):
    most_assists = una_lista[0]["estadisticas"]["asistencias_totales"]
    player_most_assists = una_lista[0]["nombre"]
    for player in una_lista:
        if player["estadisticas"]["asistencias_totales"] > most_assists:
            most_assists = player["estadisticas"]["asistencias_totales"]
            player_most_assists = player["nombre"]
    print("El jugador con el mas asistencias  ({0}) es {1}".format((most_assists),(player_most_assists)))

def calculate_and_show_highest_total_robberies(una_lista:list):
    highest_total_robberies = una_lista[0]["estadisticas"]["robos_totales"]
    player_highest_total_robberies = una_lista[0]["nombre"]
    for player in una_lista:
        if player["estadisticas"]["robos_totales"] > highest_total_robberies:
            highest_total_robberies = player["estadisticas"]["robos_totales"]
            player_highest_total_robberies = player["nombre"]
    print("El jugador con mas cantidad de robos totales ({0}) es {1}".format((highest_total_robberies),(player_highest_total_robberies)))

def calculate_and_show_highest_total_blocks(una_lista:list):
    highest_total_blocks = una_lista[0]["estadisticas"]["bloqueos_totales"]
    player_highest_total_blocks = una_lista[0]["nombre"]
    for player in una_lista:
        if player["estadisticas"]["bloqueos_totales"] > highest_total_blocks:
            highest_total_blocks = player["estadisticas"]["bloqueos_totales"]
            player_highest_total_blocks = player["nombre"]
    print("El jugador con mas cantidad de bloqueos totales ({0}) es {1}".format((highest_total_blocks),(player_highest_total_blocks)))

def calculate_and_show_ppg_average(una_lista:list):
    points_per_game = 0.00
    ppg_average = 0.00
    players = 0
    less_points = una_lista[0]["estadisticas"]["promedio_puntos_por_partido"]
    for player in una_lista:
        players = players + 1
        points_per_game = points_per_game + player["estadisticas"]["promedio_puntos_por_partido"]
        if player["estadisticas"]["promedio_puntos_por_partido"] < less_points:
            less_points = player["estadisticas"]["promedio_puntos_por_partido"]
    print(points_per_game)
    points_per_game = points_per_game - less_points
    print(points_per_game)
    players = players - 1
    print(players)
    ppg_average = points_per_game / players
    print("El promedio de puntos por partido del equipo (exlcuido aquel con la menor cantidad) es {0}".format((ppg_average)))

def calculate_and_show_highest_prizes(una_lista:list):
    highest_prizes = 0
    player_prizes = ""
    for player in una_lista:
        count_prizes = len(player["logros"])
        if count_prizes > highest_prizes:
            highest_prizes = count_prizes
            player_prizes = player["nombre"]
    print("El jugador con mas cantidad de premios ({0}) es {1}".format((highest_prizes),(player_prizes)))

def calculate_and_show_most_seasons(una_lista:list):
    most_seasons = una_lista[0]["estadisticas"]["temporadas"]
    player_most_seasons = una_lista[0]["nombre"]
    for player in una_lista:
        if player["estadisticas"]["temporadas"] > most_seasons:
            most_seasons = player["estadisticas"]["temporadas"]
            player_most_seasons = player["nombre"]
    print("El jugador con mas cantidad de temporadas jugadas ({0}) es {1}".format((most_seasons),(player_most_seasons)))

def show_players_average_points_comparison(una_lista:list):
    comparison = int(input("Por favor ingrese un valor de puntos por partido:\n"))
    print("Puntos a comparar", comparison)
    players = []
    for player in una_lista:
        if player["estadisticas"]["promedio_puntos_por_partido"] > comparison:
            players.append(player["nombre"])
    for player in players:
        print(player)

def show_players_average_rebounds_comparison(una_lista:list):
    comparison = int(input("Por favor ingrese un valor de rebotes por partido:\n"))
    print("Rebotes a comparar", comparison)
    players = []
    for player in una_lista:
        if player["estadisticas"]["promedio_rebotes_por_partido"] > comparison:
            players.append(player["nombre"])
    for player in players:
        print(player)

def show_players_average_assists_comparison(una_lista:list):
    comparison = int(input("Por favor ingrese un valor de asistencias por partido:\n"))
    print("Asistencias a comparar", comparison)
    players = []
    for player in una_lista:
        if player["estadisticas"]["promedio_asistencias_por_partido"] > comparison:
            players.append(player["nombre"])
    for player in players:
        print(player)

def show_players_free_throw_percentage_comparison(una_lista:list):
    comparison = int(input("Por favor ingrese un porcentaje de tiros libres por partido:\n"))
    print("Porcentaje de tiros libres a comparar", comparison)
    players = []
    for player in una_lista:
        if player["estadisticas"]["porcentaje_tiros_libres"] > comparison:
            players.append(player["nombre"])
    for player in players:
        print(player)

def show_players_3points_shooting_percentage_comparison(una_lista:list):
    comparison = int(input("Por favor ingrese un porcentaje de tiros triples por partido:\n"))
    print("Porcentaje de tiros triples a comparar\n", comparison)
    players = []
    for player in una_lista:
        if player["estadisticas"]["porcentaje_tiros_triples"] > comparison:
            players.append(player["nombre"])
    for player in players:
        print(player)

def show_players_field_goals_comparison(una_lista:list):
    comparison = int(input("Por favor ingrese un porcentaje de tiros de campo por partido:\n"))
    print("Porcentaje de tiros de campo a comparar\n", comparison)
    players = []
    for player in una_lista:
        if player["estadisticas"]["porcentaje_tiros_de_campo"] > comparison:
            players.append(player["nombre"])
    key = "posicion"
    sort_list = quick_sort(players, key)
    for player in sort_list:
        print(player)