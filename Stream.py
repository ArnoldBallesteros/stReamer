import tweepy
import csv
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

CONSUMER_KEY = '9CmniCaIWNrMOs39KnYOdRvlo'
CONSUMER_SECRET = 'AlowiR8XLqmpZqgSBj7SI0eRaEd3bixbt9ecGP925RYCy5yzhe'
TOKEN = '1176891456-p1FquDzrgp3PJWdwzxZwHosHQtNlXwB3ngjCy1E'
TOKEN_SECRET = 'rkERNpUqKHXcB87fQ5SvFeSGBiFvpOswP49e6ItBAS3fP'

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)
api = tweepy.API(auth)
#print(api.rate_limit_status())


class MyStreamListener(StreamListener):
	
	def on_status(self, status):
		print(status.text)

	def on_error(self, status_code):
		print(status_code)
		if status_code == 420:
			print("Disconnected")
			return False

termList = []

with open('term.csv') as f:
	terms = csv.reader(f, delimiter = ' ')
	for row in terms:
		for word in terms:
				termList.extend(word)
	#	termList.replace(",","")
blockList = [x.replace(',', '') for x in termList]
print(blockList)
blockString = ''.join(blockList)

		
myStreamListener = MyStreamListener()
mystream = Stream(api.auth, myStreamListener)

mystream.filter(track='HACKRPI', async = True)
