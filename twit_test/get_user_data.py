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
def timeline_tweets(username):
    """ Gets timeline tweets based on user information """
    user = tweepy.get_user(username)
    print(user.screen_name + "has " + user.followers_count + " followers")

timeline_tweets("AarshPatel")
