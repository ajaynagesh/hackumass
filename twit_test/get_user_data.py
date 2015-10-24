from ConfigParser import SafeConfigParser
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

parser = SafeConfigParser()
parser.read('config.ini');

access_token = parser.get("user_auth", "access_token")
access_token_secret = parser.get("user_auth", "access_token_secret")
consumer_key = parser.get("user_auth", "consumer_key")
consumer_secret = parser.get("user_auth", "consumer_secret")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def timeline_tweets(username):
    """ Gets timeline tweets based on user information """
    print "User = " , username
    public_tweets = api.home_timeline(screen_name = username, count = 200)
    for tweet in public_tweets:
        print tweet.text


timeline_tweets("AarshPatel")
