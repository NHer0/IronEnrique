# Import function get_audio_features_db()

import pandas as pd
import spotify_api as sp_api

# Artist List

# Top1000 most streamed artists

artist_list = list(pd.read_csv(filepath_or_buffer="Data/spotify1000.csv")["artist"])

# Playlists

playlist_list = [("Mariannne Vossy", "2iBH9S3UXlrtUBxjffgZEh") # best hits since the 80s top1000
                ,("phil347stoner", "04ryCYgHr0d36qPXQTgeLD")   # best rock songs top1000
                ,("Spotify", "37i9dQZF1DXcBWIGoYBM5M")         # Spotify's Today's Top Hits
                ,("Armada Music", "68BiK8KG3otORDaYB3ZaO9")    # Chill Out top1000
                ,("Tomorrowland", "1mB0DBalm5cTnkoi8yDFul")    # Tomorrowland top1000
                #,("Armada Music", "5hrcDyMev3xAONUyx68cgS")    # Deep House Top1000
                ,("Armada Music", "4VXFwpNvQysB8yS6E2t2ls")    # House Top1000
                ,("Liquicity", "4EzbaJ4cpc1DN1Cht6Jg3q")       # Drum and Bass Top1000
                ,("Isidro Muñoz", "7qvZykTVPjvEX2LCcXoHog")    # Ultimate Classical Music
                ,("Spotify", "37i9dQZF1DXbITWG1ZJKYt")         # Jazz Classics
                #,("swisher509", "5S2P5NSWBY2ccuPjroEA6t")      # Trap Rap
                #,("katerina", "4gdyJJFph3i2oMdpRnCONw")        # Rap 2016-2021
                ,("jasper_van_loon", "7BDUphylF8dfPKFo9Tvdr9") # Blues, soul, jazz               
                ,("Justin E. Miller", "5KUiUIqJgTcrL1676wgwnt") # Country
                ]



for i in range(len(playlist_list)):
    
    artist_list = list(set(artist_list
                  + sp_api.get_artists_from_playlist(playlist_list[i][0], playlist_list[i][1])
                  ))
    
                       
output_df = pd.DataFrame(artist_list, columns=["artist"])
output_df.to_csv(path_or_buf="Data/artist_list.csv")
