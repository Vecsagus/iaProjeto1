# coding=utf-8
from QuebraCabeca import QuebraCabeca
from Agente import busca_bidirecional

modelo = [[5, 3, 2], [1, 0, 4], [6, 7, 8]]
modelo31 = [[1, 4, 2], [3, 5, 8], [6, 0, 7]]
quebra_cabeca = QuebraCabeca(modelo31)

solucao = busca_bidirecional(quebra_cabeca)
print(solucao)


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
