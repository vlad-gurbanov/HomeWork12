# Импорт библиотек и функций
import logging
from flask import Blueprint, render_template, request
from functions import load_json_file, is_filename_allowed
from json import JSONDecodeError

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/load/')
def load_page():
    """ Представление  страницы, где загружаются посты"""
    return render_template("post_form.html")


@loader_blueprint.route('/upload_post/', methods=['POST'])
def upload_post():
    """ Представление  страницы, с загруженными постами"""
    try:
        added_page = request.form['content']
        picture = request.files.get("picture")
        filename = picture.filename
        picture.save(f"static/uploads/{filename}")
        load_json_file(picture, added_page)
        load_json_file(picture, added_page)
        if is_filename_allowed(filename):
            return render_template("post_uploaded.html", added_page=added_page, filename=filename)
        else:
            logging.error('Файл с неверным расширением')
            return "Неверное расширение файла"
    except PermissionError:
        logging.error('Файл не найден')
        return "<h1>Ошибка загрузки файла. Загрузите файл заново</h1>"
    except JSONDecodeError:
        return 'Файл не удалось преобразовать'
