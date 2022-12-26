# Импорт библиотеки json
import json


def get_text(filename):
    """ Преобразование json файла в python файл"""

    with open(filename, "r", encoding='UTF-8') as file:
        file_read = file.read()
        pyt_file = json.loads(file_read)
    return pyt_file


def get_content(filename, text):
    """ Поиск введенного слова"""

    elements_list = []
    for element in filename:
        if text.lower() in element["content"].lower():
            elements_list.append(element)
    return elements_list


def load_json_file(picture, added_page):
    """ Добавление нового тееста и фото в json файл"""

    word_diction = {}
    word_diction["pic"] = f"{picture}"
    word_diction["content"] = f"{added_page}"
    with open("posts.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
        data.append(word_diction)
    with open("posts.json", "w", encoding="UTF-8") as file:
        new_file = json.dump(data, file, ensure_ascii=False)
    return new_file


def is_filename_allowed(filename):
    """Определение расширения загружаемого файла"""

    allowed_extensions = ['png', 'jpg', 'jpeg']
    extension = filename.split(".")[-1]
    if extension in allowed_extensions:
        return True
    else:
        return False
