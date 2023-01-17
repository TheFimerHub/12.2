import logging
from flask import Blueprint, request, render_template
from functions import *
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename="basic.log", level=logging.INFO)


@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')



ALLOWED_EXTENSIONS = {'jpg', 'png'}


@loader_blueprint.route('/post', methods=['POST'])
def upload_file():
    picture = request.files.get("picture")
    picture_filename = picture.filename
    extension = picture_filename.split(".")[-1]
    if picture:
        if extension in ALLOWED_EXTENSIONS:
            picture.save(f'./uploads/images/{picture_filename}')
            text = request.form.get("text")
            new_post(f'./uploads/images/{picture_filename}', text)
            return render_template('post_uploaded.html', picture_filename=picture_filename, text=text)
        else:
            logging.info("Загруженный файл - не картинка (расширение не jpe и не png")
            return f'Загруженный файл - не картинка (расширение не jpg и не png)'    
    else:
        logging.error("Ошибка при загрузке файла")
        return 'Файл не загружен'
@loader_blueprint.errorhandler(403)
def not_found(error):
    return "Ошибка: posts.json отсутствует или не хочет преобразовываться в список.", 403