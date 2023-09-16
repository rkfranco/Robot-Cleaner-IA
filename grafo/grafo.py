from grafo.aresta import Aresta


def tratar_caminho(vertices, distancia):
    vertices_copia = vertices.copy()
    resposta = [vertices[0]]

    for vertice in vertices_copia:
        vertice.definir_lido(False)

    for i in distancia:
        index = menor_distancia(distancia, vertices)
        resposta.append(vertices[index])
        vertices[index].definir_lido(True)
    print(resposta)
    return resposta


def menor_distancia(distancia, vertices):
    menor_valor = 100
    index = 0
    for i in range(len(distancia)):
        if (not vertices[i].foi_lido()) and menor_valor > distancia[i]:
            menor_valor = distancia[i]
            index = i
    return index


class Grafo:
    def __init__(self, vertices):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if i != j:
                    vertices[i].add_aresta(Aresta(vertices[i], vertices[j]))
        self.vertices = vertices

    def definir_menor_caminho(self):
        vertices = self.vertices
        distancia = [0]
        # caminho = [None]

        for i in range(1, 9):
            distancia.append(99)
            # caminho.append(None)

        for i in range(len(vertices)):
            index = menor_distancia(distancia, vertices)
            temp_dist = 99
            destino_id = 0
            for aresta in vertices[index].acessar_arestas():
                if not aresta.destino_lido():
                    dist = distancia[index] + aresta.pegar_distancia()
                    if dist < temp_dist:
                        destino_id = aresta.pegar_id_destino()
                        temp_dist = dist

            if temp_dist != 99:
                distancia[destino_id] = temp_dist
                # caminho[destino_id] = vertices[index]
            vertices[index].definir_lido(True)
        return tratar_caminho(vertices, distancia)
