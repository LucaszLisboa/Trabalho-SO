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
    while self.num_insercoes < limite:
      self.inserir_processo()
      self.num_insercoes += 1
      time.sleep(intervalo)
      lista_processos = list(self.db['processos'].find())
      self.iniciar_verificacao_estados(lista_processos)
    if self.num_insercoes == limite:
      self.num_insercoes -= 1
      self.delete_one_processo()
        
  def iniciar_verificacao_estados(self, lista_processos):
    for processo in lista_processos:
      if processo["estado"] == "Início":
        thread = threading.Thread(target=self.troca_estado_processo, args=(processo, "Início", "Pronto"))
        thread.daemon = True
        thread.start()
      elif processo["estado"] == "Pronto":
        thread = threading.Thread(target=self.troca_estado_processo, args=(processo, "Pronto", "Execução"))
        thread.daemon = True
        thread.start()
      elif processo["estado"] == "Execução":
        thread = threading.Thread(target=self.troca_estado_processo, args=(processo, "Execução", "Espera"))
        thread.daemon = True
        thread.start()
      elif processo["estado"] == "Espera":
        thread = threading.Thread(target=self.troca_estado_processo, args=(processo, "Espera", "Pronto"))
        thread.daemon = True
        thread.start()
      elif processo["estado"] == "Execução" and self.num_insercoes == 9:
        thread = threading.Thread(target=self.troca_estado_processo, args=(processo, "Execução", "Fim"))
        thread.daemon = True
        thread.start()

  
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


  def troca_estado_processo(self, processo, estadoAtual, estadoNovo):
    while True:
      processoRepository = self.db['processos']
      filtro = {"estado": estadoAtual}
      newProcesso = { "$set": { 
          "estado": estadoNovo
          } 
      }
      if estadoNovo == "Execução":
        # Encontre um único processo em estado "Pronto" e atualize para "Execução"
        processoEmExecução = processoRepository.find_one({"estado": "Execução"})
        if processoEmExecução is None:
          filtro["_id"] = processo["_id"]
          processoRepository.update_one(filtro, newProcesso)
        else:
          print("Já existe um processo em execução")
      else:
          # Atualize todos os processos no estado atual para o novo estado
          processoRepository.update_one(filtro, newProcesso)
      time.sleep(5)


  def delete_one_processo(self):
    processoRepository = self.db['processos']
    processoRepository.delete_one({"estado": "Pronto"})
    self.inserir_processo_periodicamente()

  
