# coding=utf-8
import random
from enum import Enum


class QuebraCabeca:
    estado_objetivo = None
    estado_inicial = None
    estado_atual = None

    def __init__(self, estado_inicial=None):
        self.estado_objetivo = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.estado_inicial = estado_inicial if not None else self.gera_estado_inicial()
        self.estado_atual = estado_inicial
        self.acao = Enum('Acao', 'para_esquerda para_cima para_direita para_baixo')

    @staticmethod
    def gera_estado_inicial():
        estado_inicial = []
        pecas = [i for i in range(9)]
        random.shuffle(pecas)
        estado_inicial.append([pecas[0], pecas[1], pecas[2]])
        estado_inicial.append([pecas[3], pecas[4], pecas[5]])
        estado_inicial.append([pecas[6], pecas[7], pecas[8]])
        return estado_inicial

    #
    # Executa a transição do espaço em branco ou seja o 0
    # Retorna um novo estado, caso não possa modificar o 0 então retorna False
    #
    def transicao(self, estado, acao):
        for l, linha in enumerate(estado):  # Linha
            for c, peca in enumerate(linha):  # Coluna
                if peca == 0:
                    if acao == self.acao.para_esquerda and (c > 0):
                        (estado[l][c], estado[l][c - 1]) = (estado[l][c - 1], estado[l][c])
                    elif (acao == self.acao.para_cima) and (l > 0):
                        (estado[l][c], estado[l - 1][c]) = (estado[l - 1][c], estado[l][c])
                    elif acao == self.acao.para_direita and (c < 2):
                        (estado[l][c], estado[l][c + 1]) = (estado[l][c + 1], estado[l][c])
                    elif acao == self.acao.para_baixo and (l < 2):
                        (estado[l][c], estado[l + 1][c]) = (estado[l + 1][c], estado[l][c])
                        pass
                    else:
                        return False

        self.estado_atual = estado
        return estado

    def teste_de_objetivo(self, estado):
        return self.estado_objetivo == estado

    def imprime(self, estado):
        for linha in estado:
            print("-------")
            for coluna in linha:
                print("|" + str(coluna))
            print("|")
        print("-------")
