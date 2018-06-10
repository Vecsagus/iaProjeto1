# coding=utf-8
from ArvoreDeBusca import NoArvoreDeBusca

class Busca:
    def __init__(self, raiz):
        self.borda = [raiz]
        self.ids_borda = set()
        self.explorado = set()

    def adiciona_na_borda(self, no):
        no_id = self.gera_id_de_estado(no.estado)
        if (no_id not in self.ids_borda) and (no_id not in self.explorado):
            self.borda.append(no)
            self.ids_borda.add(no_id)
        else:
            return False

    def foi_explorado(self, estado):
        no_id = self.gera_id_de_estado(estado)
        self.explorado.add(no_id)

    def gera_id_de_estado(self, estado):
        return "".join(["".join([str(letra) for letra in linha]) for linha in estado])

    def acha_no_por_id(self, estado):
        for no in self.borda:
            if no.estado == estado:
                return no
            else:
                return False

'''
Dado um nó 'no', explora recursivamente seus nós antecessores e em cada nó sua ação é lida e armazenada uma lista.
O parâmetro início deve ser True somente na primeira chamada da função, nunca na chamada recursiva.
'''
def solucao(no, inicio = True):
    # verifica se o nó atual é o primeiro da lista
    if inicio:
        # inicia uma lista vazia para armazenar as ações
        acoes_solucao = []
    # verifica se o nó atual não tem um pai (é o nó raiz)
    if not no.pai:
        # adiciona a ação do nó raiz à lista de ações
        acoes_solucao += [no.acao]
        # retorna para os nós filhos uma a lista contendo a primeira ação
        return acoes_solucao
    # faz chamada recursiva para os nós antecessores
    acoes_solucao += solucao(no.pai, False)

'''
Dados 2 nós que contêm o mesmo estado, encontra a solução de ambos e as concatena.
'''
def solucao_bidirecional(no_indo, no_vindo):
    # verifica se os nós contêm o mesmo estado
    if no_indo.estado != no_vindo.estado:
        # retorna falha
        return -1
    # encontra a lista de soluções vindo e inverte a lista.
    solucoes_vindo = solucao(no_vindo)[::-1] 
    # retira o primeiro elemento, que é igual ao último da solução indo.
    del solucoes_vindo[0]
    # encontra a lista de soluções indo e concatena com as soluções vindo.
    solucao = solucao(no_indo) + solucoes_vindo
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
    no_atual = busca.borda[0]
    del busca.borda[0]
    # adiciona nó ao conjunto de nós explorados
    busca.foi_explorado(no_atual.estado)
    print("    estado slecionado:")
    print("    " + no_atual.estado)
    
    for acao in problema.get_opcoes_possiveis():
        novo_estado = problema.transicao(no_atual.estado, acao)
        # verifica se a ação gerou um novo estado
        if novo_estado:
            # cria um no na arvore para o novo estado
            filho = NoArvoreDeBusca(novo_estado, no_atual, acao)
            # adiciona nó na borda
            busca.adiciona_na_borda(filho)
            '''
            # cria identificador para o novo estado
            # novo_estado_id = "".join(["".join([str(letra) for letra in linha]) for linha in novo_estado])
            # verifica se o novo estado nao esta na lista de estados busca.explorados
            
            if (novo_estado_id not in busca.explorado) and (filho not in busca.borda):
                busca.borda.append(filho)
                print("    estados filhos:")
                print("    " + novo_estado_id)
            '''
    return busca.borda


def busca_bidirecional(problema):
    if problema.estado_inicial == problema.estado_objetivo:
        return problema.estado_objetivo
    print("Estado inicial:")
    print(problema.estado_inicial)
    raiz_da_busca_indo = NoArvoreDeBusca(problema.estado_inicial, None, None)
    raiz_da_busca_vindo = NoArvoreDeBusca(problema.estado_objetivo, None, None)
    busca_indo = Busca(raiz_da_busca_indo)
    busca_vindo = Busca(raiz_da_busca_vindo)
    
    while True:
        print("Busca indo: ")
        print("    " + str(busca_indo.borda[0].estado))
        borda_indo = expande_em_largura(problema, busca_indo)
        print('Explorados indo: ' + str(len(busca_indo.explorado)))
        print("Busca vindo: ")
        print("    " + str(busca_vindo.borda[0].estado))
        borda_vindo = expande_em_largura(problema, busca_vindo)
        print('Explorados vindo: ' + str(len(busca_vindo.explorado)))
        if (not borda_indo) or (not borda_vindo):
            return -1

        '''
        Irei refazer essa comparação de bordas, modificando a lista da borda da busca para que cada elemento contenha não só o nó, mas também o ID do estado.
        Dessa forma, será possível relacionar dois nós diferentes (em bordas diferentes e com pais diferentes), mas que contêm o mesmo estado
        '''
        for noI in borda_indo:
            if noI.estado in [noV.estado for noV in borda]:
                return solucao_bidirecional(noV,
        '''
        for noI in zip(borda_indo, borda_vindo):
            if noV.estado == noI.estado:
                return solucao_bidirecional(noV, noI)
        '''


    
