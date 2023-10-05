from pymongo import MongoClient
from bson.objectid import ObjectId
import time
import threading

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

        self.iniciar_insercao_periodica_em_segundo_plano()
        self.iniciar_troca_estado_periodicamente()

    def cadastrarProcesso(self, nomeProcesso, pid, nomeUsuarioUID, prioridade, usoCPU, estado, espacoMemoria):
        if(pid == '' or nomeProcesso == '' or nomeUsuarioUID == '' or prioridade == '' or usoCPU == '' or estado == '' or espacoMemoria == ''):
            return 0
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
    
    #NOME DIFF
    #PID DIFF
    #CPU DIFF
    #MEMORIA DIFF
    def inserir_processo(self):
        repository = self.db['processos']
        processo = {
            "_id": str(ObjectId()),
            "nomeProcesso": "processo",
            "pid": 123,
            "nomeUsuarioUID": "usuario",
            "prioridade": 1,
            "usoCPU": 1,
            "estado": "Pronto",
            "espacoMemoria": 1
        }
        repository.insert_one(processo)

    def inserirProcessoPeriodicamente(self, limite=10, intervalo=5):
        num_insercoes = 0
        while num_insercoes < limite:
            self.inserir_processo()
            num_insercoes += 1
            time.sleep(intervalo)

    def iniciar_insercao_periodica_em_segundo_plano(self):
        insercao_thread = threading.Thread(target=self.inserirProcessoPeriodicamente)
        insercao_thread.daemon = True
        insercao_thread.start()

    def trocaEstadoProcessoExecucao(self, estado):
        processoRepository = self.db['processos']
        filtro = {"estado": "Pronto"}
        newProcesso = { "$set": { 
            "estado": estado
            } 
        }
        result = processoRepository.update_many(filtro, newProcesso)
        return result.modified_count
    
    def teste(self, intervalo=5):
        while 1:
            self.trocaEstadoProcessoExecucao("Execução")
            time.sleep(intervalo)

    def iniciar_troca_estado_periodicamente(self):
        troca_thread = threading.Thread(target=self.teste)
        troca_thread.daemon = True
        troca_thread.start()


        
    def get_database(self):
        CONNECTION_STRING = 'mongodb://localhost:27017'
        client = MongoClient(CONNECTION_STRING)
        return client['Sistema_Operacional']
