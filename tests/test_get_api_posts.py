import pytest
import application

KEYS = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "tags", "pk"}


def test_api_posts():

    response = application.app.test_client().get('/api/posts/', follow_redirects=True)
    assert response.status_code == 200, "Error!"
    assert type(response.json) == list, 'Запрос: /api/posts. Возвращается не список!'
    assert set(response.json[0].keys()) == KEYS, 'Запрос: /api/posts. Список ключей не верный!'


def test_api_post_id_page():

    response = application.app.test_client().post('/api/posts/1')
    print(type(response.data))
    assert type(response.json) == dict, 'Запрос: /api/posts/1. Возвращается не словарь!'
    assert set(response.json.keys()) == KEYS, 'Запрос: /api/posts/1. Список ключей не верный!'
