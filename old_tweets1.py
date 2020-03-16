import tweepy as tw
import pandas as pd
import time
from main_preprocessor1 import *

consumer_key= 'MctWeB1kkWFZ3ZTidijQpIqpK'
consumer_secret= 'K5FCcROjU2r6jsn7pgiEvGMEqu5BotXwe4KV0aSdeWTAICVKme'
access_token= '1048952278961418240-0xijpR9vu3M84w7nBMGFds7FW2MmiJ'
access_token_secret= 'm0ha9dhwYbpHdHhT88ASySaNoAOhLbicKWqDBmTRWxZzp'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

def collect_tweets(word):

    search_words = word + " -filter:retweets"

    tweets = tw.Cursor(api.search,q=search_words,lang="en").items(100)


    tweets_details = [[tweet.text, tweet.user.location] for tweet in tweets]
    tweet_df = pd.DataFrame(data=tweets_details, 
                            columns=['text', "location"])
    main_df = preprocess_all(tweet_df)

    return main_df


