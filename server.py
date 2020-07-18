
from flask import Flask
from flask import request,render_template
app=Flask(__name__)


import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import json

positive=0
negative=0
neutral=0
ptweets=0
ntweets=0
tweets=0
finaltextpos=""
finaltextneg=""

class TwitterClient(object):
    def __init__(self):
        consumer_key = 'SrswKRiDO5hvjbhVQpJEkv4ek'
        consumer_secret = 'fGUfsVnFesk7RaaQ7MYzGE9LUaMEW7TOkxClnYcEWSrjBSjqUc'
        access_token = '1210145731085914118-h9IgCKPLpGpIhQEei4IBPweZFxbONm'
        access_token_secret = 'UgBQlVMRCwWnrhCfdVzaYA3npKajxcgNAY1eyu6VgKjy7'
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        global positive
        global negative
        global neutral
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            positive=positive+1
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            neutral=neutral+1
            return 'neutral'
        else:
            negative=negative+1
            return 'negative'

    def get_tweets(self, query, count = 10):
        tweets = []
        try:
            fetched_tweets = self.api.search(q = query, count = count)
            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
            return tweets
        except tweepy.TweepError as e:
            print("Error : " + str(e))

def abc(text):
    global ptweets
    global ntweets
    global tweets
    global finaltextpos
    global finaltextneg
    api = TwitterClient()
    tweets = api.get_tweets(query = text, count = 500)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    finaltextpos="Positive tweets:\n\n"
    print()
    for tweet in ptweets[:10]:
        finaltextpos+=tweet['text']+"\n"
    finaltextneg="\n\nNegative tweets:\n\n"
    print()
    for tweet in ntweets[:10]:
        finaltextneg+=tweet['text']+"\n"


@app.route("/",methods=["POST"])
def hello():
    global positive
    global negative
    global neutral
    positive=0
    negative=0
    neutral=0
    text=request.get_data()
    #text=request.form["name"]
    #data=request.get_json()
    #text=data['name']
    abc(text)
    x={"positive":positive,"negative":negative,"neutral":neutral,"finaltextneg":finaltextneg,"finaltextpos":finaltextpos}
    y=json.dumps(x)
    return(str(y))

