# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca
from ThreadAmplitude import ThreadAmplitude
from ThreadAmplitudeReversa import ThreadAmplitudeReversa


class Agente:
    borda_amplitude_1 = []
    borda_amplitude_2 = []
    estado_atual = None

    def __init__(self):
        pass

    def get_borda_amplitude(self):
        return self.borda_amplitude_1

    def get_borda_amplitude2(self):
        return self.borda_amplitude_2

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

            if (self.get_borda_amplitude() == self.get_borda_amplitude2()) \
                    and (len(self.get_borda_amplitude()) > 0 and len(self.get_borda_amplitude2()) > 0):
                return self.estado_atual

            if len(borda) == 0:
                return -1
            # seleciona o primeiro item da fila
            no_atual = borda[0]
            del borda[0]
            # cria string identificadora do estado
            estado_id = "".join(["".join([str(letra) for letra in linha]) for linha in no_atual.estado])
            # adiciona identificador de estado aos explorados
            explorado.add(estado_id)
            print("Qty Explorados Thread normaly ->" + str(len(explorado)))
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
                        self.estado_atual = filho
                        borda.append(filho)

        #
        # Busca em amplitude
        #

    def busca_em_amplitude_reversa(self, problema):
        no_raiz = NoArvoreDeBusca(problema.estado_inicial, None, None)
        borda = []
        explorado = set()
        borda.append(no_raiz)

        while True:
            if (self.get_borda_amplitude() == self.get_borda_amplitude2()) \
                    and (len(self.get_borda_amplitude()) > 0 and len(self.get_borda_amplitude2()) > 0):
                return self.estado_atual

            if len(borda) == 0:
                return -1
            # seleciona o primeiro item da fila
            no_atual = borda[0]
            del borda[0]
            # cria string identificadora do estado
            estado_id = "".join(["".join([str(letra) for letra in linha]) for linha in no_atual.estado])
            # adiciona identificador de estado aos explorados
            explorado.add(estado_id)
            print("Qty Explorados Thread Reversa ->" + str(len(explorado)))
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
                        self.borda_amplitude_2.append(filho)
                        self.estado_atual = filho
                        borda.append(filho)

    #
    # Busca Bi-Direcional
    #
    def busca_bidirecional(self, problema_do_inicio, problema_do_final):

        threads = []

        thread1 = ThreadAmplitude(1, self, problema_do_inicio)
        thread2 = ThreadAmplitudeReversa(2, self, problema_do_final)

        try:
            thread1.start()
            thread2.start()
            threads.append(thread1)
            threads.append(thread2)

            for t in threads:
                t.join()

        except Exception as ex:
            print(ex.message)
            return self.estado_atual
