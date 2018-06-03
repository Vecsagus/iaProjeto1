# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca


class Agente:
    def __init__(self):
        pass

    def esta_explorado(self, no_atual):
        pass

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
            if no_atual.estado == problema.estado_objetivo:
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
