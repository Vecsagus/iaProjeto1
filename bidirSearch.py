import random
from enum import Enum

class ProblemaQuebraCabeca:
    def __init__(self, estado_inicial = self.__gera_estado_inicial()):
        self.estado_objetivo = [[0,1,2],[3,4,5],[6,7,8]]
        self.estado_inicial = estado_inicial
        self.estado_atual = self.estado_inicial
        self.acao = Enum('Acao', 'esquerda para_cima direita para_baixo')
        

    def __gera_estado_inicial(self):
        estado_inicial = []
        pecas = [i for i in range(9)]
        random.shuffle(pecas)
        estado_inicial.append([pecas[0], pecas[1], pecas[2]])
        estado_inicial.append([pecas[3], pecas[4], pecas[5]])
        estado_inicial.append([pecas[6], pecas[7], pecas[8]])
        return estado_inicial

    
    
    def transicao(self, estado, acao):
        for num, linha in estado:
            for pos, peca in linha:
                if (peca == 0):
                    if (acao == self.acao.esquerda and pos > 0):
                        (linha[num][pos], linha[num][pos-1]) = (linha[num][pos-1], linha[num][pos])
                    elif (acao == self.acao.para_cima and num < 2):
                        (linha[num][pos], linha[num+1][pos]) = (linha[num+1][pos], linha[num][pos])
                    elif (acao == self.acao.direita and pos < 2):
                        (linha[num][pos], linha[num][pos+1]) = (linha[num][pos+1], linha[num][pos])
                    elif (acao == self.acao.para_baixo and num > 0):
                        (linha[num][pos], linha[num-1][pos]) = (linha[num-1][pos], linha[num][pos])
                        pass
                    else:
                        return [-1, 'Acao invalida']

    def teste_de_objetivo(self, estado):
        return cmp(self.estado_objetivo, estado)

    def imprime(estado):
        for linha in estado:
            print("-------")
            for coluna in linha:
                print("|" + str(coluna), end="")
            print("|")
        print("-------")

class NoArvoreDeBusca:
    def __init__(self, estado, pai, acao):
        self.estado = estado
        self.pai = pai
        slef. acao = acao

def busca_em_amplitude(problema):
    explorado = set()
    borda = []
    no_raiz = NoArvoreDeBusca(problema.estado_inicial, None, None)
    borda.append(no_raiz)

    while(True):
        if not len(borda):
            return -1
        # seleciona e deleta o primeiro elemento da borda
        no_atual = borda[0]
        del borda[0]
        # retorna o estado atual se ele for igual ao objetivo
        return no_atual if cmp(no_atual.estado, problema.estado_objetivo) 
        # adiciona ao conjunto de nós explorados    
        explorado.add(no_atual)
        #### Expandir noh
        # move p/ esquerda
        trans_esquerda = problema.transicao(problema.acao.esquerda)
        borda.append(NoArvoreDeBusca(trans_esquerda, no_atual, problema.acao.esquerda)) if trans_esquerda[0] != -1) else None
        # move p/ para_cima
        trans_para_cima = problema.transicao(problema.acao.para_cima)
        borda.append(NoArvoreDeBusca(trans_para_cima, no_atual, problema.acao.para_cima)) if trans_para_cima[0] != -1) else None
        # move p/ direita
        trans_direita = problema.transicao(problema.acao.direita)
        borda.append(NoArvoreDeBusca(trans_direita, no_atual, problema.acao.direita)) if trans_direita[0] != -1) else None
        # move p/ para_baixo
        trans_para_baixo = problema.transicao(problema.acao.para_baixo)
        borda.append(NoArvoreDeBusca(trans_para_baixo, no_atual, problema.acao.para_baixo)) if trans_para_baixo[0] != -1) else None

def busca_bidirecional(problema):
    pass





