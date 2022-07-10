import json


# Класс: обрабатывает данные постов:
class PostersAndCommentsDAO:


    # Функция: ссылка на data.json:
    def __init__(self, path_data, path_comments):
        self.path_data = path_data
        self.path_comments = path_comments




    # Функция: загружаем из json-файл информацию о постах:
    def load_posters_data(self) -> list[dict]:
        """
        :return: информация о постах
        """
        with open(self.path_data, 'r', encoding='utf-8') as file:
            load_data = json.load(file)
            if not load_data:
                raise ValueError("Информация о постах не загружается из json-файла!")
            return load_data

    # Функция: загружаем из json-файл информацию о комментариях:
    def load_comments_data(self):
        """
        :return: информация о комментариях
        """
        with open(self.path_comments, 'r', encoding='utf-8') as file:
            load_comments = json.load(file)
            return load_comments




    # Функция: предоставляем данные обо всех постах (возвращает список(словарей) постов):
    def get_all_posters(self):
        """
        :return: данные о постах
        """
        all_posters = self.load_posters_data()
        return all_posters

    # Функция: предоставляем данные обо всех комментариях (возвращает список(словарей) комментариев):
    def get_all_comments(self):
        """
        :return: данные о комментариях
        """
        all_comments = self.load_comments_data()
        return all_comments




    # Функция: возвращает посты определенного пользователя:
    def search_posters_by_users(self, poster_user) -> list[dict]:
        """
        :param poster_user: имя (идентификатор) пользователя
        :return: посты пользователя
        """

        # Проверяем наличие у пользователя постов (поиск постов):
        all_posters = self.get_all_posters()
        # Буфер, проверяющий наличие пользователя среди авторов постов:
        have_user_poster = False
        # Список всех постов пользователя:
        all_poster_by_user = []
        for poster in all_posters:
            if poster["poster_name"] == poster_user:
                all_poster_by_user.append(poster)
                have_user_poster = True

        # Вывод ошибки, если пользователя нет среди авторов постов:
        if not have_user_poster:
            raise ValueError("Такого пользователя среди авторов постов нет!")

        # Возвращаем список статей пользователя (пустой список, если статей нет):
        return all_poster_by_user




    # Функция: поиск поста по pk_поста(идентификация поста):
    def search_posters_by_pk(self, poster_pk):
        """
        :param poster_pk: идентификатор поста
        :return: результат поиска - пост с нужным pk
        """
        poster_with_poster_pk = 0
        # Ищем пост по pk_поста:
        all_posters = self.get_all_posters()
        for poster in all_posters:
            if poster['pk'] == int(poster_pk):
                poster_with_poster_pk = poster
        return poster_with_poster_pk




    # Функция: возвращает комментарии определенного поста:
    def get_comments_by_post_id(self, poster_pk):

        # Находим пост по poster_pk:
        poster_with_poster_pk = self.search_posters_by_pk(poster_pk)

        # Проверяем наличие поста(по его poster_pk):
        if not poster_with_poster_pk:
            raise ValueError(poster_with_poster_pk)

        # Вытаскиваем pk найденного поста:
        pk_poster = poster_with_poster_pk["pk"]

        # Загружаем список всех комментариев:
        all_comments = self.get_all_comments()
        # Список комментариев определенного поста:
        all_comments_by_pk_poster = []

        # Совершаем поиск комментариев по pk-поста (определенного poster_pk):
        for comment in all_comments:
            if comment["post_id"] == pk_poster:
                all_comments_by_pk_poster.append(comment)

        # Возвращает список комментариев определенного поста (пустой, если список пуст):
        return all_comments_by_pk_poster



    # Фуекция: возвращает все посты по ключевому слову:
    def search_posters_by_args(self, args):
        """\
        :param args: ключевое слово
        :return: список постов с ключевым словом
        """
        # Все посты:
        all_posters = self.get_all_posters()

        # Список постов, в которых есть ключевое слово:
        posts_with_args = []

        # Поиск поста с наличием в нем ключевого слова:
        for post in all_posters:
            if args in post['content']:
                posts_with_args.append(post)

        return posts_with_args



    # Функция: возвращает все посты по тегу:
    def search_posters_by_tags(self, get_tags):

        # Получаем список всех постов:
        all_posters = self.get_all_posters()

        # Список постов с указанными тегами:
        founder_tags = []

        for poster in all_posters:
            if poster['tags'] == get_tags:
                founder_tags.append(poster)

        return founder_tags


# Класс: обработка закладки:
class Bookmarks(PostersAndCommentsDAO):

    # Создаем подкласс со ссылкой на json-файл с закладками:
    def __init__(self, path_data, path_comments, path_bookmarks):
        super().__init__(path_data, path_comments)
        self.path_bookmarks = path_bookmarks

    # Функция - открываем json-файл с закладками:
    def load_bookmarks_data(self):
        """
        :return: информация о закладках
        """
        with open(self.path_bookmarks, 'r', encoding='utf-8') as file:
            load_data = json.load(file)
            return load_data

    # Функция - получаем все закладки
    def get_all_bookmarks(self):
        """
        :return: данные о комментариях
        """
        all_bookmarks = self.load_bookmarks_data()
        return all_bookmarks


    # Функция - копируем информацию о посте в закладки:
    def put_post_in_bookmarks_json(self, poster_pk):

        """
        :param poster_pk: идентификатор поста
        :return: обновленный список закладок
        """

        # Получаем нужный пост по его 'pk':
        poster_with_poster_pk = self.search_posters_by_pk(poster_pk)

        # Получаем список всех закладок:
        all_bookmarks = self.get_all_bookmarks()

        # Добавляем новую закладку в список с закладками:
        all_bookmarks.append(poster_with_poster_pk)

        # Добавляем обновленный список закладок (с новой закладкой) в json-файл:
        with open(self.path_bookmarks, 'w', encoding='utf-8') as file:
            json.dump(all_bookmarks, file)

        return all_bookmarks


    # Функция: удаляем требуемый пост:
    def delet_post_in_bookmark(self, poster_pk):

        """
        :param poster_pk: идентификатор поста
        :return: обновленный список закладок
        """

        # Получаем список всех закладок:
        all_bookmarks = self.get_all_bookmarks()

        # Буфер, который будет содержать все посты, кроме удаляемого:
        bookmarks_not_bookmarks_pk = []

        # Поиск нужного для удаления пост:
        for bookmark in all_bookmarks:
            if bookmark['pk'] == int(poster_pk):
                continue
            else:
                bookmarks_not_bookmarks_pk.append(bookmark)

        # Добавляем все посты обратно в закладки, кроме удаляемого:
        with open(self.path_bookmarks, 'w', encoding='utf-8') as file:
            json.dump(bookmarks_not_bookmarks_pk, file)

        return bookmarks_not_bookmarks_pk
