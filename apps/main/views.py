import logging

from flask import Blueprint, render_template, jsonify
from apps.dao.poster_and_comments_dao import PostersAndCommentsDAO
from apps.dao.poster_and_comments_dao import Bookmarks

# Создаем Blueprint для main:
bp_main = Blueprint('main_blueprint', __name__, template_folder='template_main')

# Создаем экземпляр класса Posters_and_comments_DAO:
poster_and_comments = PostersAndCommentsDAO('./data/data.json', './data/comments.json')

# Создаем экземпляр класса Posters_and_comments_DAO:
bookmarks = Bookmarks('./data/data.json', './data/comments.json', './data/bookmarks.json')


# Создаем view для main_page:
@bp_main.route('/', methods=["GET", "POST"])
def main_page():
    # Получаем информацию обо всех постах:
    all_users = poster_and_comments.get_all_posters()
    # Получаем кол-во закладок:
    len_bookmarks = len(bookmarks.get_all_bookmarks())
    return render_template('index.html', users=all_users, len_bookmarks=len_bookmarks)


# Создаем view : передаем JSON-список всех постов через API-эндпоинт:
@bp_main.route('/api/posts/', methods=["GET", "POST"])
def api_posts_page():

    response = poster_and_comments.get_all_posters()
    # logger_one.info(f'Запрос к api/posts/')
    return jsonify(response)


# Создаем view : передаем JSON-список определенного поста (по post_id) через API-эндпоинт:
@bp_main.route('/api/posts/<post_id>', methods=["GET", "POST"])
def api_post_id_page(post_id):

    result_search = poster_and_comments.search_posters_by_pk(post_id)
    logger_one.info(f'Запрос к api/posts/{post_id}')
    return jsonify(result_search)


# Логирование для API:
# Создаем или получаем новый логгер:
logging.basicConfig(filename='./logs/api.log', level=logging.INFO)
logger_one = logging.getLogger('logger_one')

# Создаем обработчик логгера (указываем, что формат обработчика будет записывать логги в файл, и указываем файл):
logger_handler = logging.FileHandler(filename='./logs/api.log', mode='a', encoding='utf-8')

# Создаем формат обработки для логов:
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# Применяем форматирование к обработчику (выше):
logger_handler.setFormatter(formatter_one)

# Добавляем обработчик с форматированием к логгеру, созданному выше (в самом начале):
logger_one.addHandler(logger_handler)