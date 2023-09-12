import random

from matplotlib.colors import ListedColormap

CORES_MATRIZ = ListedColormap(['b', 'g', 'y'])


def gerar_matriz():
    matriz = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
    ]

    return matriz


def gerar_sujeira(matriz):
    qtd_sujeira = 0
    while qtd_sujeira < 9:
        x = random.randint(1, 4)
        y = random.randint(1, 4)

        if matriz[x][y] == 2:
            continue

        matriz[x][y] = 2
        qtd_sujeira += 1


def existe_sujeira(matriz):
    for linha in matriz:
        for coluna in linha:
            if coluna == 2:
                return True
    return False
