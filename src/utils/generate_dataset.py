import sqlite3
from dataclasses import dataclass
from typing import Dict
from ..configuration import Configuration


@dataclass
class Track:
    title: str
    track_id: str
    artist_name: str
    lyrics: Dict[str, int] = None


def generate(songs_database, metadata_database):
    lyrics = sqlite3.connect(songs_database)
    metadata = sqlite3.connect(metadata_database)

    tracks = metadata.execute("SELECT track_id, title, artist_name from songs").fetchall()
    tracks_dict = {}

    query = "SELECT track_id, word, count FROM lyrics"
    i = 0
    print('Loading the dataset from database...')
    for t in tracks:
        track_id, title, artist_name = t
        track = Track(title, track_id, artist_name)
        tracks_dict[t[0]] = track
        words = lyrics.execute(query + f" where track_id = '{track.track_id}'").fetchall()
        track = tracks_dict[track_id]
        track.lyrics = {}
        for w in words:
            id, word, count = w
            track.lyrics[word] = count
        i+=1
        print(f'{(i/10000.0)}%', end="\r")
    print('Dataset loaded')
    return tracks_dict


def does_file_exist(path):
    try:
        with open(path, 'r') as f:
            pass
    except IOError:
        return False
    return True


def get_dataset(configuration: Configuration):
    import pickle
    data = None

    try:
        with open(configuration.dataset_path, 'rb') as f:
            print('Loading dataset from the drive....')
            data = pickle.load(f)
            print('Dataset loaded')
        reload_database = False
    except IOError:
        print('File is not present, will reload database...')
        reload_database = True

    if reload_database:
        print(configuration.lyrics_database)
        data = generate(configuration.lyrics_database, configuration.metadata_database)
        print('Pickling ... ')
        with open(configuration.dataset_path, 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    return data
