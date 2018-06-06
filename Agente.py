# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca


class Agente:
    borda_amplitude_1 = None
    borda_amplitude_2 = None

    def __init__(self):
        pass

    @staticmethod
    def esta_na_borda(lista, estado):
        for item in lista:
            if item.estado == estado:
                return True

        return False

    @staticmethod
    def esta_explorado(lista, estado):
        for item in lista:
            if item == estado:
                return True

        return False

    #
    # Busca em amplitude
    #
    def busca_em_amplitude(self, problema):
        no_raiz = NoArvoreDeBusca(problema.estado_inicial, None, None)
        borda = []
        explorado = set()
        borda.insert(0, no_raiz)

        # retorna o estado atual se ele for igual ao objetivo
        if problema.teste_de_objetivo(no_raiz.estado):
            return no_raiz

        while True:
            if len(borda) == 0:
                return -1
            # seleciona e deleta o primeiro elemento da borda
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

    def busca_bidirecional(self, problema):
        pass
