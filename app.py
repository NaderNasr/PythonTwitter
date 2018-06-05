from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
# def hello():
#     return "Hello World! The server is AAAAlllliiiiivvveeeee"


Bootstrap(app)


if __name__ == "__main__":
    app.run(debug=True)
