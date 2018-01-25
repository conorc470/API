from auth import get_api

api = get_api()

GLA_WOE_ID = 21125
LON_WOE_ID = 44418
 
 
gla_trends = api.trends_place(GLA_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

print(gla_trends)

gla_trends_set = set([(trend['name'], trend['tweet_volume']) for trend in gla_trends[0]['trends']])

print(gla_trends_set)