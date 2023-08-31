from models.modelUser import ModelUser

class ControllerUser:
    def __init__(self, view):
        self.modelUser = ModelUser()
        self.view = view

    def cadastrarUsuario(self, nome, senha, confirmacaoSenha):
        usuario = self.modelUser.cadastrarUsuario(nome, senha, confirmacaoSenha)
        if usuario == "senhas_distintas":
            self.view.exibirMensagem("Senhas não confirmam, tente novamente!")
        elif usuario == "usuario_ja_cadastrado":
            self.view.exibirMensagem("Usuário já cadastrado, tente novamente!")
        else:
            self.view.exibirMensagem("Usuário cadastrado com sucesso!")
            self.view.exibeTelaInicio()

    def verificarLogin(self, usuario, senha):
        loginValido = self.modelUser.verificarLogin(usuario, senha)
        if loginValido == True:
            self.view.exibeTelaGerenciamento()
        else:
            self.view.exibirMensagem("Usuário ou senha inválidos, tente novamente!")