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

#lo armo con lista e indice, pero deberia probar de guardar un jugador como dict y pasarlo como parametro
#def generate_player_csv(file_name:str, player:dict):
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