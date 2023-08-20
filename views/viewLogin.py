from tkinter import *
from PIL import Image, ImageTk
import sys
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controllers.controller import Controller

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.controller = Controller(self)  

        self.root.title("Sistemas Operacionais")
        self.root.geometry("300x400")
        self.root.resizable(False,False)
        self.container =tk.Frame(self.root)
        self.container.pack()

        self.telaLogin()
        self.telaLogin.grid(row=0,column=0,sticky="nswe")

        self.telaRegistro()
        self.telaRegistro.grid(row=0,column=0,sticky="nswe")

        self.telaSistema()
        self.telaSistema.grid(row=0,column=0,sticky="nswe")

        self.exibiTelaInicio()

        self.root.mainloop()
    
    def exibiTelaInicio(self):
        self.telaLogin.tkraise()

    def telaLogin(self):
        self.telaLogin =tk.Frame(self.container)

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
        self.button_entrar.configure(fg="White",bg="#55ACEE", width=14)   # PAD TAMANHO DE DENTRO 
        self.button_entrar.grid(row=6,pady=40)

        #ACESSO AO REGISTRO
        self.button_registrar = Button(self.telaLogin,text="Registrar-se",border=0, font=("Arial",12,"bold"), command=self.exibiTelaRegistro)
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
        self.button_voltar = Button(self.frameBotoes, text="Voltar", font=("Arial",11,"bold"),width=10,command=self.exibiTelaInicio)
        self.button_voltar.configure(fg="White",bg="#9ed1f7")  
        self.button_voltar.grid(row=0,column=0)

        # BOTÃO CADASTRAR
        self.button_cadastrar = Button(self.frameBotoes, text="Cadastrar", font=("Arial",11,"bold"),width=10, command=self.cadastrar)
        self.button_cadastrar.configure(fg="White",bg="#55ACEE")
        self.button_cadastrar.grid(row=0,column=1,padx=5)

    def telaSistema(self):
        self.telaSistema = tk.Frame(self.container)

    def close(self, evento=None):
        sys.exit()

    def verificarLogin(self):
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get()
        self.controller.verificarLogin(usuario, senha)

    def exibiTelaRegistro(self):
        self.telaRegistro.tkraise()

    def exibiTelaSistema(self):
        self.telaSistema.tkraise()

    def cadastrar(self):
        self.controller.cadastrarUsuario(self.entry_nomeUsuario.get(),self.entry_novaSenha.get(),self.entry_confirmarSenha.get())

    def exibirMensagem(self, mensagem):
        messagebox.showinfo("Sistemas Operacionais", mensagem)

View()