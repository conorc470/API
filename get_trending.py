import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '1lcxZ8FNcSj7FfSIqqgybYMyK'
CONSUMER_SECRET = 'NEaZcJ26T6O6i8BJcr6rQ3F4t7IvdUzy3Mff7hsZ2Mnqi3Qs1W'
OAUTH_TOKEN = '921001241467064321-zj9SdXBH2oGFmS0DxmCRt7vJfo7vurZ'
OAUTH_TOKEN_SECRET = 'xrwTg4QMXLlr02pGnbjF63rXubux3D49giHmvCO8VgmKc'

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)

api = get_api()


DUB_WOE_ID = 560743

dub_trends = api.trends_place(DUB_WOE_ID)

print (json.dumps(dub_trends, indent=1))