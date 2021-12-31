# Import function get_audio_features_db()

import pandas as pd
import spotify_api as sp_api

# Load the artist list

artist_list = list(pd.read_csv(filepath_or_buffer="Data/artist_list.csv")["artist"])[0:3208]
                       

# Generate the db using get_audio_features_artist_db() and save into a csv file

output = sp_api.get_audio_features_artists_db(artist_list)
output.to_csv(path_or_buf="Data/audiofeatures_db.csv")
