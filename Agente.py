# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca


class Agente:
    borda_amplitude_1 = None
    borda_amplitude_2 = None

    def __init__(self):
        pass

    #
    # Busca em amplitude
    #
    def busca_em_amplitude(self, problema):
        no_raiz = NoArvoreDeBusca(problema.estado_inicial, None, None)
        borda = []
        explorado = set()
        borda.append(borda)

        # retorna o estado atual se ele for igual ao objetivo
        if problema.teste_de_objetivo(no_raiz.estado):
            return no_raiz

        while True:
            if len(borda) == 0:
                return -1
            # seleciona o primeiro item da fila
            no_atual = borda[0]
            del borda[0]
            # cria string identificadora do estado
            estado_id = "".join(["".join([str(letra) for letra in linha]) for linha in no_atual.estado])
            # adiciona identificador de estado aos explorados
            explorado.add(estado_id)
            print("Qty Explorados ->" + str(len(explorado)))
            for acao in problema.get_opcoes_possiveis():
                novo_estado = problema.transicao(no_atual.estado, acao)
                # verifica se a ação gerou um novo estado
                if novo_estado:
                    # cria um no na arvore para o novo estado
                    filho = NoArvoreDeBusca(novo_estado, no_atual, acao)
                    # cria identificador para o novo estado
                    novo_estado_id = "".join(["".join([str(letra) for letra in linha]) for linha in novo_estado])
                    # verifica se o novo estado nao esta na lista de estados explorados
                    if (novo_estado_id not in explorado) and (filho not in borda):
                        # retorna o estado atual se ele for igual ao objetivo
                        if problema.teste_de_objetivo(filho.estado):
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
