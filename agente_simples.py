import matplotlib.pyplot as plt

from matriz import CORES_MATRIZ


def gerar_caminho_simples():
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


def exibir_caminho_simples(matriz):
    global posAPAx
    global posAPAy

    posAPAx = 1
    posAPAy = 1

    caminho_simples = gerar_caminho_simples()

    while True:
        for (x, y) in caminho_simples:
            posAPAx = x
            posAPAy = y

            exibir_matriz(matriz)

            if matriz[posAPAx][posAPAy] == 2:
                matriz[posAPAx][posAPAy] = 0
                exibir_matriz(matriz)


def exibir_matriz(matriz):
    plt.imshow(matriz, cmap=CORES_MATRIZ)

    plt.plot([posAPAy], [posAPAx], marker='o', color='r', ls='')

    plt.show(block=False)

    plt.pause(.3)
    plt.clf()
