from flask import Flask, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'just_dance_dara_duru'


@app.route('/')
def mission_name():
    return f'<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return f'<h2>И на Марсе будут яблони цвести!</h2>'


@app.route('/promotion')
def promotion():
    return '''<h2>Человечество вырастает из детства.
    </br>Человечеству мала одна планета.
    </br>Мы сделаем обитаемыми безжизненные пока планеты.
    </br>И начнем с Марса!
    </br>Присоединяйся!<h2>'''



@app.route('/image_mars')
def mars_greeting():
    picture_url = url_for('static', filename='img/mars.jpg')
    return f"""
            <img src={picture_url} alt="The greatest planet on Earth :)">
            <h2>Вот она какая, красная планета!</h2>
        """


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
