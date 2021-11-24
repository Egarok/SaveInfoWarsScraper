import requests
import pandas as pd
import cloudscraper

# URL to latest donation data
url = "https://www.givesendgo.com/donation/recentdonations?camp=44611&donation=null"

scraper = cloudscraper.create_scraper()

res = scraper.get(url=url)
data = res.json()
df = pd.DataFrame(data['returnData']['donations'])

# df_previous = pd.read_csv('data/saveinfowars-funding.csv', index_col=False)
# print(df_previous)


# write to data file
df.to_csv('data/saveinfowars-funding.csv', sep=',', index=False)

