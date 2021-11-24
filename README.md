# Save Info Wars Scraper

[![scraper-saveinfowars](https://github.com/Egarok/SaveInfoWarsScraper/actions/workflows/scraper-saveinfowars.yml/badge.svg)](https://github.com/Egarok/SaveInfoWarsScraper/actions/workflows/scraper-saveinfowars.yml)

Record fundraising changes for Alex Jones' latest grift

https://saveinfowars.com/

---

The angry 🍅 Alex Jones

![Alex Jones](https://media.giphy.com/media/MDyUdNLYH2YHeHtCC7/giphy.gif)

Alex Jones found liable for Sandy Hook hoax lies

![Alex Jones Being Sued](https://media.giphy.com/media/kRiIx7abitgVq/giphy.gif)

Alex Jones after lawsuits

![Alex Jones after Lawsuits](https://media.giphy.com/media/1AgDOgXEBkhBOr9cTD/giphy.gif)

---

## Data Available (in /data)

`saveinfowars-donations-records.csv` : CSV that updates based on a routine cron job with GitHub Actions - should have most up to date data on donations

- using `scrape-saveinfowars.py`

`saveinfowars-donations-compiled.csv` : all SaveInfoWars donation data compiled as the starting file

- using `scrape-saveinfowars-csv-builder.py`

---

## Special Thanks for inspiring me to do this project

- [Knowledge Fight Podcast (where I discovered AJ was asking for donations)](https://podcasts.apple.com/us/podcast/knowledge-fight/id1192992870)
- [Behind the Bastards Podcast](https://podcasts.apple.com/us/podcast/behind-the-bastards/id1373812661)

## Resources

- [Save Info Wars GiveSendGo Fundraising Page](https://www.givesendgo.com/G2CK4)

---

- [Get Around Cloudflare Blocking with Cloudscraper](https://stackoverflow.com/questions/49087990/python-request-being-blocked-by-cloudflare)
- query I used: https://lmgtfy.app/?q=python+request+cloudflare

---

- [Blog Article on GitHub Actions cron job with Python](https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/)
- query I used: https://lmgtfy.app/?q=python+github+actions+cron

---