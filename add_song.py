from pathlib import Path
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
    
    song_metadata.append((song_name,artist,year))
    
    #run mp3 to samples function
    #run sample to spectogram function
    #run peak finding function
    #run fingerprint creation function with output ((fi, fj, delta_t, abs_time))
    #make song id
    #add song to dictionary with key: (fi, fj, delta_t) and value: List of tuple with song_id and abs_time
    
    
    return None
    