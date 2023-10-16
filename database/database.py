from pymongo import MongoClient

class Database:
  def __init__(self):
    self.db = self.get_database()
  
  def get_database(self):
    CONNECTION_STRING = 'mongodb://localhost:27017'
    client = MongoClient(CONNECTION_STRING)
    return client['Sistema_Operacional']