import json


def get_posts_all():
    """ возвращает посты """

    with open("data/posts.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_posts_by_user(user_name):
    """– возвращает посты определенного пользователя.
    Функция должна вызывать ошибку `ValueError`
    если такого пользователя нет и пустой список,
    если у пользователя нет постов."""

    posts = get_posts_all()
    posts_by_user = []

    for post in posts:
        if post["poster_name"] == user_name:
            posts_by_user.append(post)

    return posts_by_user


def search_for_posts(query):
    """– возвращает список постов по ключевому слову"""

    posts = get_posts_all()
    matching_posts = []

    query_lower = query.lower()

    for post in posts:
        if query_lower in post["content"].lower():
            matching_posts.append(post)

    return matching_posts


def get_post_by_pk(pk):
    """ – возвращает один пост по его идентификатору."""

    posts = get_posts_all()

    for post in posts:
        if post['pk'] == pk:
            return post


def get_comments_all():
    with open("data/comments.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_comments_by_post_pk(pk):
    """"– возвращает комментарии определенного поста.
    Функция должна вызывать ошибку `ValueError`
    если такого поста нет и пустой список, если у
    поста нет комментов."""

    if pk < 1:
        return []

    comments = get_comments_all()
    comments_for_post = []

    for comment in comments:
        if comment["post_id"] == pk:
            comments_for_post.append(comment)

    return comments_for_post
