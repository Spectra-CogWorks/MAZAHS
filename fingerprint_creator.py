"""
Module to find and analyze peaks in spectrogram data for sound samples
and create fingerprints for samples using pattern fanouts
"""

from numba import njit
import numpy as np

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure
from scipy.ndimage.morphology import iterate_structure

# `@njit` "decorates" the `_peaks` function. This tells Numba to
# compile this function using the "low level virtual machine" (LLVM)
# compiler. The resulting object is a Python function that, when called,
# executes optimized machine code instead of the Python code

@njit
def _peaks(data_2d, rows, cols, amp_min):
    """
    A Numba-optimized 2-D peak-finding algorithm. This is just a helper function.
    Use "local_peak_locations" instead if you want to get the peaks.
    
    Parameters
    ----------
    data_2d : numpy.ndarray, shape-(H, W)
        The 2D array of data in which local peaks will be detected.

    rows : numpy.ndarray, shape-(N,)
        The 0-centered row indices of the local neighborhood mask
    
    cols : numpy.ndarray, shape-(N,)
        The 0-centered column indices of the local neighborhood mask
        
    amp_min : float
        All amplitudes at and below this value are excluded from being local 
        peaks.
    
    Returns
    -------
    List[Tuple[int, int]]
        (row, col) index pair for each local peak location. 
    """
    peaks = []
    
    # iterate over the 2-D data in col-major order
    for c, r in np.ndindex(*data_2d.shape[::-1]):
        if data_2d[r, c] <= amp_min:
            continue

        for dr, dc in zip(rows, cols):
            # don't compare element (r, c) with itself
            if dr == 0 and dc == 0:
                continue

            # mirror over array boundary
            if not (0 <= r + dr < data_2d.shape[0]):
                dr *= -1

            # mirror over array boundary
            if not (0 <= c + dc < data_2d.shape[1]):
                dc *= -1

            if data_2d[r, c] < data_2d[r + dr, c + dc]:
                break
        else:
            peaks.append((r, c))
    return peaks


def local_peak_locations(data_2d, threshold_percentile=75):
    """
    Defines a local neighborhood and finds the local peaks
    in the spectrogram, which must be larger than the specified `peak_threshold`.
    
    Parameters
    ----------
    data_2d : numpy.ndarray, shape-(H, W)
        The 2D array of data in which local peaks will be detected.
        Comes from the spectrogram.
    
    threshold_percentile : int
        The percentile at which we are distinguishing between the foreground 
        and background data.
    
    Returns
    -------
    List[Tuple[int, int]]
        (row, col) index pair for each local peak location.
    
    Notes
    -----
    The local peaks are returned in column-major order.
    """
    peak_threshold = np.percentile(data_2d, threshold_percentile)
    neighborhood= iterate_structure(generate_binary_structure(2,1), 20)

    rows, cols = np.where(neighborhood)
    assert neighborhood.shape[0] % 2 == 1
    assert neighborhood.shape[1] % 2 == 1

    # center neighborhood indices around center of neighborhood
    rows -= neighborhood.shape[0] // 2
    cols -= neighborhood.shape[1] // 2
    
    return _peaks(data_2d, rows, cols, amp_min=peak_threshold)

def fingerprints_create(peaks, fanoutVal=15):
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
	
	# Initialize the fingerprints list
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