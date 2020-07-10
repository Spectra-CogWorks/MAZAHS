from pathlib import Path
from samples_and_amp_array import get_mp3_samples, get_spec
from fingerprint_creator import local_peaks, fingerprint_create
from database_load_and_save import save_database, load_database
def add_song(song_name, artist, year, path = Path("file1.mp3")):
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
    database_pathway = '' #insert path here
    #load database
    (song_metadata, fingerprint_database) = load_database(database_pathway)
    #append metadata to the list
    song_metadata.append((song_name,artist,year))
    #call functions to get samples, create spectrogram, identify peaks, and create fingerprint
    (fi, fj, delta_t, abs_time) = fingerprint_create(local_peaks(get_spec(get_mp3_samples(path), 44100)), 10)
    #assign song_id
    song_id = len(song_metadata) 
    #add song data to fingerprint_database
    key = (fi, fj, delta_t)
    value = (song_id, abs_time)
    if key in fingerprint_database:
        fingerprint_database[key] = fingerprint_database[key].append(value)
    else:
        fingerprint_database[key] = [value]
        #save database
    save_database(song_metadata,fingerprint_database, database_pathway)
    #DONE
    return None
    
    