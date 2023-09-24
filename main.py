from agente_objetivo import exibir_caminho_objetivo
from agente_simples import exibir_caminho_simples
from matriz import gerar_matriz, gerar_sujeira

matriz = gerar_matriz()
gerar_sujeira(matriz)

#exibir_caminho_simples(matriz)
exibir_caminho_objetivo(matriz)
