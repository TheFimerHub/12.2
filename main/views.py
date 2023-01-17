import logging
import logging.config
from flask import Blueprint, request, render_template
from functions import get_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename="basic.log", level=logging.INFO)

@main_blueprint.route("/")
def index_page():
    return render_template('index.html')

@main_blueprint.route("/search")
def search_page():
    search = request.args.get('s')
    posts = get_by_word(search)
    logging.info("Страница поиского запроса: запрошена")
    return render_template('post_list.html', search=search, posts=posts)
@main_blueprint.errorhandler(500)
def not_found(error):
    logging.error("Ошибка: posts.json отсутствует или не хочет преобразовываться в список")
    return "Ошибка: posts.json отсутствует или не хочет преобразовываться в список.", 500