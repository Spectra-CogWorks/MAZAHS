"""
Module to find and analyze peaks in spectrogram data for sound samples and create fingerprints for samples using pattern fanouts
"""

def local_peaks(spec_samples):
	"""
	"""
	# ! Delete this pass
	pass

def fingerprint_create(peaks, fanoutVal):
	"""
	Creates a fingerprint by creating a list of fanout patterns based on each peak traversed in order of 
	ascending frequency and then time

	Parameters:
	-----------
	peaks: List[Tuples]
		A list of the peaks found from the samples with tuples containing their row and column indices from the
		spectrogram sample array

	fanoutVal: int
		A constant that decides the number of peaks that are recorded in each fanout pattern

	Returns:
	--------
	fingerprints: List[Tuple(initial_peak_freq, fanout_peak_freq, time_interval, initial_time)]
		A list of tuples containing the initial peak frequency, the other peak's frequency, the time of the initial peak, 
		and time interval between the two peaks

	"""
	# // TODO Test the function with sample data and fix bugs
	# // TODO Optimize the code once the base design is working and has base functionality
	
	# Initialize the fingerprints array
	fingerprints = []
	
	# Check that there are enough peaks for the fanout value otherwise return a more informative error
	assert len(peaks) > fanoutVal, "There are too few peaks to create a fingerprint"

	# Iterate over the peaks array which should be already organized by ascending frequency and time
	for i in range(len(peaks)):
		# Iterate over range(1, fanoutVal+1) to create the fanout pattern
		for n in range(i+1, i+fanoutVal+1):
			if n >= len(peaks):
				break
				
			# The time_interval is calculated as the time of the fanout_peak minus the time of the initial_peak
			# Append the tuple to the list (initial_peak, fanout_peak, initial_time, time_interval)
			# The tuple contains these values initial_peak_freq, fanout_peak_freq, time_interval, initial_time
			fingerprints.append((peaks[i][1], peaks[n][1], peaks[n][0]-peaks[i][0], peaks[i][0]))
	
	# Return the fingerprints list
	return fingerprints