from flask import Flask, request, render_template

import utils

import logging



app = Flask(__name__)


@app.route('/')
def page_index():

    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_pk>')
def page_single_post(post_pk):

    post = utils.get_post_by_pk(post_pk)
    comments = utils.get_comments_by_post_pk(post_pk)
    comments_len = len(comments)

    return render_template("post.html", post=post, comments=comments, comments_len=comments_len)


@app.route('/search')
def page_search():

    query = request.args.get('s')
    if not query or query == "":
        return "Вы ничего не ищете"

    posts = utils.search_for_posts(query)
    posts_count = len(posts)

    return render_template("search.html", posts=posts, posts_count=posts_count, query=query)


@app.route('/users/<user_name>')
def page_user(user_name):

    posts = utils.get_posts_by_user(user_name)
    posts_count = len(posts)

    return render_template("user-feed.html", posts=posts, posts_count=posts_count, user_name=user_name)


@app.errorhandler(404)
def page_not_fount(error):
    return render_template('indexerror.html', title="Страница не найдена")


@app.route('/api/posts')
def api_posts():
    list_posts = utils.get_posts_all
    return list_posts()


@app.route('/api/posts/<int:post_id>')
def api_post(post_id):
    one_post = utils.get_post_by_pk(post_id)
    return one_post


app.run()


logging.basicConfig(level=logging.INFO, filename="logs/py_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("An INFO")

