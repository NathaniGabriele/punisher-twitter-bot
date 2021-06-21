from lyrics import tweet_lyric
import tweepy
import os
import schedule
import time

API_KEY = os.environ['API_KEY']
API_SECRET_KEY = os.environ['API_SECRET_KEY']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']


# Twitter Authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

user = api.me()

def tweet():
    api.update_status(tweet_lyric) # post a tweet

# schedule the tweet 

schedule.every().day.at("15:03").do(tweet) #UTC time zome

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
