# coding=utf-8
import random
from enum import Enum
import copy

class QuebraCabeca:
    def __init__(self, estado_inicial=None):
        self.estado_objetivo = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.estado_inicial = estado_inicial if not None else self.gera_estado_inicial()
        self.acao = Enum('Acao', 'para_esquerda para_cima para_direita para_baixo')
        self.opcoes_possiveis = [
            self.acao.para_esquerda,
            self.acao.para_cima,
            self.acao.para_direita,
            self.acao.para_baixo,
        ]

    def get_opcoes_possiveis(self):
        return self.opcoes_possiveis

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
        estado_copy = copy.deepcopy(estado)
        for l, linha in enumerate(estado_copy):  # Linha
            for c, peca in enumerate(linha):  # Coluna
                if peca == 0:
                    if acao == self.acao.para_esquerda and (c > 0):
                        (estado_copy[l][c], estado_copy[l][c - 1]) = (estado_copy[l][c - 1], estado_copy[l][c])
                        self.estado_atual = estado_copy
                        return estado_copy

                    elif (acao == self.acao.para_cima) and (l > 0):
                        (estado_copy[l][c], estado_copy[l - 1][c]) = (estado_copy[l - 1][c], estado_copy[l][c])
                        self.estado_atual = estado_copy
                        return estado_copy

                    elif acao == self.acao.para_direita and (c < 2):
                        (estado_copy[l][c], estado_copy[l][c + 1]) = (estado_copy[l][c + 1], estado_copy[l][c])
                        self.estado_atual = estado_copy
                        return estado_copy

                    elif acao == self.acao.para_baixo and (l < 2):
                        (estado_copy[l][c], estado_copy[l + 1][c]) = (estado_copy[l + 1][c], estado_copy[l][c])
                        self.estado_atual = estado_copy
                        return estado_copy

                    else:
                        return False

    def teste_de_objetivo(self, estado):
        return self.estado_objetivo == estado

    def imprime(self, estado):
        for linha in estado:
            print("-------")
            for coluna in linha:
                print("|" + str(coluna))
            print("|")
        print("-------")
