# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca


class Agente:
    fronteira_amplitude_1 = None
    fronteira_amplitude_2 = None

    def __init__(self):
        pass

    @staticmethod
    def esta_explorado(no_atual, lista):
        for item in lista:
            if item.estado == no_atual.estado:
                return True

        return False

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

            print("Explorados")
            print([item.estado for item in explorado])
            print("Atual")
            print(no_atual.estado)
            if not self.esta_explorado(no_atual, explorado):
                # adiciona ao conjunto de nós explorados
                explorado.add(no_atual)

                # move p/ esquerda
                move_para_esquerda = problema.transicao(problema.estado_atual, problema.acao.para_esquerda)
                if move_para_esquerda is not False:
                    fronteira.append(NoArvoreDeBusca(move_para_esquerda, no_atual, problema.acao.para_esquerda))

                # move p/ para_cima
                move_para_cima = problema.transicao(problema.estado_atual, problema.acao.para_cima)
                if move_para_cima is not False:
                    fronteira.append(NoArvoreDeBusca(move_para_cima, no_atual, problema.acao.para_cima))

                # move p/ direita
                move_para_direita = problema.transicao(problema.estado_atual, problema.acao.para_direita)
                if move_para_direita is not False:
                    fronteira.append(NoArvoreDeBusca(move_para_direita, no_atual, problema.acao.para_direita))

                # move p/ para_baixo
                move_para_baixo = problema.transicao(problema.estado_atual, problema.acao.para_baixo)
                if move_para_baixo is not False:
                    fronteira.append(NoArvoreDeBusca(move_para_baixo, no_atual, problema.acao.para_baixo))

    def busca_bidirecional(self, problema):
        pass
