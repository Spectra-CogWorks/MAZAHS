import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from typing import Tuple
import librosa
from IPython.display import Audio
from typing import Union, Callable, Tuple
from pathlib import Path

# normalizing arrays
def rescale(array, new_min, new_max):
    minimum, maximum = np.min(array), np.max(array)
    ratio = (new_max - new_min) / (maximum - minimum)
    scaled_array = ratio * array
    shift = np.min(scaled_array) - new_min
    return scaled_array - shift

# microphone samples
def get_mic_samples(listen_time):

    from microphone import record_audio
    frames, sample_rate = record_audio(listen_time)

    samples = [np.frombuffer(frames[i], np.int16) for i in range(len(frames))]
    samples = np.hstack(samples)

    return rescale(samples, -2**15, 2**15)

# mp3 samples
def get_mp3_samples(file_path):

    local_song_path = Path(file_path)

    # load the digital signal for the song
    samples, sampling_rate = librosa.load(local_song_path, sr=44100, mono=True)
    samples = np.interp(samples, (samples.min(), samples.max()), (-2**15, 2**15))

    return rescale(samples, -2**15, 2**15)

# obtaining the spectrogram for the waveform
sampling_rate = 44100 # or set to whatever

def get_spec(samples, sampling_rate):
    S, freqs, times = mlab.specgram(
        samples,
        NFFT=4096,
        Fs=sampling_rate,
        window=mlab.window_hanning,
        noverlap=int(4096 / 2),
        mode='magnitude'
    )
    return S
