import tweepy


consumer_token = '3p6R5GffllmdOFwIQpMe5ZI6I'
consumer_secret = 'Nk4Z5pOGej6CVPD0Q5GPGLZOu6SLMibxjQZzaRMXvflrtwEL3W'
access_token = '328208831-VFyiBf8qz7yYhSmQaxlefN8uw07i1Tf2g1YKHPlh'
access_token_secret = 'EFdGZQiGeCTyQawrWcx6ayPEN6Gn5T6MFkiG255ttXdHF'

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
