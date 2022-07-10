from flask import Blueprint, render_template, request
from apps.dao.poster_and_comments_dao import PostersAndCommentsDAO

# Создаем Blueprint: bp_posts
bp_posts = Blueprint('bp_posts', __name__, template_folder='template_posts')

# Создаем экземпляр класса Posters_and_comments_DAO:
poster_and_comments = PostersAndCommentsDAO('./data/data.json', './data/comments.json')


# Создаем view : поиск постов по id:
@bp_posts.route('/posts/<postid>')
def get_single_poster(postid):

    # Получаем комментарии к посту, согласно postid:
    comments_by_post_from_poster_pk = poster_and_comments.get_comments_by_post_id(postid)

    # Получаем кол-во комментариев (считая длину вхождения в список комментариев):
    len_comments = len(comments_by_post_from_poster_pk)

    # Ищем нужный пост по его идентификатору(postid):
    poster_by_pk = poster_and_comments.search_posters_by_pk(postid)

    return render_template('post.html', comments=comments_by_post_from_poster_pk, len_comments=len_comments, poster=poster_by_pk)


# Создаем view : поиск постов по ключевому слову:
@bp_posts.route('/search/', methods=["GET"])
def search_page_by_word():

    # Получаем из кверри-параметра ключевое слово:
    args = str(request.args['s'])

    if args:

        # Ищем по ключевому слову все посты:
        all_posts_with_args = poster_and_comments.search_posters_by_args(args)

        # Получаем кол-во постов по ключевому слову:
        len_all_posts_with_args = len(all_posts_with_args)

        return render_template('search.html', posts_args=all_posts_with_args, len_posts_args=len_all_posts_with_args)

    else:
        return render_template('search.html')


# Функция: выводим все посты по тегу:
@bp_posts.route('/tag/<tagname>', methods=["GET", "POST"])
def search_page_by_tagname(tagname):

    all_poster_with_tagname = poster_and_comments.search_posters_by_tags(tagname)

    return render_template('user-feed.html', users=all_poster_with_tagname)
