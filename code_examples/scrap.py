import json
import reactivex as rx
from reactivex import operators as ops
import tweepy


# Twitter API authentication
import tweepy

api_key = consumer_key
api_secret_key = consumer_secret
# access_token =  # access_token
# access_token_secret =  # access_token_secret
# authorize the API Key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)
# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)
# call the api
api = tweepy.API(authentication)

# Streaming tweets from user timeline

user = "AnalyticsVidhya"
public_tweet = api.user_timeline(id=user, count=5)

for tweet in public_tweet:
    print("-->", tweet.text)
