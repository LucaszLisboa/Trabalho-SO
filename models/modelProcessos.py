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
        processoRepository = self.db['processos']
        existeProcesso = processoRepository.find_one({"pid": pid})
        if existeProcesso:
            modified_count = self.editarProcesso(nomeProcesso, pid, nomeUsuarioUID, prioridade, usoCPU, estado, espacoMemoria)
            return modified_count
        else:
            self.id = str(ObjectId())
            self.nomeProcesso = nomeProcesso
            self.pid = pid
            self.nomeUsuarioUID = nomeUsuarioUID
            self.prioridade = prioridade
            self.usoCPU = usoCPU
            self.estado = estado
            self.espacoMemoria = espacoMemoria
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
            processoRepository.insert_one(processo)
            return processo  

    def consultarProcessos(self):
        processoRepository = self.db['processos'] 
        processos = processoRepository.find()
        return processos
    
    def deletarProcesso(self, pid):
        pid = str(pid)
        processoRepository = self.db['processos']
        result = processoRepository.delete_one({"pid": pid})
        return result.deleted_count
    
    def editarProcesso(self, nomeProcesso, pid, nomeUsuarioUID, prioridade, usoCPU, estado, espacoMemoria):
        pid = str(pid)
        processoRepository = self.db['processos']
        processo = processoRepository.find_one({"pid": pid})
        newProcesso = { "$set": { 
            "nomeProcesso": nomeProcesso, 
            "nomeUsuarioUID":nomeUsuarioUID, 
            "prioridade": prioridade,
            "usoCPU": usoCPU,
            "estado": estado,
            "espacoMemoria": espacoMemoria
            } 
        }
        result = processoRepository.update_one(processo, newProcesso)
        return result.modified_count
    

        
    def get_database(self):
        CONNECTION_STRING = 'mongodb://localhost:27017'
        client = MongoClient(CONNECTION_STRING)
        return client['Sistema_Operacional']
