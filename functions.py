import json
from os.path import isfile

DATA_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"


def get_data_from_json():
    if isfile(DATA_PATH):
        with open(DATA_PATH, encoding="utf-8") as file:
            return json.load(file)
    else:
        print("Файл не найден")
        return {}


def get_comments_from_json():
    if isfile(COMMENTS_PATH):
        with open(COMMENTS_PATH, encoding="utf-8") as file:
            return json.load(file)
    else:
        print("Файл не найден")
        return {}


def get_post_by_pk(pk):
    posts = get_data_from_json()
    user_data = []

    for post in posts:
        if pk == post["pk"]:
            user_data.append(post)
    return user_data


def get_comment_by_id(post_id):
    comments = get_comments_from_json()
    user_comments = []

    for comment in comments:
        if post_id == comment["post_id"]:
            user_comments.append(comment)
    return user_comments

# `search_for_posts(query)` – возвращает список словарей по вхождению query
#
# `get_post_by_pk(pk)`

#
# print(get_posts_by_user(3))
#
#
# def get_post_by_tag(tag):
#     posts = get_posts_from_json()
#     tag_match = f'#{tag}'
#     posts_list = []
#
#     for post in posts:
#         if tag_match in post["content"]:
#             posts_list.append(post)
#     return posts_list
#
#
# def get_all_tags_from_str(string):
#     tags = set()
#
#     for word in string.split(' '):
#         if word.startswith('#'):
#             tags.add(word[1:])
#
#     return tags
#
#
# def get_all_tags_from_posts():
#     posts = get_posts_from_json()
#     tags = set()
#
#     for post in posts:
#         post_content = post.get('content')
#         tag_in_posts = get_all_tags_from_str(post_content)
#         tags = tags.union(tag_in_posts)
#
#     return tags
