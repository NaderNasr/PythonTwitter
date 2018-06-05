from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import twitter

# app = Flask(__name__)
# Bootstrap(app)


# @app.route("/")
# def index():
#     return render_template('index.html')
# def hello():
#     return "Hello World! The server is AAAAlllliiiiivvveeeee"


# if __name__ == "__main__":
#     app.run(debug=True)

api = twitter.Api(consumer_key='3p6R5GffllmdOFwIQpMe5ZI6I',
                  consumer_secret='Nk4Z5pOGej6CVPD0Q5GPGLZOu6SLMibxjQZzaRMXvflrtwEL3W',
                  access_token_key='328208831-VFyiBf8qz7yYhSmQaxlefN8uw07i1Tf2g1YKHPlh',
                  access_token_secret='EFdGZQiGeCTyQawrWcx6ayPEN6Gn5T6MFkiG255ttXdHF')

generat = api.GetUserTimeline(screen_name="nader_nasr", count=100)


print(generat)
