from models.threadingProcessos import ThreadingProcessos

class ControllerThreading:
    def __init__(self, view):
        self.threading = ThreadingProcessos()
        self.view = view

    def iniciar_insercao_periodica_em_segundo_plano(self):
        self.threading.iniciar_insercao_periodica_em_segundo_plano()