import pickle
from pathlib import Path

class DatabaseManager:
  __default = False
  __path = Path("./database.pickle")

  @staticmethod
  def set_path(path):
    if path != None:
      DatabaseManager.__path = path

  @staticmethod
  def default():
    if DatabaseManager.__default:
      return DatabaseManager.__default
    else:
      DatabaseManager.__default = DatabaseManager()
      return DatabaseManager.__default
  
  def __init__(self):
    self.metadata, self.fingerprint_database = pickle.load(
      open(DatabaseManager.__path, "rb")
    )