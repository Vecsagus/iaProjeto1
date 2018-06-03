# coding=utf-8
import random
from enum import Enum
from ArvoreDeBusca import NoArvoreDeBusca


class QuebraCabeca:
    def __init__(self, estado_inicial=None):
        self.estado_objetivo = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.estado_inicial = estado_inicial if not None else self.gera_estado_inicial()
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
        return estado

    def teste_de_objetivo(self, estado):
        return cmp(self.estado_objetivo, estado)

    # def imprime(estado):
    #     for linha in estado:
    #         print("-------")
    #         for coluna in linha:
    #             print("|" + str(coluna), end = "")
    #         print("|")
    #     print("-------")

    def busca_em_amplitude(self, problema):
        explorado = set()
        fronteira = []
        no_raiz = NoArvoreDeBusca(problema.estado_inicial, None, None)
        fronteira.append(no_raiz)

        while True:
            if not len(fronteira):
                return -1
            # seleciona e deleta o primeiro elemento da borda
            no_atual = fronteira[0]
            del fronteira[0]
            # retorna o estado atual se ele for igual ao objetivo
            if cmp(no_atual.estado, problema.estado_objetivo):
                return no_atual
            # adiciona ao conjunto de nós explorados
            explorado.add(no_atual)

            # move p/ esquerda
            move_para_esquerda = problema.transicao(problema.acao.para_esquerda)
            if move_para_esquerda is not False:
                fronteira.append(NoArvoreDeBusca(move_para_esquerda, no_atual, problema.acao.esquerda))

            # move p/ para_cima
            move_para_cima = problema.transicao(problema.acao.para_cima)
            if move_para_cima is not False:
                fronteira.append(NoArvoreDeBusca(move_para_cima, no_atual, problema.acao.para_cima))

            # move p/ direita
            move_para_direita = problema.transicao(problema.acao.para_direita)
            if move_para_direita[0] is not False:
                fronteira.append(NoArvoreDeBusca(move_para_direita, no_atual, problema.acao.direita))

            # move p/ para_baixo
            move_para_baixo = problema.transicao(problema.acao.para_baixo)
            if move_para_baixo[0] is not False:
                fronteira.append(NoArvoreDeBusca(move_para_baixo, no_atual, problema.acao.para_baixo))


def busca_bidirecional(self, problema):
    pass
