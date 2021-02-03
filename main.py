from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
all_posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route("/post/<num>")
def go_post(num):
    num_to_int = int(num)
    requested_post = None

    for post in all_posts:
        if post["id"] == num_to_int:
            requested_post = post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
