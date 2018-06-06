import sys
import csv

#http://www.tweepy.org/
import tweepy

consumer_key = '3p6R5GffllmdOFwIQpMe5ZI6I'
consumer_secret = 'Nk4Z5pOGej6CVPD0Q5GPGLZOu6SLMibxjQZzaRMXvflrtwEL3W'
access_key = '328208831-VFyiBf8qz7yYhSmQaxlefN8uw07i1Tf2g1YKHPlh'
access_secret = 'EFdGZQiGeCTyQawrWcx6ayPEN6Gn5T6MFkiG255ttXdHF'


#method to get a user's last 100 tweets
def get_tweets(username):

    #http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #set count to however many tweets you want; twitter only allows 200 at once
    number_of_tweets = 100

    #get tweets
    tweets = api.user_timeline(screen_name = username,count = number_of_tweets)

    #create array of tweet information: username, tweet id, date/time, text
    tweets_for_csv = [[username,tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

    #write to a new csv file from the array of tweets
    print "writing to {0}_tweets.csv".format(username)
    with open("{0}_tweets.csv".format(username) , 'w+') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerows(tweets_for_csv)


        #if we're running this as a script
        if __name__ == '__main__':

            #get tweets for username passed at command line
            if len(sys.argv) == 2:
                get_tweets(sys.argv[1])
            else:
                print "Error: enter one username"

                #alternative method: loop through multiple users
                # users = ['user1','user2']

                # for user in users:
                get_tweets('AugmentedReality')
