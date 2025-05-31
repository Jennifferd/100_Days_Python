from flask import Flask, render_template, request
from email.message import EmailMessage
import requests
import smtplib

my_email = YOUR_EMAIL
password = YOUR_PASSWORD
all_posts = requests.get("https://api.npoint.io/cf2a8491048ad73da9d4").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        msg = EmailMessage()
        msg['Subject'] = "Contact form"
        msg.set_content(f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(my_email, EMAIL_TO, msg.as_string())
        return render_template("contact.html", text="Successfully sent your message" )
    return render_template("contact.html", text="Contact Me")


@app.route('/post/<int:num>')
def show_post(num):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
