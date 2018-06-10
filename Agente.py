# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca

class Busca:
    def __init__(self, raiz):
        self.borda = [[raiz, self.gera_id_de_estado(raiz.estado)]]
        self.explorado = set()

    def adiciona_na_borda(self, no):
        no_id = self.gera_id_de_estado(no.estado)
        if (no_id not in [item[1] for item in self.borda]) and (no_id not in self.explorado):
            self.borda.append([no, no_id])
            return True
        else:
            return False

    def foi_explorado(self, estado):
        no_id = self.gera_id_de_estado(estado)
        self.explorado.add(no_id)

    def gera_id_de_estado(self, estado):
        return int("".join(["".join([str(letra) for letra in linha]) for linha in estado]))

    def acha_no_por_id(self, identificador):
        for item in self.borda:
            if item[1] == identificador:
                return item[0]
        return False
'''
Dado um nó 'no', explora recursivamente seus nós antecessores e em cada nó sua ação é lida e armazenada uma lista.
O parâmetro início deve ser True somente na primeira chamada da função, nunca na chamada recursiva.
'''
def solucao(no, acoes =[]):
    # verifica se o nó atual não tem um pai (é o nó raiz)
    if not no.pai:
        # adiciona a ação do nó raiz à lista de ações
        acoes += [no.acao]
        # retorna para os nós filhos uma a lista contendo a primeira ação
        return acoes_solucao
    # faz chamada recursiva para os nós antecessores
    acoes_solucao += acoes
    solucao(no.pai, acoes_solucao)

'''
Dados 2 nós que contêm o mesmo estado, encontra a solução de ambos e as concatena.
'''
def solucao_bidirecional(no_indo, no_vindo):
    # verifica se os nós contêm o mesmo estado
    if no_indo.estado != no_vindo.estado:
        # retorna falha
        return -1
    # encontra a lista de soluções vindo e inverte a lista.
    solucoes_vindo = []
    solucao(no_vindo, solucoes_vindo)[::-1] 
    # retira o primeiro elemento, que é igual ao último da solução indo.
    del solucoes_vindo[0]
    # encontra a lista de soluções indo e concatena com as soluções vindo.
    solucao = []
    solucao_indo = []
    solucao(no_indo, solucao_indo)
    solucao = solucao_indo + solucoes_vindo
    # retorna a lista de ações que formam a solução da busca bidirecional
    return solucao
    
# Transformar essa funcao em metodo da classe QuebraCabeca
'''
Dados um problema e uma busca contendo borda e conjunto de explorados, 
retira o primeiro nó na borda da busca e cria nós filhos para ele a partir das ações do problema.
Retorna borda com os novos nós.
'''
def expande_em_largura(problema, busca):
    if len(busca.borda) == 0:
        return -1
    no_atual = busca.borda[0][0]
    del busca.borda[0]
    # adiciona nó ao conjunto de nós explorados
    busca.foi_explorado(no_atual.estado)
    
    #print("    Estados filhos:")
    for acao in problema.get_opcoes_possiveis():
        novo_estado = problema.transicao(no_atual.estado, acao)
        # verifica se a ação gerou um novo estado
        if novo_estado:
            # cria um no na arvore para o novo estado
            filho = NoArvoreDeBusca(novo_estado, no_atual, acao)
            # adiciona nó na borda
            '''if '''
            busca.adiciona_na_borda(filho)
                #print("        " + str(novo_estado))
    return busca.borda

def busca_bidirecional(problema):
    if problema.estado_inicial == problema.estado_objetivo:
        return problema.estado_objetivo
    #print("Estado inicial:")
    #print(problema.estado_inicial)
    raiz_da_busca_indo = NoArvoreDeBusca(problema.estado_inicial, None, None)
    raiz_da_busca_vindo = NoArvoreDeBusca(problema.estado_objetivo, None, None)
    busca_indo = Busca(raiz_da_busca_indo)
    busca_vindo = Busca(raiz_da_busca_vindo)
    
    while True:
        #print("Busca indo: ")
        #print("    " + str(busca_indo.borda[0][0].estado))
        borda_indo = expande_em_largura(problema, busca_indo)
        print("    Explorados indo: " + str(len(busca_indo.explorado)))
        #print("Busca vindo: ")
        #print("    " + str(busca_vindo.borda[0][0].estado))
        borda_vindo = expande_em_largura(problema, busca_vindo)
        print("    Explorados vindo: " + str(len(busca_vindo.explorado)))
        if (not borda_indo) or (not borda_vindo):
            return -1

        for itemBI in borda_indo:
            if itemBI[1] in [itemBV[1] for itemBV in borda_vindo]:
                #print("Estado da intersecção de buscas: " + str(itemBI[0].estado))
                identificador = itemBI[1]
                noBI = busca_indo.acha_no_por_id(identificador)
                noBV = busca_vindo.acha_no_por_id(identificador)
                return solucao_bidirecional(noBV, noBI)
