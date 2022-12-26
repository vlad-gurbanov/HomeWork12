# Импорт библиотеки flask
from flask import Flask, send_from_directory

import logging

# Импорт блюпринтов

from main.view import main_blueprint
from loader.view import loader_blueprint

# Объявление экземпляра класса Flask
app = Flask(__name__)

# Регистрация  блюпринтов
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename="basic.log", level=logging.INFO)


@app.route('/static/uploads/<path:path>')
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
