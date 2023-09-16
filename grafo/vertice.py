class Vertice:
    def __init__(self, x, y, contador):
        self.x = x
        self.y = y
        self.id = contador
        self.lido = False
        self.arestas = []

    def pegar_x(self):
        return self.x

    def pegar_y(self):
        return self.y

    def definir_lido(self, lido):
        self.lido = lido

    def foi_lido(self):
        return self.lido

    def acessar_arestas(self):
        return self.arestas

    def pegar_id(self):
        return self.id

    def add_aresta(self, aresta):
        self.arestas.append(aresta)

    def calcular_distancia(self, ponto):
        return abs(self.x - ponto.x) + abs(self.y - ponto.y)

    def __repr__(self):
        return f'Vertice {self.id}: (X: {self.x} | Y: {self.y} | lido: {self.lido}) \n'
