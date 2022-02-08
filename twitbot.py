import configparser
CONFIG = configparser.ConfigParser()
CONFIG.read('credentials.ini')

from TwitterSearch import TwitterSearch, TwitterSearchOrder, TwitterSearchException

tso = TwitterSearchOrder()
tso.set_keywords(['election'])
tso.set_language('en')
tso.set_include_entities(False)
tFeeds=[]
    try:
        #tuo = TwitterUserOrder(username) # create a TwitterUserOrder
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([username])
        tso.set_language('en')
        tso.set_count(50)
        tso.set_include_entities(False)
        tso.set_until(date.today()-timedelta(days=2))


ts = TwitterSearch(access_token=CONFIG['DEFAULT']['access_token'], #your access token
            access_token_secret=CONFIG['DEFAULT']['access_token_secret'], #your access token secret
            consumer_key=CONFIG['DEFAULT']['consumer_key'], #your consumer key
            consumer_secret=CONFIG['DEFAULT']['consumer_secret']) # your consumer secret

results = []
for tweet in ts.search_tweets_iterable(tso):
    results.append(tweet)



print(results[0])