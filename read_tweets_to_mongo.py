from tweepy import Stream
from tweepy.streaming import StreamListener
from pymongo import MongoClient
from auth import get_auth, MONGODB_URI
import json

keyword_list=['brexit']
limit = 10

DBS_NAME = "tweets"
COLLECTION_NAME = "richardadalton"


class MyStreamListener(StreamListener):

    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with MongoClient(MONGODB_URI) as conn:
                    collection = conn[DBS_NAME][COLLECTION_NAME]
                    tweet = json.loads(data)
                    collection.insert_one(tweet)
                    return True
            except BaseException as e:
                print ("Failed on_data: %s" % str(e))
            return True
        else:
            return False

    def on_error(self, status):
        print(status)
        return True

auth = get_auth()

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)