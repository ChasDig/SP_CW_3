import pytest
from apps.dao.poster_and_comments_dao import PostersAndCommentsDAO

# Список ключей, которые должны быть у posters(data.json):
KEY_SHOULD_BE_POSTERS = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "tags", "pk"]

# Список ключей, которые должны быть у comments(comments.json):
KEY_SHOULD_BE_COMMENTS = ["post_id", "commenter_name", "comment", "pk"]


# Создаем fixture - экземпляр класса Posters_and_comments_DAO:
@pytest.fixture()
def posters_and_comments_DAO():
    posters_and_comments_DAO_instance = PostersAndCommentsDAO('./data/data.json', './data/comments.json')
    return posters_and_comments_DAO_instance


# Класс: проверяем класс PostersAndCommentsDAO:
class TestPostersAndCommentsDAO:

    # Тест: get_all_posters():
    def test_get_all_posters(self, posters_and_comments_DAO):
        test_all_posters = posters_and_comments_DAO.get_all_posters()
        assert type(test_all_posters) == list, "Ошибка, возвращается не список постов!"
        assert len(test_all_posters) > 1, "Ошибка, длина списка постов слишком мала!"
        assert set(test_all_posters[0].keys) == KEY_SHOULD_BE_POSTERS, "Ошибка, неверный список ключей постов!"

    # Тест: get_all_posters():
    def test_get_all_comments(self, posters_and_comments_DAO):
        test_all_comments = posters_and_comments_DAO.get_all_comments()
        assert type(test_all_comments) == list, "Ошибка, возвращается не список комментариев!"
        assert len(test_all_comments) > 0, "Ошибка, длина списка комментариев слишком мала!"
        assert set(test_all_comments[0].keys) == KEY_SHOULD_BE_COMMENTS, "Ошибка, неверный список ключей" \
                                                                         "комментариев!"

    # Тест: search_posters_by_users():
    def test_search_posters_by_users(self, posters_and_comments_DAO):
        test_search_posters_by_users_instance = posters_and_comments_DAO.search_posters_by_users("leo")
        assert type(test_search_posters_by_users_instance) == list, "Ошибка, возвращает не список постов пользователя!"
        assert len(test_search_posters_by_users_instance) > 0, "Ошибка, список постов пользователя слишком мал!"

    # Тест: search_posters_by_pk():
    def test_search_posters_by_pk(self, posters_and_comments_DAO):
        test_search_posters_by_pk_instance = posters_and_comments_DAO.search_posters_by_pk(1)
        assert type(test_search_posters_by_pk_instance) == dict, "Ошибка, возвращается не словарь поста пользователя!"
        assert len(test_search_posters_by_pk_instance) > 0, "Ошибка, длина поста пользователя слишком мала!"

    # Тест: get_comments_by_post_id():
    def test_get_comments_by_post_id(self, posters_and_comments_DAO):
        test_get_comments_by_post_id_instance = posters_and_comments_DAO.get_comments_by_post_id(1)
        assert type(test_get_comments_by_post_id_instance) == list, "Ошибка, возвращается не список комментариев поста!"
        assert len(test_get_comments_by_post_id_instance) > 0, "Ошибка, длина списка с комментариями поста мала!"
