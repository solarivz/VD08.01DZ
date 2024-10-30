from flask import Flask, render_template, request, redirect, url_for
import requests

# Создаём экземпляр Flask-приложения
app = Flask(__name__)


# Маршрут для главной страницы
@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None  # Переменная для хранения цитаты

    # Если пользователь нажал кнопку "Получить цитату"
    if request.method == 'POST':
        # Запрашиваем случайную цитату через API
        response = requests.get('https://api.quotable.io/random')

        if response.status_code == 200:  # Если запрос успешен
            data = response.json()
            quote = {
                'content': data['content'],  # Текст цитаты
                'author': data['author']  # Автор цитаты
            }

    # Рендерим HTML-шаблон и передаём в него цитату
    return render_template('index.html', quote=quote)


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
