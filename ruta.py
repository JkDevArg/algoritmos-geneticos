from city import Ciudad


class Ruta: # Este es nuestro "cromosoma"
    def __init__(self, ciudades):
        self.ciudades = ciudades
        self.distancia = sum(
            (a.distancia(b) for a, b in zip(self.ciudades[1:], self.ciudades[:-1]))
        )




















        #self.distancia = 0
        #for i in range(len(self.ciudades)- 1):
        #    self.distancia += self.ciudades[i].distancia(self.ciudades[i+1])