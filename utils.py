from grafo.vertice import Vertice


def pegar_vertices(matriz):
    vertices = []
    indice = 0
    for i in range(6):
        for j in range(6):
            if matriz[i][j] == 2:
                vertices.append(Vertice(i, j, indice))
                indice += 1
    return vertices


def definir_caminho(vertices):
    x = 1
    y = 1
    caminho_detalhado = [[x, y]]
    for vertice in vertices:
        while vertice.pegar_x() != x or vertice.pegar_y() != y:
            if x != vertice.pegar_x():
                if x < vertice.pegar_x():
                    x += 1
                else:
                    x -= 1
                caminho_detalhado.append([x, y])
            if y != vertice.pegar_y():
                if y < vertice.pegar_y():
                    y += 1
                else:
                    y -= 1
                caminho_detalhado.append([x, y])
    print(len(caminho_detalhado))
    return caminho_detalhado

