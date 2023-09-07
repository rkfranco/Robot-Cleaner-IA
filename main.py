# Função que exibe o ambiente na tela
import random

import matplotlib.pyplot as plt


# Funciona apenas em ambientes com a biblioteca matplotlib instalada.

def is_not_clean(mat):
    for row in mat:
        for column in row:
            if column == 2:
                return True
    return False


def generate_trash(out_matriz):
    qtd_trash = 0
    while qtd_trash < 9:
        x = random.randint(1, 4)
        y = random.randint(1, 4)
        if out_matriz[x][y] == 2:
            continue
        out_matriz[x][y] = 2
        qtd_trash += 1


# Função que exibe o ambiente na tela
def exibir(matriz):
    global posAPAx
    global posAPAy

    posAPAx = 1
    posAPAy = 1

    while is_not_clean(matriz):
        for position in matriz_path:
            posAPAx = position[0]
            posAPAy = position[1]

            # Altera o esquema de cores do ambiente
            plt.imshow(matriz, 'gray')
            plt.nipy_spectral()

            # Coloca o agente no ambiente
            plt.plot([posAPAy], [posAPAx], marker='o', color='r', ls='')

            plt.show(block=False)

            # Pausa a execução do código por 0.5 segundos para facilitar a visualização
            plt.pause(1)
            plt.clf()

            if matriz[posAPAx][posAPAy] == 2:
                matriz[posAPAx][posAPAy] = 0


matriz = [[1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1]]

matriz_path = [
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 1],
    [4, 2],
    [4, 3],
    [4, 4],
    [3, 4],
    [3, 3],
    [3, 2],
    [2, 2],
    [2, 3],
    [2, 4],
    [1, 4],
    [1, 3],
    [1, 2]
]

generate_trash(matriz)

exibir(matriz)
