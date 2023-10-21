import time
import threading
import random
from bson.objectid import ObjectId
from database.database import Database

class ThreadingProcessos:
  def __init__(self):
    self.db = Database().get_database()
    self.nomesProcessos = ['bash.exe', 'python.exe', 'chrome.exe', 'code.exe', 'blitz.exe', 'explorer.exe', 'msedge.exe', 'mysql.exe', 'mongo.exe', 'excel.exe', 'word.exe', 'powerpoint.exe', 'notepad.exe', 'cmd.exe', 'java.exe', 'node.exe', 'php.exe', 'c++.exe', 'c.exe', 'c#.exe', 'ruby.exe', 'rust.exe', 'go.exe', 'dart.exe', 'flutter.exe', 'android.exe', 'ios.exe', 'ubuntu.exe', 'debian.exe', 'linux.exe', 'windows.exe', 'mac.exe', 'ios.exe']
    self.num_insercoes = 0

  def iniciar_insercao_periodica_em_segundo_plano(self):
    insercao_thread = threading.Thread(target=self.inserir_processo_periodicamente)
    insercao_thread.daemon = True
    insercao_thread.start()

  def inserir_processo_periodicamente(self, limite=10, intervalo=5):
    while True:
      self.inserir_processo()
      self.num_insercoes += 1
      time.sleep(intervalo)
      lista_processos = list(self.db['processos'].find())
      self.iniciar_verificacao_estados(lista_processos)
      time.sleep(intervalo)
      self.delete_one_processo()
        
  def iniciar_verificacao_estados(self, lista_processos):
    repository = self.db['processos']
    for processo in lista_processos:
      if processo.get("completou_ciclo", False) == True:
        if processo["estado"] == "Execução":
          filtro = {"_id": processo["_id"]}
          newProcesso = {"$set": {"estado": "Fim"}}
          repository.update_one(filtro, newProcesso)
        else:
          processoEmExecucao = repository.find_one({"estado": "Execução"})
          if processoEmExecucao is not None:
            filtro = {"_id": processoEmExecucao["_id"]}
            newProcesso = {"$set": {"estado": "Espera"}}
            repository.update_one(filtro, newProcesso)
  
          filtro = {"_id": processo["_id"]}
          newProcesso = {"$set": {"estado": "Execução"}}
          repository.update_one(filtro, newProcesso)

      elif processo["estado"] == "Início":
        filtro = {"_id": processo["_id"]}
        newProcesso = { "$set": {"estado": "Pronto"}}
        repository.update_one(filtro, newProcesso)

      elif processo["estado"] == "Execução":
        filtro = {"_id": processo["_id"]}
        if processo.get("completou_ciclo", False) == True: 
          newProcesso = { "$set": {"estado": "Fim" }}
        else:
          newProcesso = { "$set": {"estado": "Espera"}}
        repository.update_one(filtro, newProcesso)

      elif processo["estado"] == "Pronto":
        processoEmExecucao = repository.find_one({"estado": "Execução"})
        if processoEmExecucao is None:
            filtro = {"_id": processo["_id"]}
            newProcesso = { "$set": {"estado": "Execução"}}
            repository.update_one(filtro, newProcesso)
        else:
            filtro = {"_id": processo["_id"]}
            newProcesso = { "$set": {"estado": "Pronto"}}
            repository.update_one(filtro, newProcesso)

      elif processo["estado"] == "Espera":
        filtro = {"_id": processo["_id"]}
        newProcesso = {"$set": {"estado": "Pronto", "completou_ciclo": True}}
        repository.update_one(filtro, newProcesso)
  
  def inserir_processo(self):
    repository = self.db['processos']
    processo = {
        "_id": str(ObjectId()),
        "nomeProcesso": random.choice(self.nomesProcessos),
        "pid": random.randint(1, 9999),
        "nomeUsuarioUID": "admin",
        "prioridade": "Normal",
        "usoCPU": (str(random.randint(1, 99))+'%'),
        "estado": "Início",
        "espacoMemoria": (str(random.randint(1, 1024))+' mb')
    }
    repository.insert_one(processo)
    return processo

  def delete_one_processo(self):
    processoRepository = self.db['processos']
    processoRepository.delete_one({"estado": "Fim"})
    self.inserir_processo_periodicamente()

  
