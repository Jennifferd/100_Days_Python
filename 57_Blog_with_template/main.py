from flask import Flask, render_template
from post import Post
import requests

all_posts = requests.get("https://api.npoint.io/a840f823b3ced5b24d7a").json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:num>")
def show_post(num):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
