from ensurepip import bootstrap
import tweepy
import time
from confluent_kafka import Producer
from faker import Faker                     # Create dummy data
import json
import time
import logging
import random
import pandas as pd

api_key ="esbTFosPhgM5aM3qR6u6XlaKt"
api_secret ="egsaXsdI45Eu5XoU09tY4KyYj9A40uTLXHLYDRsotKeZhyw1l7"
bearer_token =r"AAAAAAAAAAAAAAAAAAAAACVShwEAAAAAXO6MzFXiHTB7e5xzT88e5%2Bvrga0%3DRxjRKlO0lYmlTgyXX643tWDvQDsab004DF0AmCXVQEURhwS1eA"
access_token ="1577563364619735041-vCeuegMZxH6dEdhcnpYf5bPlhiUpLE"
access_token_secret="jzEQng6OnusDqyMdA4OFGvZ8F9HpItX3O2j0GnB3GuCJz"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
user = 'Jokowi'
limit=300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)