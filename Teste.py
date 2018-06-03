# coding=utf-8
from QuebraCabeca import QuebraCabeca

novo_quebra_cabeca = QuebraCabeca()
estadoInicial = novo_quebra_cabeca.estado_inicial
print("--------INICIAL----------")
print(estadoInicial)
novo_quebra_cabeca.para_direita()
print("--------ATUAL----------")
print(novo_quebra_cabeca.estado_atual)
novo_quebra_cabeca.para_baixo()
print("--------ATUAL----------")
print(novo_quebra_cabeca.estado_atual)
