from pathlib import Path
from samples_and_amp_array import get_mp3_samples, get_spec
from fingerprint_creator import local_peak_locations, fingerprints_create
from database import save_database, load_database
def add_song(song_name, artist, year, song_path, database_path):
    """Adds new song to database and stores metadata in metadata list.

    Parameters
    ----------
    song_name: string
        The name of the song
    artist: string
        The artist associated with the song
    year: string
        The year of the song's release
    path: Path object
        The pathway to the .mp3 file with the song

    Returns
    -------
    None"""
    #load database
    song_metadata, fingerprint_database = load_database(database_path)
    #append metadata to the list
    song_metadata.append((song_name,artist,year))
    #call functions to get samples, create spectrogram, identify peaks, and create fingerprints
    song_fingerprints = fingerprints_create(local_peak_locations(get_spec(get_mp3_samples(song_path), 44100)), 10)
    #assign song_id (first id is 0)
    song_id = len(song_metadata) - 1
    for fingerprint in song_fingerprints:
        #unpack fingerprint and repack into key and value
        fi, fj, delta_t, abs_time = fingerprint
        key = (fi, fj, delta_t)
        value = (song_id, abs_time)
        #add fingerprint data to fingerprint_database
        if key in fingerprint_database:
            fingerprint_database[key].append(value)
        else:
            fingerprint_database[key] = [value]
    #save database
    save_database(song_metadata,fingerprint_database, database_path)
    #DONE
    return None