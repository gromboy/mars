from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def start():
    return '<b>Миссия Колонизация Марса<b>'


@app.route('/index')
def index():
    return '<b>И на Марсе будут яблони цвести!<b>'


@app.route('/promotion')
def promotion():
    return '''<b>Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<b>
    <br>И начнем с Марса!<br>Присоединяйся!'''


@app.route('/image_mars')
def image():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.png')}">
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
