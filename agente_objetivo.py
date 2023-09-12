import matplotlib.pyplot as plt

from matriz import existe_sujeira, CORES_MATRIZ


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

    posAPAx = 1
    posAPAy = 1

    caminho_objetivo = gerar_caminho_objetivo()

    while existe_sujeira(matriz):
        for (x, y) in caminho_objetivo:
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
