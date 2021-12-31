# Importing Modules

from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

# Top 1000 most streamed artist chart url

url_spotify1000 = "https://chartmasters.org/most-streamed-artists-ever-on-spotify"

# Scrapping Function


def spotify1000_scrapper():

    artist_list = []

    # requesting and downloading the URL
    response = requests.get(url_spotify1000)

    # parsing the html  
    soup = BeautifulSoup(response.content, "html.parser")

    # looping the html code and storing the artist names

    for i in tqdm(range(1, 1001)):
    
        row = soup.select(f'tbody > tr:nth-child({i}) > td:nth-child(2)')
        artist_list.append(row[0].get_text())
    
    output = pd.DataFrame(artist_list, columns=["artist"])
    
    return output


