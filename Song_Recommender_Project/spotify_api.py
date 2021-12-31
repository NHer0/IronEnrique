# Importing Modules

import config
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from time import sleep
from random import randint
from tqdm import tqdm
from IPython.display import IFrame

# Initialize SpotPy with user credentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.client_id,
                                                           client_secret= config.client_secret))


def get_playlist_tracks(username, playlist_id):
    
    results = sp.user_playlist_tracks(username,playlist_id,market="US")
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


def get_artists_from_track(track):
    return [artist["name"] for artist in track["artists"]]


def get_artists_ids_from_track(track):
    return [artist["id"] for artist in track["artists"]]


def get_artists_from_playlist(username, playlist_id):
    tracks_from_playlist = get_playlist_tracks(username, playlist_id)
    return list(set(artist for subset in [get_artists_from_track(track["track"]) for track in tracks_from_playlist] for artist in subset))


def get_artists_ids_from_playlist(username, playlist_id):
    tracks_from_playlist = get_playlist_tracks(username, playlist_id)
    return list(set(artist for subset in [get_artists_ids_from_track(track["track"]) for track in tracks_from_playlist] for artist in subset))


def spotify_player(song_id):
    track_id = song_id
    player = IFrame(src=f"https://open.spotify.com/embed/track/{track_id}",
             width="320",
             height="80",
             frameborder="0",
             allowtransparency="true",
             allow="encrypted-media",
            )
    return player

def get_audio_features_artists_db(artist_list):

    output_list = []

    # Load artist list (1,000 most streamed artists in Spotify)

    columns_names = ["artist", "song_name", "song_id", "danceability", 'energy', 'key', 'loudness', 
                 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness',
                 'valence', 'tempo'
                     ]
    
    for i, artist in enumerate(tqdm(artist_list)):
        
        # Creating a list of artists ids

        try:
            artist_id = sp.search(q=artist, type="artist", limit=1,market="US")["artists"]["items"][0]["id"]

        except IndexError:
            continue
        
        # API query for the 10 most popular songs of the artist      
        pop_tracks = sp.artist_top_tracks(artist_id, "US") 
        
        for j in range(len(pop_tracks["tracks"])):
            
            row = []
            row.append(artist_list[i])
            song_name = pop_tracks["tracks"][j]["name"]
            row.append(song_name)
            song_id = pop_tracks["tracks"][j]["id"]
            row.append(song_id)
            audio_f = sp.audio_features(song_id)
        
            for k in range(11):

                try:
                    key = list(audio_f[0].keys())[k]
                    row.append(audio_f[0][key])

                except AttributeError:
                    continue
            
            output_list.append(row)

        wait_time = randint(1, 15)/10
        sleep(wait_time)

    output = pd.DataFrame(output_list, columns=columns_names)

    return output
