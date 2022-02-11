from flask import Flask, render_template, request
from functions import get_data_from_json,get_post_by_pk,get_comment_by_id

app = Flask(__name__)


@app.route("/")
def main_paige():
    posts = get_data_from_json()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:postid>")
def post_paige(postid):
    posts = get_post_by_pk(postid)
    comments = get_comment_by_id(postid)
    comment_counter = len(comments)
    print(comment_counter)
    return render_template("post.html", posts=posts, comments=comments, comment_counter=comment_counter)


app.run()
