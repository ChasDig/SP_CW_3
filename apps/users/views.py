from flask import Blueprint, render_template
from apps.dao.poster_and_comments_dao import PostersAndCommentsDAO

# Создаем Blueprint: bp_posts
bp_users = Blueprint('bp_users', __name__, template_folder='template_users')

# Создаем экземпляр класса Posters_and_comments_DAO:
poster_and_comments = PostersAndCommentsDAO('./data/data.json', './data/comments.json')



# Ищем пользователя по его имени:
@bp_users.route('/users/<username>', methods=["GET", "POST"])
def post_get_users(username):

    # Получаем все посты определенного пользователя по его имени:
    get_all_posters_users = poster_and_comments.search_posters_by_users(username)


    return render_template('user-feed.html', users=get_all_posters_users)
