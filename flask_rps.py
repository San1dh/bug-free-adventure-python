# works on VScode, connection error on Replit

from flask import Flask, render_template
import random
# from replit.web import App

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/data")
def data():
    x = random.randrange(0, 3)
    
    return (
    
        {"result" : "rock"}
        if(x == 0)
        else
        {"result": "paper"}
        if(x == 1)
        else
        {"result" : "scissors"}
        if(x == 2)
        else
        {"error" : "none"}
    )

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='8080', debug=True)
