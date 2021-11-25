import cloudscraper
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.givesendgo.com/G2CK4"

# create CloudScraper Instance
scraper = cloudscraper.create_scraper()
page = scraper.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# grab total amount raised
total_amount_elements = list(set(soup.find_all('span', {"style": "font-weight:bold;color: #000;"})))

# Grab elements
total_amount_raised = total_amount_elements[0].get_text()
total_donations_elements = list(set(soup.find_all(class_='totalDonationCount')))
donations_count = total_donations_elements[0].get_text()
shares_count = total_donations_elements[1].get_text()
prayer_count = soup.find_all(id='praynowcount')[0].get_text()
updated_at = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

data = [str(total_amount_raised), str(donations_count), str(shares_count), str(prayer_count), updated_at]

# used for creating initial CSV
# header = ['total_amount_raised', 'donations_count', 'shares_count', 'prayers_count', 'updated_at']
# with open('saveinfowars-stats.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)

csv_filename = 'data/saveinfowars-stats.csv'
df = pd.read_csv(csv_filename, index_col=False)

# append new row of data to top
df.loc[-1] = data
df.index = df.index + 1
df.sort_index(inplace=True)

# write to data file
df.to_csv(csv_filename, sep=',', index=False)


