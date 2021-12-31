# Importing Modules

from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

#  url

url_rolling500 = "https://rocknyc.live/rolling-stones-latest-top-500-greatest-songs-of-all-time-list-bye-bye-boomer-bye-bye.html"


# Scrapping Function

#def rolling500_scrapper():

output = []
columns = ["song", "artist", "last_week", "peak_pos", "n_weeks"]

# requesting and downloading the URL
response = requests.get(url_rolling500)

# parsing the html
soup = BeautifulSoup(response.content, "html.parser")

# storing the html code containing the top100 data in a variable

parent = "#content-area > div > div.fl-row-content.fl-row-fixed-width.fl-node-content > div.fl-col-group.fl-node-60b776b9d45a1 > div.fl-col.fl-node-60b776b9d45a2 > div > div.fl-module.fl-module-fl-post-content.fl-node-60b776b9d45a3.post-content > div"
children = parent + " > p:nth-child(84)"

t = soup.select(children)

for i in tqdm(range(84,584)):
    
    row = soup.select(parent + f' > p:nth-child({i})')
    output.append(row[0].get_text())





