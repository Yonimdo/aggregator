import tweepy
import pandas as pd
import secret
from pprint import pprint

pd.options.display.max_columns = 50
pd.options.display.max_rows = 50
pd.options.display.width = 120

if not secret.TWI_TOKEN:
    secret.TWI_TOKEN = tweepy.OAuthHandler(consumer_key=secret.API_KEY, consumer_secret=secret.API_SECRET)

api = tweepy.API(secret.TWI_TOKEN)

results = api.search(q="yairlapid")

pprint(results)
