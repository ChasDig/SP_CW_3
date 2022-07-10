from flask import Blueprint, redirect, render_template
from apps.dao.poster_and_comments_dao import Bookmarks


# Создаем Blueprint: bp_bookmarks
bp_bookmarks = Blueprint('bp_bookmarks', __name__, template_folder='template_bookmarks')

# Создаем экземпляр класса Posters_and_comments_DAO:
bookmarks = Bookmarks('./data/data.json', './data/comments.json', './data/bookmarks.json')


# Функция: добавляем пост в закладки:
@bp_bookmarks.route('/bookmarks/add/<pk_post>', methods=["GET", "POST"])
def bookmarks_page(pk_post):

    bookmarks.put_post_in_bookmarks_json(pk_post)

    return redirect("/", code=302)


# Функция: переходим на страницу с закладками:
@bp_bookmarks.route('/bookmarks/')
def bookmarks_pages():

    # Список всех закладок:
    all_bookmarks = bookmarks.get_all_bookmarks()
    len_bookmarks = len(all_bookmarks)

    return render_template('bookmarks.html', bookmarks=all_bookmarks)


# Функция: удаление постов:
@bp_bookmarks.route('/bookmarks/adds/<pk_post>', methods=["GET", "POST"])
def bookmarks_remove_page(pk_post):

    # Удаляем пост из json-файла со списком закладок:
    delete_post = bookmarks.delet_post_in_bookmark(pk_post)

    return redirect("/bookmarks/", code=302)
