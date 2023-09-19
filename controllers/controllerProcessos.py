from models.modelProcessos import ModelProcessos

class ControllerProcessos:
    def __init__(self, view):
        self.modelProcessos = ModelProcessos()
        self.view = view

    def cadastrarProcesso(self, nomeProcesso, pid, nomeUsuarioUID, prioridade, usoCPU, estado, espacoMemoria):
        processo = self.modelProcessos.cadastrarProcesso(nomeProcesso, pid, nomeUsuarioUID, prioridade, usoCPU, estado, espacoMemoria)
        if processo == 0:
            self.view.exibirMensagem("Preencha todos os campos!")
            return
        elif processo == 1:
            self.view.exibirMensagem("Processo atualizado com sucesso!")
        else:
            self.view.exibirMensagem("Processo cadastrado com sucesso!")
        self.view.exibeTelaGerenciamento()
        self.view.limparCamposCadastroProcesso()

    def consultarProcessos(self):
        processos = self.modelProcessos.consultarProcessos()
        return processos
    
    def deletarProcesso(self, pid):
        deleted_count = self.modelProcessos.deletarProcesso(pid)
        if(deleted_count == 1):
            self.view.exibirMensagem('Processo deletado com sucesso!')
            self.view.popularTabela()

    def editarProcesso(self, processo):
        if processo[1]:
            self.view.popularEdicaoProcesso(processo)
