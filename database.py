import pickle
from database_manager import DatabaseManager

def save_database(metadata, fingerprint_database, path):
	"""Saves metadata and fingerprint database to a file.

	Saves `metadata` and `fingerprint_database` to file specified by `path`.

	Parameters
	----------
	metadata : List[Tuple[str, str, str]]
		List of song song metadata as tuples of the form (name, artist, year)

	fingerprint_database : Dict[Tuple[int, int, int], Tuple[int, int]]
		Song metadata dictionary as dictionary mapping from (f_i, f_j, delta_t)
		to (song ID, absolute position)

	path : Path
		The path to save the database file to
	"""
	print("Saving to disk...")
	pickle.dump((metadata, fingerprint_database), open(path, "wb"))
	print("Saved!")

def init_database(path):
	"""Initalizes a new song database.

	Initializes a song database in a file specified by `path`.

	Parameters
	----------
	path : Path
		The path to save the database file to
	"""
	print("Saving to disk...")
	pickle.dump(([], {}), open(path, "wb"))
	print("Saved!")

def load_database(path=None):
	"""Load metadata and fingerprint database from a file.

	Load `metadata` and `fingerprint_database` from file specified by `path`.

	Parameters
	----------
	path : Path
		The path to save the database file to

	Returns
	-------
	database : Tuple[List[Tuple[str, str, str]], 
		Dict[Tuple[int, int, int], Tuple[int, int]]]
		Tuple containing song metadata and the fingerprint database as
		described for `save_database`
	"""
	print("Loading database...")
	DatabaseManager.set_path(path)
	return (
		DatabaseManager.default().metadata,
		DatabaseManager.default().fingerprint_database
	)