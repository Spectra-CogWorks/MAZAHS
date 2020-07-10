"""
A module to recognize songs by querying the database, tallying matches to songs, 
and using an experimentally determined algorithm to decide the song the sample
matches to.
"""

def tally(fingerprints):
	"""
	This function tallies the matches to the database dictionary's stored fingerprints
	and stores the matches organized by song ID and then offsets within each song
	
	Parameters:
	-----------
	fingerprints: List[Tuple()]
		This list contains the fingerprints stored as tuples of the format
		(initial_peak_freq, fanout_peak_freq, time_interval, initial_time)
	
	Returns:
	--------
	tallies: Dictionary[song_id:offset_counters]
		This is the dictionary where each key is a song ID and stores a Counter object
		that has entries for each offset and the number of matches for each one
	"""
	
	pass

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
	
	pass