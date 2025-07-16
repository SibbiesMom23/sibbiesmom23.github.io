# tweet_scheduler.py

import tweepy
import time

# Twitter API credentials – replace with your actual credentials
API_KEY = 'RkYmWcYggT2knzbyxy6dVJSX9'
API_SECRET = 'qR5lBOXcZPI0dCtSwujrUO8eBfdRSL2FJjtmk88ElpZDVVXOAy'
ACCESS_TOKEN = '842922986-luHSpYNUvy5QOT8JZ0VMMCE4TfrPZ7JeWXR6tNfL'
ACCESS_SECRET = 'CsiPfx9XAaBJSaE5CI96DRT64UxCD1VLy7Bu7VFgwXJ0I'

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def read_tweets(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def post_tweets(tweets, delay_seconds=120):
    for tweet in tweets:
        try:
            api.update_status(tweet)
            print(f"✅ Tweeted: {tweet}")
        except Exception as e:
            print(f"❌ Error: {e}")
        time.sleep(delay_seconds)

if __name__ == "__main__":
    tweets = read_tweets('tweets.txt')
    print(f"Loaded {len(tweets)} tweets.")
    post_tweets(tweets)
