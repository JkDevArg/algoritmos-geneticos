from utils import genera_poblacion, generate_cities, selecciona_padres

from utils import cruza, muta

todas_ciudades = generate_cities(50, 0, 0, 100, 100)
poblacion = genera_poblacion(todas_ciudades, 100)

for generacion_id in range(1000):
    mejor_ruta = sorted(poblacion, key=lambda ruta: ruta.distancia)[0]
    print(f"{generacion_id}: {mejor_ruta.distancia:.3f}")

    padres_seleccionados = selecciona_padres(poblacion, 20)

    nuevos_hijos = cruza(padres_seleccionados, 100)

    hijos_mutados = muta(nuevos_hijos)

    poblacion = padres_seleccionados + hijos_mutados


