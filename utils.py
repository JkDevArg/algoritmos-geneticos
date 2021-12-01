from city import Ciudad
from ruta import Ruta
import csv
import random
from copy import deepcopy



def generate_cities(
    city_count: int, minx: int, miny: int, maxx: int, maxy: int
):
    cities = set()
    with open("cities.csv", encoding="utf8") as readable:
        reader = csv.reader(readable)
        for raw_city in reader:
            x = random.randint(minx, maxx)
            y = random.randint(miny, maxy)
            cities.add(Ciudad(name=raw_city[0], x=x, y=y))
    return set(random.sample(cities, city_count))


def genera_poblacion(ciudades, pop_size):
    poblacion = []
    for _ in range(pop_size):
        poblacion.append(
            Ruta(random.sample(ciudades, len(ciudades)))
        )
    return poblacion

def selecciona_padres(poblacion, n_padres):
    ordenados_por_distancia = sorted(poblacion, key=lambda ruta: ruta.distancia)
    return ordenados_por_distancia[:n_padres]

def _cruza_dos_padres(padre1, padre2):
    hijo = deepcopy(padre2)

    elementos = 3

    for posicion_p1, valor_p1 in enumerate(padre1):
        posicion_p2 = hijo.index(valor_p1)
        hijo[posicion_p2] = hijo[posicion_p1]
        hijo[posicion_p1] = valor_p1

    return hijo


def cruza(mejora_padres, pop_size):
    hijos_faltantes = pop_size - len(mejora_padres)

    nuevos_hijos = []
    for _ in range(hijos_faltantes):
        padre1, padre2 = random.sample(mejora_padres, 2)
        nuevo_hijo = Ruta(_cruza_dos_padres(padre1.ciudades, padre2.ciudades))

        nuevos_hijos.append(nuevo_hijo)
    return nuevos_hijos


def muta(nuevos_hijos):
    hijos_mutados = []

    for hijo in nuevos_hijos:
        ciudades = deepcopy(hijo.ciudades)

        if 0.5 > random.random():
            swap_from = random.randint(0, len(ciudades) -1)
            swap_to = random.randint(0, len(ciudades) -1)
            while swap_to == swap_from:
                swap_to = random.randint(0, len(ciudades) -1)

            aux = ciudades[swap_to]
            ciudades[swap_to] = ciudades[swap_from]
            ciudades[swap_from] = aux

    hijos_mutados.append(Ruta(ciudades))

    return hijos_mutados

