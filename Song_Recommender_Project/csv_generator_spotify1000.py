# Import function spotify1000_scrapper()

from spotify1000_scrapper import spotify1000_scrapper

# Scrap url and store in a csv file the top 1000 most streamed artists in Spotify

output = spotify1000_scrapper()
output.to_csv(path_or_buf="Data/spotify1000.csv")
