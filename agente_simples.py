import matplotlib.pyplot as plt

from matriz import CORES_MATRIZ


def gerar_caminho_simples(matriz):
    caminho = []
    linhas = len(matriz) - 1
    colunas = len(matriz[0]) - 1

    for linha in range(1, linhas):
        if linha % 2 != 0:
            for coluna in range(1, colunas):
                caminho.append((linha, coluna))
        else:
            for coluna in range(1, colunas)[::-1]:
                caminho.append((linha, coluna))

    caminho_reverso = caminho[::-1]
    caminho_reverso.pop(0)  # remover primeiro
    caminho_reverso.pop()  # remover ultimo
    caminho.extend(caminho_reverso)

    return caminho


def exibir_caminho_simples(matriz):
    global posAPAx
    global posAPAy

    posAPAx = 1
    posAPAy = 1

    caminho_simples = gerar_caminho_simples(matriz)

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
