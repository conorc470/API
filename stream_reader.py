import json

results = []

tweets_file = open('tweet_mining.json', "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue
 
print(len(results))