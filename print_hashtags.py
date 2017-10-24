import json

results = []

tweets_file = open('tweet_mining.json', "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue
 
for tweet in results:
    hashtags = tweet['entities']['hashtags']
    if not hashtags == []:
        print(hashtags) 
        
for tweet in results:
    hashtags = tweet['entities']['hashtags']
    for ht in hashtags:
        print(ht['text'])