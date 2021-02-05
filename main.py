from flask import Flask, render_template, request
import requests
import smtplib

all_posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

OWN_EMAIL = "EMAIL ADDRESS"
OWN_PASSWORD = "EMAIL PASSWORD"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


@app.route("/post/<num>")
def go_post(num):
    num_to_int = int(num)
    requested_post = None

    for post in all_posts:
        if post["id"] == num_to_int:
            requested_post = post

    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
