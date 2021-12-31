# Importing

from kmeans_model import kmeans_model
import pandas as pd
import pickle

# Loading the audio features db

songs_db = pd.read_csv("Data/audiofeatures_db.csv", index_col=0)

# Build the model

kmeans_model, scaler, songs_db = kmeans_model(songs_db, n_clusters=20, n_init=20, tol=0)

# Save the database with the clusters
songs_db.to_csv("Data/audiofeatures_clustered_db.csv")

# Save the model and the scaler

with open("Data\kmeans_model.pickle", "wb") as f:
    pickle.dump(kmeans_model, f)

with open("Data\scaler.pickle", "wb") as f:
    pickle.dump(scaler, f)


