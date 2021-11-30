import requests
import pandas as pd
import cloudscraper

# URL to latest donation data
url = "https://www.givesendgo.com/donation/recentdonations?camp=44611&donation=null"

# returns a CloudScraper instance
scraper = cloudscraper.create_scraper()

res = scraper.get(url=url)
data = res.json()
donations_data = data['returnData']['donations']
df_recent = pd.DataFrame(donations_data)

csv_filename = 'data/saveinfowars-donations-records.csv'

df_compiled = pd.read_csv(csv_filename, index_col=False)

for index, row in df_recent.iterrows():
    if row['donation_id'] not in df_compiled['donation_id'].tolist():
        # source: add row to top of DataFrame (optimize later?)
        # https://stackoverflow.com/questions/43408621/add-a-row-at-top-in-pandas-dataframe

        df_compiled.loc[-1] = row # add new row
        df_compiled.index = df_compiled.index + 1 # shift index
        df_compiled.sort_index(inplace=True)

# write to data file
df_compiled.to_csv(csv_filename, quotechar="", sep=',', index=False)

