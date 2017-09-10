import json
from application_only_auth import Client
from config import*


# The consumer secret is an example and will not work for real requests
# To register an app visit https://dev.twitter.com/apps/new
CONSUMER_KEY = account1[0]
CONSUMER_SECRET = account1[1]

client = Client(CONSUMER_KEY, CONSUMER_SECRET)

# Pretty print of tweet payload
tweet = client.request('https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640')


# Show rate limit status for this application
status = client.rate_limit_status()
print (status['resources']['statuses']['/statuses/retweeters/ids'])