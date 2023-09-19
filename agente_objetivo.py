import matplotlib.pyplot as plt

from grafo.grafo import Grafo
from matriz import existe_sujeira, CORES_MATRIZ
from utils import pegar_vertices, definir_caminho


def gerar_caminho_objetivo():
    caminho = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
        (3, 4),
        (3, 3),
        (3, 2),
        (2, 2),
        (2, 3),
        (2, 4),
        (1, 4),
        (1, 3),
        (1, 2),
    ]

    return caminho


def exibir_caminho_objetivo(matriz):
    global posAPAx
    global posAPAy
    global pontos

    posAPAx = 1
    posAPAy = 1
    pontos = -1  # comeca em -1 pois o inicio do caminho (1,1) deve ser desconsiderado

    caminho_dijkstra = Grafo((pegar_vertices(matriz))).definir_menor_caminho()
    caminho_objetivo = definir_caminho(caminho_dijkstra)

    while existe_sujeira(matriz):
        for (x, y) in caminho_objetivo:
            posAPAx = x
            posAPAy = y
            pontos += 1

            exibir_matriz(matriz)

            if matriz[posAPAx][posAPAy] == 2:
                matriz[posAPAx][posAPAy] = 0
                pontos += 1
                exibir_matriz(matriz)

    print(f'Pontos -> {pontos}')


def exibir_matriz(matriz):
    plt.imshow(matriz, cmap=CORES_MATRIZ)

    plt.plot([posAPAy], [posAPAx], marker='o', color='r', ls='')

    plt.show(block=False)

    plt.pause(.3)
    plt.clf()
