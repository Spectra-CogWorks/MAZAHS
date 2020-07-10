"""
A module to recognize songs by querying the database, tallying matches to songs, 
and using an experimentally determined algorithm to decide the song the sample
matches to.
"""

# Library imports
from collections import Counter
from pathlib import Path

# Module imports
import database as db

def tally(fingerprints, database_path):
	"""
	This function tallies the matches to the database dictionary's stored fingerprints
	and stores the matches organized by song ID and then offsets within each song
	
	Parameters:
	-----------
	fingerprints: List[Tuple(initial_peak_freq, fanout_peak_freq, time_interval, initial_time)]
		This list contains the fingerprints stored as tuples of the format
		(initial_peak_freq, fanout_peak_freq, time_interval, initial_time)
		
	database_path: Path
		The path to the database 
	
	Returns:
	--------
	tallies: Dictionary[song_id:offset_counters]
		This is the dictionary where each key is a song ID and stores a Counter object
		that has entries for each offset and the number of matches for each one
	"""
	# TODO Code the function
	# Initialize tallies dictionary
	tallies = {}
	
	# Load the database dictionary
	database = db.load_database(database_path)
	
	# Iterate through fingerprints
	
		# Check for an instance of the fingerprint without the absolute time in the database dictionary
		# and if it is there, iterate over the list of tuples that contain a songID and absolute time
		
		# Use the absolute time of the database and the absolute time of the fingerprint to calculate the
		# offset that will be used to create an offset for each song ID in the tallies
		
		# Add to the appropriate counters in tallies by giving song ID then using the offset to add to the 
		# appropriate entry
		
	# Return tallies
	return tallies

def determine_song(tallies):
	"""
	This function determines the sample's matched song along with the specific offset and prints it
	
	Parameters:
	-----------
	tallies: Dictionary[song_id:offset_counters]
		This is the dictionary where each key is a song ID and stores a Counter object
		that has entries for each offset and the number of matches for each one
	
	Returns:
	--------
	None
	"""
	
	