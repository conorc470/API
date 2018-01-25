import json
import tweepy
from auth import get_api

api = get_api()

def get_by_search(query, count):
    return tweepy.Cursor(api.search, q=query).items(count)

def get_my_timeline(count):
    return tweepy.Cursor(api.home_timeline).items(count)

tweets = get_by_search("Storm Brian", 10)


for tweet in tweets:
    print(type(tweet))


# json_strings = json.dumps([tweet._json for tweet in tweets] )


# with open("brian.json", "w") as f:
#     f.write(json_strings)


# for tweet in tweets:
#     with open("brian.json", "a") as f:
#         f.write(json.dumps(tweet._json))
#         f.write("\n")