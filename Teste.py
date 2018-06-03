# coding=utf-8
from QuebraCabeca import QuebraCabeca

novo_quebra_cabeca = QuebraCabeca([[5, 3, 2], [1, 4, 0], [6, 7, 8]])
estadoInicial = novo_quebra_cabeca.estado_inicial
print(estadoInicial)
novo_estado = novo_quebra_cabeca.transicao(estadoInicial, novo_quebra_cabeca.acao.para_cima)
novo_estado = novo_quebra_cabeca.transicao(estadoInicial, novo_quebra_cabeca.acao.para_esquerda)
novo_estado = novo_quebra_cabeca.transicao(estadoInicial, novo_quebra_cabeca.acao.para_esquerda)
print(novo_estado)

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
