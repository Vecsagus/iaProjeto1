import threading


class ThreadAmplitudeReversa(threading.Thread):
    def __init__(self, threadID, agente, problema):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.agente = agente
        self.problema = problema
        self._stopevent = threading.Event()

    def run(self):
        print("Iniciando Thread de Amplitude Reversa")
        resultado = self.agente.busca_em_amplitude_reversa(self.problema)
        print("End Thread de Interativa")
        return resultado
