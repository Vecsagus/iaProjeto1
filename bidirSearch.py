import random
from enum import Enum


class ProblemaQuebraCabeca:
    def __init__(self):
        self.estado_objetivo = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.estado_inicial = self.__gera_estado_inicial()
        self.estado_atual = self.estado_inicial
        self.acao = Enum('Acao', 'esquerda para_cima direita para_baixo')

    @staticmethod
    def __gera_estado_inicial():
        estado_inicial = []
        pecas = [i for i in range(9)]
        random.shuffle(pecas)
        estado_inicial.append([pecas[0], pecas[1], pecas[2]])
        estado_inicial.append([pecas[3], pecas[4], pecas[5]])
        estado_inicial.append([pecas[6], pecas[7], pecas[8]])
        return estado_inicial

    def transicao(self, estado, acao):
        for num, linha in enumerate(estado):
            for pos, peca in enumerate(linha):
                if peca == 0:
                    if acao == self.acao.esquerda and pos > 0:
                        (estado[num][pos], estado[num][pos - 1]) = (estado[num][pos - 1], estado[num][pos])
                    elif acao == self.acao.para_cima and num < 2:
                        (estado[num][pos], estado[num + 1][pos]) = (estado[num + 1][pos], estado[num][pos])
                    elif acao == self.acao.direita and pos < 2:
                        (estado[num][pos], estado[num][pos + 1]) = (estado[num][pos + 1], estado[num][pos])
                    elif acao == self.acao.para_baixo and num > 0:
                        (estado[num][pos], estado[num - 1][pos]) = (estado[num - 1][pos], estado[num][pos])
                        pass
                    else:
                        return [-1, 'Acao invalida']

    def teste_de_objetivo(self, estado):
        return cmp(self.estado_objetivo, estado)


class NoArvoreDeBusca():
    def __init__(self, estado, pai, acao):
        self.estado = estado
        self.pai = pai
        self.acao = acao


def busca_em_amplitude(problema):
    pass
    '''explorado, borda = set()
    borda.add(problema.estado_inicial)'''
