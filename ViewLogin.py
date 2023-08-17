from tkinter import *
from PIL import Image, ImageTk
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x400")
        self.root.title("Sistemas Operacionais")
        self.root.resizable(False,False)
        self.container =tk.Frame(self.root)
        self.container.pack()

        self.telaLogin()
        self.TelaLogin.grid(row=0,column=0,sticky="nswe")

        self.inicio()

        self.root.mainloop()
    
    def inicio(self):
        self.TelaLogin.tkraise()

    def telaLogin(self):
        self.TelaLogin =tk.Frame(self.container)

        self.titulo_label = Label(self.TelaLogin,text="Sistemas\nOperacionais", font=("Arial",26),padx=30,pady=15,anchor="center",fg="#000000")
        self.titulo_label.grid(row=1)

        # NOME DO USUARIO
        self.user_label = Label(self.TelaLogin, text="Usuario", font=("Arial",12,"bold"),padx=50)
        self.user_label.grid(row=2,sticky="w")
        self.user_label_entry = Entry(self.TelaLogin,font= 11, width=20,highlightbackground="#000000",highlightthickness=0.5)
        self.user_label_entry.grid(row=3,padx=50,pady=2)

        # SENHA DO USUARIO
        self.senha_label = Label(self.TelaLogin, text="Senha", font=("Arial",12,"bold"),padx=50)
        self.senha_label.grid(row=4,sticky="w")
        self.senha_label_entry = Entry(self.TelaLogin, width=20,font= 11,highlightbackground="#000000",highlightthickness=0.5,show="•")
        self.senha_label_entry.grid(row=5,padx=50,pady=2)

        # BOTÃO ENTRAR
        self.Btentrar = Button(self.TelaLogin, text="ENTRAR", font=("Arial",12,"bold"),compound="center")
        self.Btentrar.configure(fg="White",bg="#55ACEE", width=14,border=0)   # PAD TAMANHO DE DENTRO 
        self.Btentrar.grid(row=6,pady=40)

        #ACESSO AO REGISTRO
        self.regacesso_bt = Button(self.TelaLogin,text="Registrar-se",border=0, font=("Arial",12,"bold"))
        self.regacesso_bt.grid(row=7)

        self.root.bind('<Escape>', self.close)

    def close(self, evento=None):
        sys.exit()

View()