# coding=utf-8
import random


class QuebraCabeca:
    estado_objetivo = None
    estado_inicial = None
    estado_atual = None

    def __init__(self):
        self.estado_objetivo = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.estado_inicial = self._gera_estado_inicial()
        self.estado_atual = self.estado_inicial

    def _gera_estado_inicial(self):
        estado_inicial = []
        pecas = [i for i in range(9)]
        random.shuffle(pecas)
        estado_inicial.append([pecas[0], pecas[1], pecas[2]])
        estado_inicial.append([pecas[3], pecas[4], pecas[5]])
        estado_inicial.append([pecas[6], pecas[7], pecas[8]])
        return estado_inicial

    def para_direita(self):
        esta_mudado = False
        if self.estado_atual is not None:
            for linha_pos, linha in enumerate(self.estado_atual):
                for column_pos, peca in enumerate(linha):

                    if peca == 0 and column_pos < 2:
                        zero = self.estado_atual[linha_pos][column_pos]
                        prox = self.estado_atual[linha_pos][column_pos + 1]
                        self.estado_atual[linha_pos][column_pos] = prox
                        self.estado_atual[linha_pos][column_pos + 1] = zero
                        esta_mudado = True

            return esta_mudado

    def para_esquerda(self):
        esta_mudado = False
        if self.estado_atual is not None:
            for linha_pos, linha in enumerate(self.estado_atual):

                for column_pos, peca in enumerate(linha):

                    if (peca == 0) and (column_pos > 0):
                        zero = self.estado_atual[linha_pos][column_pos]
                        ante = self.estado_atual[linha_pos][column_pos - 1]
                        self.estado_atual[linha_pos][column_pos] = ante
                        self.estado_atual[linha_pos][column_pos - 1] = zero
                        esta_mudado = True

            return esta_mudado

    def para_cima(self):
        esta_mudado = False
        if self.estado_atual is not None:

            for linha_pos, linha in self.estado_atual:

                for column_pos, peca in linha:

                    if peca == 0 and linha_pos > 0:
                        zero = self.estado_atual[linha_pos][column_pos]
                        cima = self.estado_atual[linha_pos + 1][column_pos]
                        self.estado_atual[linha_pos][column_pos] = cima
                        self.estado_atual[linha_pos + 1][column_pos] = zero
                        esta_mudado = True

            return esta_mudado

    def para_baixo(self):
        esta_mudado = False
        if self.estado_atual is not None:
            for linha_pos, linha in self.estado_atual:

                for column_pos, peca in linha:

                    if peca == 0 and linha_pos < 2:
                        print(column_pos)
                        print(self.estado_atual[linha_pos])
                        zero = self.estado_atual[linha_pos][column_pos]
                        baixo = self.estado_atual[linha_pos - 1][column_pos]
                        self.estado_atual[linha_pos][column_pos] = baixo
                        self.estado_atual[linha_pos - 1][column_pos] = zero
                        esta_mudado = True

            return esta_mudado
