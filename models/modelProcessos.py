from pymongo import MongoClient
from bson.objectid import ObjectId

class ModelProcessos:
    def __init__(self):
        self.id = None
        self.nomeProcesso = None
        self.pid = None
        self.nomeUsuarioUID = None
        self.prioridade = None
        self.usoCPU = None
        self.estado = None
        self.espacoMemoria = None
        self.db = self.get_database()

    def cadastrarProcesso(self, nomeProcesso, pid, nomeUsuarioUID, prioridade, usoCPU, estado, espacoMemoria):
        self.id = str(ObjectId())
        self.nomeProcesso = nomeProcesso
        self.pid = pid
        self.nomeUsuarioUID = nomeUsuarioUID
        self.prioridade = prioridade
        self.usoCPU = usoCPU
        self.estado = estado
        self.espacoMemoria = espacoMemoria
        collection = self.db['processos']
        processo = {
            "_id": self.id,
            "nomeProcesso": self.nomeProcesso,
            "pid": self.pid,
            "nomeUsuarioUID": self.nomeUsuarioUID,
            "prioridade": self.prioridade,
            "usoCPU": self.usoCPU,
            "estado": self.estado,
            "espacoMemoria": self.espacoMemoria
        }
        collection.insert_one(processo)
        return processo   
        
    def get_database(self):
        CONNECTION_STRING = 'mongodb://localhost:27017'
        client = MongoClient(CONNECTION_STRING)
        return client['Sistema_Operacional']
