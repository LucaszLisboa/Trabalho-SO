from tkinter import *
from PIL import Image, ImageTk
import sys
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controllers.controllerUser import ControllerUser
from controllers.controllerProcessos import ControllerProcessos

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.controller = ControllerUser(self)  
        self.controllerProcessos = ControllerProcessos(self)

        self.root.title("Sistemas Operacionais")
        self.root.geometry("1000x680")
        self.root.resizable(False,False)
        self.container =tk.Frame(self.root)
        self.container.pack()

        self.telaLogin()
        self.telaLogin.grid(row=0,column=0,sticky="nswe")

        self.telaRegistro()
        self.telaRegistro.grid(row=0,column=0,sticky="nswe")

        self.telaGerenciamento()
        self.telaGerenciamento.grid(row=0,column=0,sticky="nswe")

        self.telaCadastroProcessos()
        self.telaCadastroProcessos.grid(row=0,column=0,sticky="nswe")

        self.exibeTelaInicio()

        self.root.mainloop()
    
    def exibeTelaInicio(self):
        self.entry_usuario.delete(0, 'end')
        self.entry_senha.delete(0, 'end')
        self.telaLogin.tkraise()

    def telaLogin(self):
        self.telaLogin =tk.Frame(self.container)

        self.espacoBranco = tk.Frame(self.telaLogin, height=60)
        self.espacoBranco.grid(row=0)

        self.label_titulo = Label(self.telaLogin,text="Sistemas\nOperacionais", font=("Arial",26),padx=30,pady=15,anchor="center",fg="#000000")
        self.label_titulo.grid(row=1)

        # NOME DO USUARIO
        self.label_usuario = Label(self.telaLogin, text="Usuario", font=("Arial",12,"bold"),padx=50)
        self.label_usuario.grid(row=2,sticky="w")
        self.entry_usuario = Entry(self.telaLogin,font= 11, width=20,highlightbackground="#000000",highlightthickness=0.5)
        self.entry_usuario.grid(row=3,padx=50,pady=2)

        # SENHA DO USUARIO
        self.label_senha = Label(self.telaLogin, text="Senha", font=("Arial",12,"bold"),padx=50)
        self.label_senha.grid(row=4,sticky="w")
        self.entry_senha = Entry(self.telaLogin, width=20,font= 11,highlightbackground="#000000",highlightthickness=0.5,show="•")
        self.entry_senha.grid(row=5,padx=50,pady=2)

        # BOTÃO ENTRAR
        self.button_entrar = Button(self.telaLogin, text="ENTRAR", font=("Arial",12,"bold"),compound="center", command=self.verificarLogin)
        self.button_entrar.configure(fg="White",bg="#3f9eeb", width=14)   # PAD TAMANHO DE DENTRO 
        self.button_entrar.grid(row=6,pady=40)

        #ACESSO AO REGISTRO
        self.button_registrar = Button(self.telaLogin,text="Registrar-se",border=0, font=("Arial",12,"bold"), command=self.exibeTelaRegistro)
        self.button_registrar.grid(row=7)

        self.root.bind('<Escape>', self.close)

    def telaRegistro(self):
        self.telaRegistro = tk.Frame(self.container)

        self.espacoBranco = tk.Frame(self.telaRegistro, height=60)
        self.espacoBranco.grid(row=0)

        # NOME DO USUARIO
        self.label_nomeUsuario = Label(self.telaRegistro, text="Nome do Usuario:", font=("Arial",12,"bold"),padx=50)
        self.label_nomeUsuario.grid(row=1,sticky="w")
        self.entry_nomeUsuario = Entry(self.telaRegistro, width=20,highlightthickness=0.5, highlightbackground="black",font=12)
        self.entry_nomeUsuario.grid(row=2,padx=50,pady=5)

        # NOVA SENHA  
        self.label_novaSenha = Label(self.telaRegistro, text="Nova Senha:", font=("Arial",12,"bold"),padx=50)
        self.label_novaSenha.grid(row=4,sticky="w")
        self.entry_novaSenha = Entry(self.telaRegistro, width=20,highlightthickness=0.5,highlightbackground="black", font=10, show="•")
        self.entry_novaSenha.grid(row=5, padx=50,pady=5)

        # CONFIRMAÇÃO DA NOVA SENHA
        self.label_confirmarSenha = Label(self.telaRegistro, text="Confirmar Senha:", font=("Arial",12,"bold"),padx=50)
        self.label_confirmarSenha.grid(row=6,sticky="w")
        self.entry_confirmarSenha = Entry(self.telaRegistro,highlightthickness=0.5,font=10, highlightbackground="black", show="•")
        self.entry_confirmarSenha.grid(row=7,padx=50,pady=5)

        self.frameBotoes = tk.Frame(self.telaRegistro)
        self.frameBotoes.grid(row=8,column=0,columnspan=2, pady=30)

        # BOTÃO VOLTAR
        self.button_voltar = Button(self.frameBotoes, text="Voltar", font=("Arial",11,"bold"),width=10,command=self.exibeTelaInicio)
        self.button_voltar.configure(fg="White",bg="#9c9c9c")  
        self.button_voltar.grid(row=0,column=0)

        # BOTÃO CADASTRAR
        self.button_cadastrar = Button(self.frameBotoes, text="Cadastrar", font=("Arial",11,"bold"),width=10, command=self.cadastrar)
        self.button_cadastrar.configure(fg="White",bg="#3f9eeb")
        self.button_cadastrar.grid(row=0,column=1,padx=5)

    def telaGerenciamento(self):
        self.telaGerenciamento = tk.Frame(self.container)

        menubar = tk.Menu(self.telaGerenciamento)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Inicio", menu=filemenu)
        filemenu.add_command(label="Processos", command=self.exibeTelaGerenciamento)
        filemenu.add_command(label="Criar Processo", command=self.exibeTelaCadastroProcessos)
        filemenu.add_command(label="Sair", command=self.exibeTelaInicio)
        self.root.config(menu=menubar)

        # define columns
        columns = ('nome', 'pid', 'status', 'nome_de_usuario', 'prioridade', 'cpu', 'espaco_memoria')

        self.tabela = ttk.Treeview(self.telaGerenciamento, columns=columns, show='headings', height=30, selectmode=tk.BROWSE)

        # define headings
        self.tabela.heading('nome', text='Nome')
        self.tabela.heading('pid', text='PID')
        self.tabela.column('pid', width=120)
        self.tabela.heading('status', text='Status')
        self.tabela.column('status', width=120)
        self.tabela.heading('nome_de_usuario', text='Nome de usuário')
        self.tabela.heading('prioridade', text= 'Prioridade')
        self.tabela.column('prioridade', width=120)
        self.tabela.heading('cpu', text='CPU')
        self.tabela.column('cpu', width=120)    
        self.tabela.heading('espaco_memoria', text='Espaço memória')
        self.tabela.column('espaco_memoria', width=120)
        self.tabela.bind('<<TreeviewSelect>>')
        self.tabela.grid()

        self.popularTabela()
        buttonEditarProcesso = ttk.Button(self.telaGerenciamento, text='Editar', command=self.editarProcesso)
        buttonEditarProcesso.grid()

        buttonDeleteProcesso = ttk.Button(self.telaGerenciamento, text='Excluir', command=self.deletarProcesso)
        buttonDeleteProcesso.grid()


    def telaCadastroProcessos(self):
        self.telaCadastroProcessos = tk.Frame(self.container)

        label_nomeProcesso = Label(self.telaCadastroProcessos, text="Nome do Processo:", font=("Arial",10),padx=50)
        label_nomeProcesso.grid(row=1,sticky="w")
        self.entry_nomeProcesso = Entry(self.telaCadastroProcessos, width=20,highlightthickness=0.5, highlightbackground="black",font=8)
        self.entry_nomeProcesso.grid(row=2,padx=50,pady=5)

        label_pid = Label(self.telaCadastroProcessos, text="PID:", font=("Arial",10),padx=50)
        label_pid.grid(row=3, sticky="w")
        self.entry_pid = Entry(self.telaCadastroProcessos, width=20,highlightthickness=0.5, highlightbackground="black",font=8)
        self.entry_pid.grid(row=4, padx=50, pady=5)

        label_nomeUsuarioUID = Label(self.telaCadastroProcessos, text="Nome do Usuário (UID):", font=("Arial",10),padx=50)
        label_nomeUsuarioUID.grid(row=5, sticky="w")
        self.entry_nomeUsuarioUID = Entry(self.telaCadastroProcessos, width=20,highlightthickness=0.5, highlightbackground="black",font=8)
        self.entry_nomeUsuarioUID.grid(row=6, padx=50, pady=5)

        label_prioridade = Label(self.telaCadastroProcessos, text="Prioridade:", font=("Arial",10),padx=50)
        label_prioridade.grid(row=7, sticky="w")
        prioridades = ["Alta", "Média", "Comum"]
        self.select_prioridade = ttk.Combobox(self.telaCadastroProcessos, values=prioridades, width=27, state= 'readonly')
        self.select_prioridade.grid(row=8, padx=50, pady=5)

        label_usoCPU = Label(self.telaCadastroProcessos, text="Uso da CPU(%):",  font=("Arial",10),padx=50)
        label_usoCPU.grid(row=9, sticky="w")
        self.entry_usoCPU = Entry(self.telaCadastroProcessos, width=20,highlightthickness=0.5, highlightbackground="black",font=8)
        self.entry_usoCPU.grid(row=10, padx=50, pady=5)

        label_estado = Label(self.telaCadastroProcessos, text="Estado:",  font=("Arial",10),padx=50)
        label_estado.grid(row=11, sticky="w")
        estados = ["Pronto", "Execução", "Espera"]
        self.select_estado = ttk.Combobox(self.telaCadastroProcessos, values=estados, width=27, state= 'readonly')
        self.select_estado.grid(row=12, padx=50, pady=5)

        label_espacoMemoria = Label(self.telaCadastroProcessos, text="Espaço de Memória (MB):", font=("Arial",10),padx=50)
        label_espacoMemoria.grid(row=13, sticky="w")
        self.entry_espacoMemoria = Entry(self.telaCadastroProcessos, width=20,highlightthickness=0.5, highlightbackground="black",font=8)
        self.entry_espacoMemoria.grid(row=14, padx=50, pady=5)

        # BOTÃO CADASTRAR
        button_cadastrarProcesso = Button(self.telaCadastroProcessos, text="Cadastrar", font=("Arial",11,"bold"),width=10, command=self.cadastrarProcesso)
        button_cadastrarProcesso.configure(fg="White",bg="#55ACEE")
        button_cadastrarProcesso.grid(row=15,padx=5, pady=15)

    def close(self, evento=None):
        sys.exit()

    def verificarLogin(self):
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get()
        self.controller.verificarLogin(usuario, senha)

    def exibeTelaRegistro(self):
        self.telaRegistro.tkraise()

    def exibeTelaCadastroProcessos(self):
        self.limparCamposCadastroProcesso()
        self.telaCadastroProcessos.tkraise()

    def exibeTelaGerenciamento(self):
        self.popularTabela()
        self.telaGerenciamento.tkraise()

    def cadastrar(self):
        usuario = self.entry_nomeUsuario.get().strip()
        senha = self.entry_novaSenha.get()
        confirmacaoSenha = self.entry_confirmarSenha.get()
        self.controller.cadastrarUsuario(usuario, senha, confirmacaoSenha)

    def cadastrarProcesso(self):
        nomeProcesso = self.entry_nomeProcesso.get().strip()
        pid = self.entry_pid.get().strip()
        nomeUsuarioUID = self.entry_nomeUsuarioUID.get().strip()
        prioridade = self.select_prioridade.get()
        usoCPU = self.entry_usoCPU.get().strip()
        estado = self.select_estado.get()
        espacoMemoria = self.entry_espacoMemoria.get().strip()
        self.controllerProcessos.cadastrarProcesso(nomeProcesso, pid, nomeUsuarioUID, prioridade, usoCPU, estado, espacoMemoria)
        self.limparCamposCadastroProcesso()

    def popularTabela(self):
        self.tabela.delete(*self.tabela.get_children())
        processos = self.controllerProcessos.consultarProcessos()
        for processo in processos:
            nomeProcesso = processo['nomeProcesso']
            PID = processo['pid']
            status = processo['estado']
            nomeUsuarioUID = processo['nomeUsuarioUID']
            prioridade = processo['prioridade']
            usoCPU = processo['usoCPU']
            espacoMemoria = processo['espacoMemoria']
            self.tabela.insert("", "end", values=(nomeProcesso, PID, status, nomeUsuarioUID, prioridade, usoCPU, espacoMemoria))

    def deletarProcesso(self):
        selecionado = self.tabela.focus()
        detalhesProcesso = self.tabela.item(selecionado)
        pid = detalhesProcesso.get('values')[1]
        self.controllerProcessos.deletarProcesso(pid)

    def editarProcesso(self):
        selecionado = self.tabela.focus()
        detalhesProcesso = self.tabela.item(selecionado)
        processo = detalhesProcesso.get('values')
        self.controllerProcessos.editarProcesso(processo)

    def limparCamposCadastroProcesso(self):
        self.entry_nomeProcesso.delete(0, 'end')
        self.entry_pid.delete(0, 'end')
        self.entry_nomeUsuarioUID.delete(0, 'end')
        self.select_prioridade.set('')
        self.entry_usoCPU.delete(0, 'end')
        self.select_estado.set('')
        self.entry_espacoMemoria.delete(0, 'end')

    def exibirMensagem(self, mensagem):
        messagebox.showinfo("Sistemas Operacionais", mensagem)

    def popularEdicaoProcesso(self, processo):
        self.exibeTelaCadastroProcessos()
        self.entry_nomeProcesso.insert(0, processo[0])
        self.entry_pid.insert(0, processo[1])
        self.entry_nomeUsuarioUID.insert(0, processo[3])
        self.select_prioridade.set(processo[4])
        self.entry_usoCPU.insert(0, processo[5])
        self.select_estado.set(processo[2])
        self.entry_espacoMemoria.insert(0, processo[6])



View()