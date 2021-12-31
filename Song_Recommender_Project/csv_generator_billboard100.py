# Import function billboard100_scrapper()

from billboard100_scrapper import billboard100_scrapper

# Scrap Billboard 100 and save the data into a csv_file

output = billboard100_scrapper()
output.to_csv(path_or_buf="Data/billboard100.csv")