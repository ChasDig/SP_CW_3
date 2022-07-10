import pytest
from main import app


def test_api_posts():

    keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "tags", "pk"}
    response = app.test_client().post('/api/posts/')
    print(type(response.data))
    assert type(response.json) == list, 'Запрос: /api/posts. Возвращается не список!'
    assert set(response.json[0].keys()) == keys, 'Запрос: /api/posts. Список ключей не верный!'


def test_api_post_id_page():

    keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "tags", "pk"}
    response = app.test_client().post('/api/posts/1')
    print(type(response.data))
    assert type(response.json) == dict, 'Запрос: /api/posts/1. Возвращается не словарь!'
    assert set(response.json.keys()) == keys, 'Запрос: /api/posts/1. Список ключей не верный!'
