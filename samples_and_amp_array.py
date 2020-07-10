import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import librosa
from IPython.display import Audio
from typing import Union, Callable, Tuple
from pathlib import Path

# normalizing arrays
def rescale(array, new_min, new_max):
    """
    Normalizes all the samples to a common range.
    
    Parameters
    ----------
    array : numpy.ndarray
        A shape-(N,) array that needs to be rescaled.
    
    new_min : int
        The desired minimum of the array after scaling.

    new_max : int
        The desired maximum of the array after scaling.

    Returns
    -------
    numpy.ndarray
        A shape-(N,) array rescaled to the desired range.
    """
    minimum, maximum = np.min(array), np.max(array)
    ratio = (new_max - new_min) / (maximum - minimum)
    scaled_array = ratio * array
    shift = np.min(scaled_array) - new_min
    return scaled_array - shift

# microphone samples
def get_mic_samples(listen_time):
    """
    Uses microphone to record and digitize an analog signal.
    
    Parameters
    ----------
    listen_time : float
        Length of recording in seconds.
    
    Returns
    -------
    samples : numpy.ndarray
            A shape-(N,) array of samples extracted from the analog signal, scaled to the range (-2**15, 2**15).
    """
    # record audio through mic
    from microphone import record_audio
    frames, sample_rate = record_audio(listen_time)

    samples = [np.frombuffer(frames[i], np.int16) for i in range(len(frames))]
    samples = np.hstack(samples)

    return rescale(samples, -2**15, 2**15)

# mp3 samples
def get_mp3_samples(file_path):
    """
    Loads a local mp3 file and digitizes the analog signal.
    
    Parameters
    ----------
    file_path : Union[str, pathlib.Path]
        Path to the mp3 file. E.g. "my_audio.npy" will load an audio
        file called "my_audio.npy" to the current working directory.
    
    Returns
    -------
    samples : numpy.ndarray
            A shape-(N,) array of samples extracted from the analog signal, scaled to the range (-2**15, 2**15).
    """
    local_song_path = Path(file_path)

    # load the digital signal for the song
    samples, sampling_rate = librosa.load(local_song_path, sr=44100, mono=True)

    return rescale(samples, -2**15, 2**15)

# obtaining the spectrogram for the waveform
sampling_rate = 44100 # or set to whatever

def get_spec(samples, sampling_rate):
    """
    Returns the 2d-array of spectrogram data.
    
    Parameters
    ----------
    samples : numpy.ndarray
        A shape-(N,) array of samples extracted from the analog signal.

    sampling_rate : int
        The sampling rate at which the samples were extracted.
    
    Returns
    -------
    S : numpy.ndarray
            A 2d-array of Fourier coefficients organized by frequencies (rows) and times (columns).
    """
    S, freqs, times = mlab.specgram(
        samples,
        NFFT=4096,
        Fs=sampling_rate,
        window=mlab.window_hanning,
        noverlap=int(4096 / 2),
        mode='magnitude'
    )

    S[S == 0] = 1e-20

    return S
