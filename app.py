import tweepy
from flask import Flask, render_template


app = Flask(__name__)


# Bootstrap(app)
@app.route("/")
# def hello():
#         return "Hello World! The server is AAAAlllliiiiivvveeeee"
def index():
    return render_template('index.html')


consumer_key = '3p6R5GffllmdOFwIQpMe5ZI6I'
consumer_secret = 'Nk4Z5pOGej6CVPD0Q5GPGLZOu6SLMibxjQZzaRMXvflrtwEL3W'
access_key = '328208831-VFyiBf8qz7yYhSmQaxlefN8uw07i1Tf2g1YKHPlh'
access_secret = 'EFdGZQiGeCTyQawrWcx6ayPEN6Gn5T6MFkiG255ttXdHF'


# Function to extract tweets
def get_tweets(username):

        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)

        # Calling api
        api = tweepy.API(auth)

        # number of tweets to be extracted
        number_of_tweets = 1

        tweets = api.user_timeline(screen_name=username)

        # Empty Array
        tmp=[]

        # create array of tweet information: username,
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
        for j in tweets_for_csv:

            # Push tweets to the empty array tmp
            tmp.append(j)

        # Printing the tweets
        print(tmp)


# Driver code
if __name__ == '__main__':

    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("ReBootKAMP")
