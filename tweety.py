import tweepy
import time,json

'''
Created on 10 Sep. 2017

@author: yuyao
'''
from config import account1

APP_KEY=account1[0]
APP_SECRET=account1[1]
OAUTH_TOKEN=account1[2]
OAUTH_TOKEN_SECRET=account1[3]

auth = tweepy.OAuthHandler(APP_KEY,APP_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)
firstTweet = api.user_timeline(screen_name="realDonaldTrump")[0]

# get the original tweet
original_tweet = firstTweet.retweeted_status


# iterate over retweets to get user id
for status in api.retweets(original_tweet):
    print(status.user.id)
