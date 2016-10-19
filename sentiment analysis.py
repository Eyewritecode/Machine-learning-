import tweepy as tweety
import csv
from textblob import TextBlob

consumer_key        = "xXgGzFe8PyWOoD7x1T2KB0sB9"
consumer_secret     = "VLZRK2QstddIELeCcwzvb0zapo5Nx8zadcCWjv9mbE2ogGgHRJ"
access_token        = "51032036-L0Af231f8X2JCjcaWNscPK7Cxd2ZHdLqI0fH1CV5f"
access_token_secret = "YxBJtKc2KBgnUunc8kVNZSD9rdsWkyXum4zg2eJOd69X6"

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