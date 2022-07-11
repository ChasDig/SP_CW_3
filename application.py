from flask import Flask, render_template
from apps.poster.views import bp_posts
from apps.main.views import bp_main
from apps.users.views import bp_users
from apps.bookmarks.views import bp_bookmarks
import logging

# Создаем экземпляр Flask:
app = Flask(__name__)

# Регистрируем Blueprint: main_blueprint:
app.register_blueprint(bp_main)

# Регистрируем Blueprint: bp_posts:
app.register_blueprint(bp_posts)

# Регистрируем Blueprint: bp_users:
app.register_blueprint(bp_users)

# Регистрируем Blueprint: bp_bookmarks:
app.register_blueprint(bp_bookmarks)

# Устанавливаем параметр для  обработки JSON_AS_ASCII:
app.config['JSON_AS_ASCII'] = False


# Обработчик ошибки 404:
@app.errorhandler(404)
def error_404(e):
    return render_template("error_type.html", error_type=404), 404


# Обработчик ошибки 500:
@app.errorhandler(500)
def error_500(e):
    return render_template("error_type.html", error_type=500), 500


if __name__ == '__main__':
    app.run()
