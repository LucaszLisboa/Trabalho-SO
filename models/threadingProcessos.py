import time
import threading
import random
from bson.objectid import ObjectId
from database.database import Database

class ThreadingProcessos:
  def __init__(self):
    self.db = Database().get_database()
    self.nomesProcessos = ['bash.exe', 'python.exe', 'chrome.exe', 'code.exe', 'blitz.exe', 'explorer.exe', 'msedge.exe', 'mysql.exe', 'mongo.exe', 'excel.exe', 'word.exe', 'powerpoint.exe', 'notepad.exe', 'cmd.exe', 'java.exe', 'node.exe', 'php.exe', 'c++.exe', 'c.exe', 'c#.exe', 'ruby.exe', 'rust.exe', 'go.exe', 'dart.exe', 'flutter.exe', 'android.exe', 'ios.exe', 'ubuntu.exe', 'debian.exe', 'linux.exe', 'windows.exe', 'mac.exe', 'ios.exe']
    self.iniciar_insercao_periodica_em_segundo_plano()
    self.iniciar_troca_estado_periodicamente()
    # self.iniciar_troca_estado_para_pronto_periodicamente()
    # self.iniciar_troca_estado_para_execucao_periodicamente()
    # self.iniciar_troca_estado_para_espera_periodicamente()
    # self.iniciar_troca_estado_para_pronto_periodicamente2()
    # self.iniciar_threads()

    
  def iniciar_insercao_periodica_em_segundo_plano(self):
    insercao_thread = threading.Thread(target=self.inserir_processo_periodicamente)
    insercao_thread.daemon = True
    insercao_thread.start()

  def inserir_processo_periodicamente(self, limite=10, intervalo=5):
    num_insercoes = 0
    while num_insercoes < limite:
        self.inserir_processo()
        num_insercoes += 1
        time.sleep(intervalo)
  
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



  def iniciar_threads(self):
    self.iniciar_troca_estado_periodicamente("Início", "Pronto")
    self.iniciar_troca_estado_periodicamente("Pronto", "Execução")
    self.iniciar_troca_estado_periodicamente("Execução", "Espera")
    self.iniciar_troca_estado_periodicamente("Espera", "Pronto")


  def iniciar_troca_estado_periodicamente(self):
    troca_thread = threading.Thread(target=self.troca_estado_processo_periodicamente)
    troca_thread.daemon = True
    troca_thread.start()
    
  def troca_estado_processo_periodicamente(self):
    while True:
      self.troca_estado_processo("Início", "Pronto")
      time.sleep(5)
      self.troca_estado_processo("Pronto", "Execução")
      time.sleep(5)
      self.troca_estado_processo("Execução", "Espera")
      time.sleep(5)
      self.troca_estado_processo("Espera", "Pronto")
      time.sleep(5)







  # def iniciar_troca_estado_para_pronto_periodicamente(self):
  #   troca_thread = threading.Thread(target=self.troca_estado_processo_para_pronto_periodicamente, args=("Início", "Pronto"))
  #   troca_thread.daemon = True
  #   troca_thread.start()

  # def troca_estado_processo_para_pronto_periodicamente(self, estadoAtual, estadoNovo):
  #   while True:
  #     self.troca_estado_processo(estadoAtual, estadoNovo)
  #     time.sleep(5)


  
  # def iniciar_troca_estado_para_execucao_periodicamente(self):
  #   troca_thread = threading.Thread(target=self.troca_estado_processo_para_execucao_periodicamente)
  #   troca_thread.daemon = True
  #   troca_thread.start()

  # def troca_estado_processo_para_execucao_periodicamente(self):
  #   while True:
  #     self.troca_estado_processo("Pronto", "Execução")
  #     time.sleep(5)

  

  # def iniciar_troca_estado_para_espera_periodicamente(self):
  #   troca_thread = threading.Thread(target=self.troca_estado_processo_para_espera_periodicamente)
  #   troca_thread.daemon = True
  #   troca_thread.start()

  # def troca_estado_processo_para_espera_periodicamente(self):
  #   while True:
  #     self.troca_estado_processo("Execução", "Espera")
  #     time.sleep(5)

  

  # def iniciar_troca_estado_para_pronto_periodicamente2(self):
  #   troca_thread = threading.Thread(target=self.troca_estado_processo_para_pronto_periodicamente, args=("Espera", "Pronto"))
  #   troca_thread.daemon = True
  #   troca_thread.start()



  def troca_estado_processo(self, estadoAtual, estadoNovo):
    processoRepository = self.db['processos']
    filtro = {"estado": estadoAtual}
    newProcesso = { "$set": { 
        "estado": estadoNovo
        } 
    }
    # if estadoNovo == "Execução":
    #   # Encontre um único processo em estado "Pronto" e atualize para "Execução"
    #   processo = processoRepository.find_one({"estado": "Pronto"})
    #   if processo:
    #     filtro["_id"] = processo["_id"]
    #     processoRepository.update_one(filtro, newProcesso)
    # else:
        # Atualize todos os processos no estado atual para o novo estado
    processoRepository.update_many(filtro, newProcesso)
  
