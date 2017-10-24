from flask import Flask, request
from flask import render_template
import os

app = Flask(__name__)

fake_news = ["A banana is a better President than an orange",
             "Fruit Declares War",
             "Meat Running Scared"]

@app.route("/")
def show_search_page():
    return render_template("search.html")

@app.route("/search")
def do_search():
    #q = request.args.get('query')
    # return "You searched for {0}".format(q)
    
    return render_template("results.html", headlines=fake_news)

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))