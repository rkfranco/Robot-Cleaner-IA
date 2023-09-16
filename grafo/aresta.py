class Aresta:
    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino
        self.distancia = origem.calcular_distancia(destino)

    def pegar_destino(self):
        return self.destino

    def pegar_id_destino(self):
        return self.destino.pegar_id()

    def destino_lido(self):
        return self.destino.foi_lido()

    def origem_lido(self):
        return self.origem.foi_lido()

    def pegar_distancia(self):
        return self.distancia
