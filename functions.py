import json
from os.path import isfile

DATA_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"


def get_data_from_json():
    """Функция для распаковки JSON-файла с постами и данными юзера
    возвращает список словарей со всеми постами.
    """
    if isfile(DATA_PATH):
        with open(DATA_PATH, encoding="utf-8") as file:
            return json.load(file)
    else:
        print("Файл не найден")
        return {}


def get_comments_from_json():
    """Функция для распаковки JSON-файла с комментариями
    возвращает список словарей со всеми комментариями.
    """

    if isfile(COMMENTS_PATH):
        with open(COMMENTS_PATH, encoding="utf-8") as file:
            return json.load(file)
    else:
        print("Файл не найден")
        return {}


def get_post_by_pk(pk):
    """Функция для получения постов по идентификатору, возвращает список словарей
     с данными соответствующими указанному идентификатору
    """
    posts = get_data_from_json()
    user_data = []

    for post in posts:
        if pk == post["pk"]:
            user_data.append(post)
    return user_data


def get_comment_by_id(post_id):
    """Функция для получения комментариев к постам по идентификатору, возвращает список словарей
    с комментариями соответствующими указанному идентификатору
    """
    comments = get_comments_from_json()
    user_comments = []

    for comment in comments:
        if post_id == comment["post_id"]:
            user_comments.append(comment)
    return user_comments


def search_for_posts(query):
    """Функция для поиска постов по ключевому слову, возвращает список словарей с постами ,
    содержащими ключевое слово
    """
    posts = get_data_from_json()
    posts_list = []
    word = query

    if word:
        s = word.lower()
        posts_list = [x for x in posts if s in x.get("content").lower()]
    return posts_list


def search_posts_by_user(username):
    """Функция для поиска постов по автору, возвращает список словарей с постами ,
    принадлежащими указанному автору
    """
    posts = get_data_from_json()
    user_posts = []

    for post in posts:
        if username == post["poster_name"]:
            user_posts.append(post)
    return user_posts
