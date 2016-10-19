import tweepy as tweety
import csv
from textblob import TextBlob

consumer_key        = "###"
consumer_secret     = "###"
access_token        = "###"
access_token_secret = "###"

auth = tweety.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweety.API(auth)
public_tweets = api.search('Rwanda')
sentiment= ""
with open("data.csv", "w") as file:
	data = csv.writer(file)
	data.writerow(("Tweet", "Sentiment"))
	for tweet in public_tweets:
		#print(tweet.text)
		analysis = TextBlob(tweet.text)
		#print (analysis)
		if analysis.sentiment.polarity > 0.2:
			sentiment = "Positive" 
		else:
			sentiment = "Negative"
		 #print(analysis.sentiment)
		data.writerow((tweet.text.encode('UTF-8'), sentiment))