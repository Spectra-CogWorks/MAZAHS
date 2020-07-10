import pickle
from pathlib import Path

class DatabaseManager:
  __default = False
  __path = Path("./database.pickle")

  @staticmethod
  def set_path(path):
    """Sets the path to be used by the singleton.

    Sets the path to load the database from. (This method has no effect if
    default has already been called)

    Parameters
    ----------
    path: Optional[Path]
      Path to load database from, ignored if None
    """
    if path != None:
      DatabaseManager.__path = path

  @staticmethod
  def default():
    """Returns the singleton.

    Returns the `DatabaseManager` singleton, initializing it if neccassary.

    Returns
    -------
    singleton: DatabaseManager
      Singleton controlling loading from the database.
    """
    if DatabaseManager.__default:
      return DatabaseManager.__default
    else:
      DatabaseManager.__default = DatabaseManager()
      return DatabaseManager.__default
  
  def __init__(self):
    """Initialize the singleton.

    Intializes the singleton, loading data from `__path`.
    """
    print("Loading database...")
    self.metadata, self.fingerprint_database = pickle.load(
      open(DatabaseManager.__path, "rb")
    )