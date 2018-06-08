# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca


class Agente:
    borda_amplitude_1 = []
    borda_amplitude_2 = []
    borda_interativa_1 = []

    def __init__(self):
        pass

    #
    # Busca em amplitude
    #
    def busca_em_amplitude(self, problema):
        no_raiz = NoArvoreDeBusca(problema.estado_inicial, None, None)
        borda = []
        explorado = set()
        borda.append(no_raiz)

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
                        self.borda_amplitude_1.append(filho)
                        borda.append(filho)

    def busca_de_aprofundamento_iterativo(self, problema):
        cont = 1
        while True:
            print(cont)
            resultado = self.busca_em_profundidade_limitada(problema, cont)
            cont += 1
            if resultado != 'corte':
                return resultado

    #
    # Busca em profundidade limitada
    #
    def busca_em_profundidade_limitada(self, problema, limite):
        return self.bpl_recursiva(NoArvoreDeBusca(problema.estado_inicial, None, None), problema, limite)

    def bpl_recursiva(self, no, problema, limite):
        if problema.teste_de_objetivo(no.estado):
            return no
        elif limite == 0:
            return 'corte'
        else:
            teve_corte = False
            for acao in problema.get_opcoes_possiveis():
                novo_estado = problema.transicao(no.estado, acao)
                if novo_estado:
                    filho = NoArvoreDeBusca(novo_estado, no, acao)
                    if filho not in self.borda_interativa_1:
                        self.borda_interativa_1.append(filho)

                    resultado = self.bpl_recursiva(filho, problema, limite - 1)
                    if resultado == 'corte':
                        teve_corte = True
                    elif resultado != -1:
                        return resultado

            if teve_corte:
                return 'corte'
            else:
                return -1

    def busca_bidirecional(self, problema_do_inicio, problema_do_final):
        self.busca_em_amplitude(problema_do_inicio)
        resultado = self.busca_de_aprofundamento_iterativo(problema_do_final)

        if self.borda_interativa_1 == self.borda_amplitude_1:
            return resultado
