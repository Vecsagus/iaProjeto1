import random

class ProblemaQuebraCabeca:
    def __init__(self, estado_inicial = self.gera_estado_inicial()):
        self.estado_objetivo = [[0,1,2],[3,4,5],[6,7,8]]
        self.estado_inicial = estado_inicial
        self.estado_atual = self.estado_inicial

    def gera_estado_inicial(self):
        estado_inicial = []
        pecas = [i for i in range(9)]
        random.shuffle(pecas)
        estado_inicial.append([pecas[0], pecas[1], pecas[2]])
        estado_inicial.append([pecas[3], pecas[4], pecas[5]])
        estado_inicial.append([pecas[6], pecas[7], pecas[8]])
        return estado_inicial
    
    def para_direita(self):
        for num, linha in self.estado_atual:
            for pos, peca in linha:
                if (peca == 0 and pos < 2):
                    (linha[num][pos], linha[num][pos+1]) = (linha[num][pos+1], linha[num][pos])
                    return True
                else:
                    return False

    def para_esquerda(self):
        for num, linha in self.estado_atual:
            for pos, peca in linha:
                if (peca == 0 and pos > 0):
                    (linha[num][pos], linha[num][pos-1]) = (linha[num][pos-1], linha[num][pos])
                    return True
                else:
                    return False
    
    def para_cima(self):
        for num, linha in self.estado_atual:
            for pos, peca in linha:
                if (peca == 0 and num < 2):
                    (linha[num][pos], linha[num+1][pos]) = (linha[num+1][pos], linha[num][pos])
                    return True
                else:
                    return False

    def para_baixo(self):
        for num, linha in self.estado_atual:
            for pos, peca in linha:
                if (peca == 0 and num > 0):
                    (linha[num][pos], linha[num-1][pos]) = (linha[num-1][pos], linha[num][pos])
                    return True
                else:
                    return False





