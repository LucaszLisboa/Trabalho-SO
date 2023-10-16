from bson.objectid import ObjectId
from database.database import Database
import hashlib
import datetime

class ModelUser:
    def __init__(self):
        self.id = None
        self.nome = None
        self.senha = None
        self.dataCadastro = None
        self.db = Database().get_database()

    def cadastrarUsuario(self, nome, senha, confirmacaoSenha):
        existeCadastro = self.validaCadastro(nome)
        if existeCadastro == False:
            if senha == confirmacaoSenha:
                self.id = str(ObjectId())
                self.nome = nome
                self.dataCadastro = datetime.datetime.now()
                senhaEncriptada = hashlib.sha256(senha.encode()).hexdigest()
                self.senha = senhaEncriptada
                collection = self.db['usuarios']
                user = {
                    "_id": self.id,
                    "nome": self.nome,
                    "senha": self.senha,
                    "dataCadastro": self.dataCadastro
                }
                collection.insert_one(user)
            else:
                user = "senhas_distintas"
        else:
            user = "usuario_ja_cadastrado"
        return user
            
     
    def validaCadastro(self, nome):
        collection = self.db['usuarios']
        registro = collection.find_one({"nome": nome})
        print(registro)
        if registro == None:
            return False
        else:
            return True
    
    def verificarLogin(self, usuario, senha):
        senhaEncriptada = hashlib.sha256(senha.encode()).hexdigest()
        collection = self.db['usuarios']
        registro = collection.find_one({"nome": usuario, "senha": senhaEncriptada})
        if registro == None:
            return False
        else:
            return True

