from flask import Flask, render_template, request, redirect, url_for
import requests

# Создаём экземпляр Flask-приложения
app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    