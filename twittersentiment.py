import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
        

root= tk.Tk()
  
canvas1 = tk.Canvas(root, width = 800, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='Twitter Sentiment Analysis')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)
   
label2 = tk.Label(root, text='This application allows you to see how people react to a particular event or "hashtag" on Twitter')
label2.config(font=('Arial', 14))
canvas1.create_window(400, 100, window=label2) 
  
entry1 = tk.Entry (root)
canvas1.create_window(400, 120, window=entry1) 
          
 
  
def create_charts():
    global x1
    x1 = entry1.get()
    abc(x1)
    text = tk.Text(root)
    text.insert(tk.INSERT,finaltextpos)  
    text.insert(tk.END,finaltextneg)  
    text.pack(side=tk.LEFT)

      
    figure2 = Figure(figsize=(4,3), dpi=100) 
    subplot2 = figure2.add_subplot(111) 
    labels2 =  'Positive','Negative', 'Neutral' 
    pieSizes = [positive,negative,neutral]
    my_colors2 = ['green','red','gray']
    explode2 = ( 0,0.1, 0)  
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) 
    subplot2.axis('equal')  
    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().pack()

            
button1 = tk.Button (root, text=' Calculate ',command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 180, window=button1)


button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 260, window=button3)
 
root.mainloop()