import tweepy
from textblob import TextBlob

#checks if the twitter is positive or not
def get_label(analysis,threshold = 0):
    if(analysis.sentiment[0]>threshold):
        return 'Positive'
    else:
        return 'Negative'

#get consumer and access token key from app.twitter.com
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

#authenticate using tweepy
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#searching tweets
public_tweets = api.search('Trump',count = 100,since = '2019-1-1',until = '2019-10-20')

#creating a tweets.csv file 
with open('tweets.csv', 'a+') as tweet_file:
    tweet_file.write('tweet,label\n')
    #traversing through tweets which is searched above
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        #checking the label and writing on file
        tweet_file.write('%s%s\n' % (tweet.text.encode('utf8'),get_label(analysis)))
        
