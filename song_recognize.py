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

def tally(fingerprints):
	"""
	This function tallies the matches to the database dictionary's stored fingerprints
	and stores the matches organized by song ID and then offsets within each song
	
	Parameters:
	-----------
	fingerprints: List[Tuple(initial_peak_freq, fanout_peak_freq, time_interval, initial_time)]
		This list contains the fingerprints stored as tuples of the format
		(initial_peak_freq, fanout_peak_freq, time_interval, initial_time)
	
	Returns:
	--------
	tallies: Dictionary[song_id:offset_counters]
		This is the dictionary where each key is a song ID and stores a Counter object
		that has entries for each offset and the number of matches for each one
	"""
	# // TODO Code the function
	# TODO Debug the function
	# Initialize tallies dictionary
	tallies = {}
	
	# Load the database dictionary and song metadata
	song_metadata, database = db.load_database()
	
	# Iterate through fingerprints
	for fingerprint in fingerprints:
		# Check for an instance of the fingerprint without the absolute time in the database dictionary
		# and if it is there, iterate over the list of tuples that contain a songID and absolute time
		if fingerprint[0:3] in database:
			# Matches is a list of tuples filled with the song IDs and offsets
			matches = database[fingerprint[0:3]]
			for match in matches:
				# Use the absolute time of the database and the absolute time of the fingerprint to calculate the
				# offset that will be used to create an offset for each song ID in the tallies
				offset = match[1] - fingerprint[3]
		
				# Add to the appropriate counters in tallies by giving song ID then using the offset to add to the 
				# appropriate entry
				# Also checking to make sure that songId
				songId = matches[0]
				if songId in tallies:
					tallies[songId][offset] += 1
				else:
					tallies[songId] = Counter()
		
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
	(songId, offset)
		The song ID and offset that have the highest number of matches
	"""
	# TODO Code the function
	
	# ! For now, just use the song and offset with the maximum count
	# Print chosen song and offset
	highest_count_info = (0,0,0)
	#highest_count = (count of offsets, offset, song_id)
	for song in tallies:
		offset_counter = tallies[song]
		offset, count = offset_counter.most_common([1])
		#Gets the most common offset
		high_count, high_offset, high_song = highest_count_info
		#unpacks the highest_count tuple
		if high_count < count:
			highest_count_info = (count, offset, song)
			#if count is higher than the previous highest, updates info for highest count
	finalcount, finaloffset, song_id = highest_count_info
	#unpacks highest count tuple
	return song_id, finaloffset
	#returns the song id and offset for the highest count

	