# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca


class Agente:
    fronteira_amplitude_1 = None
    fronteira_amplitude_2 = None

    def __init__(self):
        pass

    @staticmethod
    def esta_na(lista, estado):
        for item in lista:
            if item.estado == estado:
                return True

        return False

    def busca_em_amplitude(self, jogo):

        explorado = set()
        borda = list()
        no_raiz = NoArvoreDeBusca(jogo.estado_inicial, None, None)
        borda.insert(0, no_raiz)

        # retorna o estado atual se ele for igual ao objetivo
        if jogo.teste_de_objetivo(no_raiz.estado):
            return no_raiz

        while True:
            if not len(borda):
                return -1
            # seleciona e deleta o primeiro elemento da borda
            no_atual = borda[0]
            borda.remove(no_atual)
            # adiciona ao conjunto de nós explorados
            explorado.add(no_atual)
            print("Qty Explorados ->" + str(len(explorado)))

            for acao in jogo.get_opcoes_possiveis():
                novo_estado = jogo.transicao(jogo.estado_atual, acao)
                if novo_estado is not False:
                    novo_no = NoArvoreDeBusca(novo_estado, no_atual, acao)
                    if not self.esta_na(explorado, novo_no.estado) or not self.esta_na(borda, novo_no.estado):
                        # retorna o estado atual se ele for igual ao objetivo
                        if jogo.teste_de_objetivo(novo_no.estado):
                            return novo_no
                        borda.append(novo_no)

    def busca_bidirecional(self, problema):
        pass
