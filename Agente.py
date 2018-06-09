# coding=utf-8
class Busca:
    def __init__(self, raiz):
        self.borda = [raiz]
        self.explorado = set('''adicionar ideintificador do estado inicial da raiz''')

def solucao(no, inicio = True):
    if inicio:
        acoes_solucao = []
    if not no.pai:
        acoes_solucao = [no.acao]
        return acoes_solucao
    acoes_solucao += solucao(no.pai, False)

def solucao_bidirecional(no_indo, no_vindo):
    if no_indo.estado != no_vindo.estado:
        return -1
    segunda_metade = solucao(no_vindo, None)[::-1]
    del segunda_metade[0]
    solucao = solucao(no_indo, None) + segunda_metade
    return solucao
    
# Transformar essa funcao em metodo da classe QuebraCabeca
def expande(problema, busca):
    if len(busca.borda) == 0:
        return -1
    no_atual = busca.borda[0]
    del busca.borda[0]
    # gera identificador do estado
    estado_id = "".join(["".join([str(letra) for letra in linha]) for linha in no_atual.estado])
    # adiciona identificador de estado aos busca.explorados
    busca.explorado.add(estado_id)
    
    for acao in problema.get_opcoes_possiveis():
        novo_estado = problema.transicao(no.estado, acao)
        # verifica se a ação gerou um novo estado
        if novo_estado:
            # cria um no na arvore para o novo estado
            filho = NoArvoreDeBusca(novo_estado, no_atual, acao)
            # cria identificador para o novo estado
            novo_estado_id = "".join(["".join([str(letra) for letra in linha]) for linha in novo_estado])
            # verifica se o novo estado nao esta na lista de estados busca.explorados
            if (novo_estado_id not in busca.explorado) and (filho not in busca.borda):
                busca.borda.append(filho)
                return busca.borda

def busca_bidirecional(problema):
    if problema.estado_inicial == problema.estado_objetivo:
        return problema.estado_objetivo
    raiz_da_busca_indo = NoArvoreDeBusca(problema.estado_inicial, None, None)
    raiz_da_busca_vindo = NoArvoreDeBusca(problema.estado_objetivo, None, None)
    busca_indo = Busca(raiz_da_busca_indo)
    busca_vindo = Busca(raiz_da_busca_vindo)

    
    while True:
        borda_indo = expande(problema, busca_indo)
        borda_vindo = expande(problema, busca_vindo)
        if (not borda_indo) or (not borda_vindo):
            return -1
        for noV, noI in zip(borda_indo, borda_vindo):
            if noV.estado == noI.estado:
                return solucao_bidirecional(noV, noI)



    
