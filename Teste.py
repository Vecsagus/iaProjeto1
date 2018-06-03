# coding=utf-8
from QuebraCabeca import QuebraCabeca
from Agente import Agente

novo_quebra_cabeca = QuebraCabeca([[5, 3, 2], [1, 0, 4], [6, 7, 8]])
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
