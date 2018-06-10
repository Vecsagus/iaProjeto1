# coding=utf-8
from QuebraCabeca import QuebraCabeca
from Agente import busca_bidirecional

modelo = [[5, 3, 2], [1, 0, 4], [6, 7, 8]]
modelo31 = [[1, 4, 2], [3, 5, 8], [6, 0, 7]]
facil = [[1,2,5],[6,3,4],[7,8,0]]
facil2 = [[2,5,0],[1,6,3],[7,8,4]]
nao_facil = [[1,2,5],[6,3,4],[8,7,0]]
quebra_cabeca = QuebraCabeca(nao_facil)

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
