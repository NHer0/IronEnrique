# Importing Modules

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from tqdm import tqdm
import pickle


def kmeans_model(songs_db, n_clusters=6, n_init=20, tol=0):
    # Selecting the features and scaling them

    audiofeatures = songs_db.iloc[:, 3:]
    scaler = StandardScaler()
    scaler.fit(audiofeatures)
    X_scaled = scaler.transform(audiofeatures)
    audiofeatures_scaled = pd.DataFrame(X_scaled, columns=audiofeatures.columns)

    # Clustering the songs with the audio features

    kmeans = KMeans(n_clusters=n_clusters
                    , random_state=0
                    , n_init=n_init
                    , tol=tol
                    , algorithm="elkan"
                    , init="k-means++"
                    )

    kmeans.fit(audiofeatures_scaled)
    songs_db["cluster"] = kmeans.labels_

    return kmeans, scaler, songs_db
