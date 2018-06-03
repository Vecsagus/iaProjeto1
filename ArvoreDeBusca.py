class NoArvoreDeBusca:
    def __init__(self, estado, pai, acao):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.prox = NoArvoreDeBusca
