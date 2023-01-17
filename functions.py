import json
from urllib.error import HTTPError

def load_post() -> list[dict]:
    try:
        with open('../lesson12_project_source_v3-master/posts.json', 'r') as file:
            return json.load(file)   
    except FileNotFoundError:
        return "Ошибка: posts.json отсутствует или не хочет преобразовываться в список."
    except HTTPError as e:
        if e.code == 403:
            return "<h1>Ошибка :(</h1><p>posts.json отсутствует или не хочет преобразовываться в список</p>", 500


def get_by_word(word: str) -> list[dict]:
    result = []
    for post in load_post():
        if word.lower() in post["content"].lower():
            result.append(post)
    return result

def new_post(picture, content):
    posts = load_post()
    posts.append({
        "pic": picture,
        "content": content
    })
    with open('../lesson12_project_source_v3-master/posts.json', 'w') as file:
        json.dump(posts, file, ensure_ascii=False)