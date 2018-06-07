# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca


class Agente:
    borda_amplitude_1 = None
    borda_amplitude_2 = None

    def __init__(self):
        pass

    @staticmethod
    def nao_esta_na_borda(lista, no):
        try:
            lista.index(no)
            return False
        except Exception:
            return True

    @staticmethod
    def nao_esta_explorado(lista, estado):
        try:
            lista.index(estado)
            return False
        except Exception:
            return True

    #
    # Busca em amplitude
    #
    def busca_em_amplitude(self, jogo):

        no_raiz = NoArvoreDeBusca(jogo.estado_inicial, None, None)
        borda = []
        explorado = []
        borda.append(no_raiz)

        # retorna o estado atual se ele for igual ao objetivo
        if jogo.teste_de_objetivo(no_raiz.estado):
            return no_raiz

        while True:
            if len(borda) == 0:
                return -1
            # seleciona o primeiro item da fila
            no_atual = borda[0]

            # Remove o primeiro item da fila
            del borda[0]

            print(str(len(explorado)))

            # adiciona ao conjunto de nós explorados
            if no_atual.estado not in explorado:
                explorado.append(no_atual.estado)

                for acao in jogo.get_opcoes_possiveis():
                    novo_estado = jogo.transicao(no_atual.estado, acao)

                    if novo_estado is not False:
                        filho = NoArvoreDeBusca(novo_estado, no_atual, acao)
                        if filho not in borda:
                            # retorna o estado atual se ele for igual ao objetivo
                            if jogo.teste_de_objetivo(filho.estado):
                                return filho

                            borda.append(filho)

    #
    # Busca em profundidade limitada
    #
    def busca_em_profundidade_limitada(self, problema, limite):
        return self.bpl_recursiva(NoArvoreDeBusca(problema.estado_inicial, None, None), problema, limite)

    def bpl_recursiva(self, no, problema, limite):
        if problema.teste_de_objetivo(no.estado):
            return no
        elif limite == 0:
            return no
        else:
            pass

    def busca_bidirecional(self, problema):
        pass
