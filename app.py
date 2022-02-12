from flask import Flask, render_template, request
from functions import get_data_from_json, get_post_by_pk, get_comment_by_id, search_for_posts, search_posts_by_user

app = Flask(__name__)


@app.route("/")
def main_paige():
    posts = get_data_from_json()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def post_paige(post_id):
    posts = get_post_by_pk(post_id)
    comments = get_comment_by_id(post_id)
    comment_counter = len(comments)

    return render_template("post.html", posts=posts, comments=comments, comment_counter=comment_counter)


@app.route("/search/")
def search_by_keyword():
    keyword = request.args.get("s")
    posts = search_for_posts(keyword)
    posts_count = len(posts)
    print(keyword)
    return render_template("search.html", posts=posts, posts_count=posts_count)


@app.route("/users/<username>")
def search_by_username(username):
    posts = search_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)



if __name__ == "__main__":
    app.run(debug=True)
