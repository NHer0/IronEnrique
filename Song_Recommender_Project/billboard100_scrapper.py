# Importing Modules

from bs4 import BeautifulSoup
import requests
import pandas as pd

# Billboard url

url_billboard = "https://www.billboard.com/charts/hot-100"

# Billboard 100 Scrapping Function

def billboard100_scrapper():

    res = []
    columns = ["song", "artist", "last_week", "peak_pos", "n_weeks"]

    # requesting and downloading the URL
    response = requests.get(url_billboard)

    # parsing the html
    soup = BeautifulSoup(response.content, "html.parser")

    # storing the html code containing the top100 data in a variable
    rows = soup.select(".o-chart-results-list-row")

    # looping through the html code
    for row in rows:

        lst = row.get_text().split("\n") # get the content of the html code and store in a list (without \n)

        lst_clean = [string.lower() for string in lst if len(string) > 0] # clean the \n from the list

        if lst_clean[1] == "new": # special treatment for rows with a new comer

            res.append(lst_clean[3:-3])

        elif lst_clean[1] == "re-": # special treatment for rows with RE-ENTER

            res.append(lst_clean[5:-3])
        
        else:

            res.append(lst_clean[1:-3])

            
    output = pd.DataFrame(res, columns=["song", "artist", "last_week", "peak_pos", "n_weeks"]) # output DataFrame
    output["source"] = "billboard100"

    return output