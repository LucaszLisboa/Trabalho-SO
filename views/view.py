from tkinter import *
from PIL import Image, ImageTk
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class View:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x500")
        self.root.title("Sistemas Operacionais")
        self.root.resizable(False,False)
        self.root.configure(bg="")
        self.container =tk.Frame(self.root)
        self.container.pack()

        self.telaLogin()
        self.TelaLogin.grid(row=0,column=0,sticky="nswe")

        self.telaRegistrar()
        self.telaRegistrar.grid(row=0,column=0,sticky="nswe")

        self.inicio()
        self.root.mainloop()


    def inicio(self):
        self.TelaLogin.tkraise()
    

    def registro(self):
        self.telaRegistrar.tkraise()

        
    def telaLogin(self):

        self.TelaLogin =tk.Frame(self.container)
        #self.TelaLogin.geometry("300x550")
        #self.TelaLogin.title("Tela de Login")

        #TELA DE FUNDO
        # self.TelaLogin.configure(bg="white")

        # IMAGEM DA LOGO

        # self.image = Image.open("image\Imagem3.png")
        # photo = ImageTk.PhotoImage(self.image)
        # imagem_label = Label(self.TelaLogin, image=photo)
        # imagem_label.configure(bg="")
        # imagem_label.image= photo
        # imagem_label.grid(row=0,pady=25)

        #TITULO DO APP 

        self.titulo_label = Label(self.TelaLogin,text="Sistemas\nOperacionais", font=("Arial",30),padx=30,pady=15,anchor="center",fg="#644394")
        self.titulo_label.grid(row=1)

        # NOME DO USUARIO
        
        self.user_label = Label(self.TelaLogin, text="Usuario", font=("Arial",12,"bold"),padx=50)
        self.user_label.grid(row=2,sticky="w")

        self.user_label_entry = Entry(self.TelaLogin,font= 11, width=20,highlightbackground="#BD4AB5",highlightthickness=0.5)
        self.user_label_entry.grid(row=3,padx=50,pady=2)

        # SENHA DO USUARIO

        self.senha_label = Label(self.TelaLogin, text="Senha", font=("Arial",12,"bold"),padx=50)
        self.senha_label.grid(row=4,sticky="w")

        self.senha_label_entry = Entry(self.TelaLogin, width=20,font= 11,highlightbackground="#BD4AB5",highlightthickness=0.5,show="•")
        self.senha_label_entry.grid(row=5,padx=50,pady=2)

        # ESPAÇO VAZIO

        self.espaco =tk.Frame(self.TelaLogin,width=50,height=15,bg="")
        self.espaco.grid(row=6)

        # BOTÃO ENTRAR

        self.Btentrar = Button(self.TelaLogin, text="ENTRAR", font=("Arial",12,"bold"),compound="center")
        self.Btentrar.configure(fg="White",bg="#55ACEE", width=14,border=0)   # PAD TAMANHO DE DENTRO 
        self.Btentrar.grid(row=7,pady=20)

        #ACESSO AO REGISTRO

        self.regacesso_bt = Button(self.TelaLogin,text="Registrar-se",border=0, font=("Arial",12,"bold"),pady=15,command=self.registro)
        self.regacesso_bt.grid(row=8)

        self.root.bind('<Escape>', self.close)



    def telaRegistrar(self):

        self.telaRegistrar = tk.Frame(self.container)

        #TELA DE FUNDO
                
        self.telaRegistrar.configure(bg="")

        #FRAME01

        self.topframe1 = tk.Frame(self.telaRegistrar)
        self.topframe1.pack()
        self.topframe1.configure(bg="")

        #TITULO DO APP 

        self.titulo_label = Label(self.topframe1,text="Primeiro Acesso",width=23, font=("Ruda Regular",10,"bold"),bg="#644394",padx=0,pady=8,anchor="center",fg="white")
        self.titulo_label.grid(row=1,pady=15)
        self.titulo_label.configure()

        # NOME DO USUARIO
        
        self.nomeUsuario_label = Label(self.topframe1, text="Nome do Usuario:", font=("Arial",8,"bold"),padx=50)
        self.nomeUsuario_label.configure(fg="#644394")
        self.nomeUsuario_label.grid(row=2,sticky="w")
        self.nomeUsuario_label_entry = Entry(self.topframe1, width=20,highlightbackground="#BD4AB5",highlightthickness=0.5,font=12)
        self.nomeUsuario_label_entry.grid(row=3,padx=50,pady=5)

        #FRAME04

        self.topframe4 = tk.Frame(self.telaRegistrar)
        self.topframe4.pack()
        self.topframe4.configure(bg="")

        # ORIENTAÇÃO

        self.orientlb = Label(self.topframe4, text="DEFINA UMA SENHA", font=("Arial",8,"bold"),padx=50)
        self.orientlb.configure(fg="#644394",pady=2)
        self.orientlb.grid(sticky="w")

        # NOVA SENHA  
        
        self.novaSenha_label = Label(self.topframe4, text="Nova Senha:", font=("Arial",8,"bold"),padx=50)
        self.novaSenha_label.configure(fg="#644394")
        self.novaSenha_label.grid(row=12,sticky="w")

        self.novaSenha_label_entry = Entry(self.topframe4, width=20,highlightbackground="#BD4AB5",highlightthickness=0.5,font=10)
        self.novaSenha_label_entry.grid(row=13,padx=50,pady=5)

         # CONFIRMAÇÃO DA NOVA SENHA
        
        self.ConfirmaSenha_label = Label(self.topframe4, text="Confirmar Senha:", font=("Arial",8,"bold"),padx=50)
        self.ConfirmaSenha_label.configure(fg="#644394")
        self.ConfirmaSenha_label.grid(row=14,sticky="w")

        self.ConfirmaSenha_label_entry = Entry(self.topframe4, width=20,highlightbackground="#BD4AB5",highlightthickness=0.5,font=10)
        self.ConfirmaSenha_label_entry.grid(row=15,padx=50,pady=5)

        #FRAME05

        self.topframe5 = tk.Frame(self.telaRegistrar)
        self.topframe5.pack()
        self.topframe5.configure(bg="")

        # BOTÃO CADASTRAR

        self.salvarBt = Button(self.topframe5, text="Cadastrar", font=("Arial",11,"bold"),width=10)
        self.salvarBt.configure(fg="White",bg="#644394",border=0)   # PAD TAMANHO DE DENTRO 
        self.salvarBt.grid(row=0,column=0,padx=5,pady=10)

        # BOTÃO VOLTAR
        
        self.voltarbt = Button(self.topframe5, text="Voltar", font=("Arial",11,"bold"),width=10,command=self.inicio)
        self.voltarbt.configure(fg="White",bg="#644394",border=0)   # PAD TAMANHO DE DENTRO 
        self.voltarbt.grid(row=0,column=1,padx=5,pady=10)

    def close(self, evento=None):
        sys.exit()

    # def verificaLogin(self):
    #     if(self.controller.enviaTesteLogin(self.user_label_entry.get(),self.senha_label_entry.get())):
    #         self.nome.set(self.controller.DevolveNomebebe())
    #         self.acessoPermitido()
    #         self.puxaTabela()
    #         self.historico()

    #     else: 
    #         self.acessoNegado()


    def acessoPermitido(self):
        messagebox.showinfo("login","Bem vindo! acesso sucedido!")
        
    
    def acessoNegado(self):
        messagebox.showerror("Atenção","Verificar usuario e senha!")
 


View()