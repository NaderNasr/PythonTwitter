from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


consumer_key = '3p6R5GffllmdOFwIQpMe5ZI6I'
consumer_secret = 'Nk4Z5pOGej6CVPD0Q5GPGLZOu6SLMibxjQZzaRMXvflrtwEL3W'
access_key = '328208831-VFyiBf8qz7yYhSmQaxlefN8uw07i1Tf2g1YKHPlh'
access_secret = 'EFdGZQiGeCTyQawrWcx6ayPEN6Gn5T6MFkiG255ttXdHF'


class listener(StreamListener):
# count = 0
    def on_data(self, data):

        # if(count<10):
            # count++;
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print(tweet+"\n")
            savefile = str(time.time())+"::"+tweet
            save = open('twitterDB4.csv', 'a')
            save.write(savefile)
            save.write("\n\n")
            save.close()
            return(True)

    def on_error(self, status):
        print (status)


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['AugmentedReality'])
