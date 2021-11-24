import requests
import pandas as pd
import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance

donation_id = "null"
donations = [float('inf')]
df = pd.DataFrame()
while len(donations) > 0:
  camp_url = "https://www.givesendgo.com/donation/recentdonations?camp=44611&donation=" + str(donation_id)
  res = scraper.get(url=camp_url)
  json = res.json()
  donations = json['returnData']['donations']
  donation_data = pd.DataFrame(donations)
  df = df.append(donation_data, ignore_index = True)
  donation_id = donations[-1]['donation_id'] if len(donations) > 0 else "null"
