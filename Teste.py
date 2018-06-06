# coding=utf-8
from QuebraCabeca import QuebraCabeca
from Agente import Agente

modelo = [[5, 3, 2], [1, 0, 4], [6, 7, 8]]
modelo31 = [[1, 4, 2], [3, 5, 8], [6, 0, 7]]
novo_quebra_cabeca = QuebraCabeca()
agente = Agente()
resultado = agente.busca_em_amplitude(novo_quebra_cabeca)
print(resultado)

#
# novo_quebra_cabeca = QuebraCabeca()
# estadoInicial = novo_quebra_cabeca.estado_inicial
# print("--------INICIAL----------")
# print(estadoInicial)
# novo_quebra_cabeca.para_direita()
# print("--------ATUAL----------")
# print(novo_quebra_cabeca.estado_atual)
# novo_quebra_cabeca.para_baixo()
# print("--------ATUAL----------")
# print(novo_quebra_cabeca.estado_atual)
