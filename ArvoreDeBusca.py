class NoArvoreDeBusca:
    estado = None
    pai = None
    acao = None

    def __init__(self, estado, pai, acao):
        self.estado = estado
        self.pai = pai
        self.acao = acao
