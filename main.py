from flask import Flask, url_for, render_template, request
from collections import namedtuple
from random import sample
from os.path import abspath

app = Flask(__name__)
app.config['SECRET_KEY'] = 'just_dance_dara_duru'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    html_keys = {
        'title': title
    }
    return render_template('index.html', **html_keys)


@app.route('/promotion')
def promotion():
    return '''<h2>Человечество вырастает из детства.
    </br>Человечеству мала одна планета.
    </br>Мы сделаем обитаемыми безжизненные пока планеты.
    </br>И начнем с Марса!
    </br>Присоединяйся!<h2>'''


@app.route('/promotion_image')
def mars_greeting():
    html_keys = {
        'picture_url': url_for('static', filename='img/mars.jpg'),
        'css_url': url_for('static', filename='css/style.css')
    }
    return render_template('promotion.html', **html_keys)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    html_keys = {
        'professions': [
            "инженер-исследователь",
            "пилот",
            "строитель",
            "экзобиолог",
            "врач",
            "инженер по терраформированию",
            "климатолог",
            "специалист по радиационной защите",
            "астрогеолог",
            "гляциолог",
            "инженер жизнеобеспечения",
            "метеоролог",
            "оператор марсохода",
            "киберинженер",
            "штурман",
            "пилот дронов"
        ],
        'education_variants': [
            'Начальное общее образование',
            'Основное общее образование',
            'Среднее общее образование',
            'Среднее профессиональное образование',
            'Высшее образование'
        ],
        'css_url': url_for('static', filename='css/registration styles.css')
    }
    return render_template('registration form.html', **html_keys)


@app.route('/choice/<name>')
def choice(name):
    Article = namedtuple('Article', ['text', 'color'])
    ordered_planet_info = [
        Article('Прекрасная планета!', 'alert alert-dark'),
        Article('Только бескрайние поля;', 'alert alert-dark'),
        Article('Человечество тут не властно;', 'alert alert-success'),
        Article('Максимум пара племен гунганов;', 'alert alert-success'),
        Article('Здесь царит справедливость и порядок;', 'alert alert-secondary'),
        Article('Даже не знаю, что может пойти не так;', 'alert alert-secondary'),
        Article('Отличный выбор!', 'alert alert-warning'),
        Article('Собирай вещи и в полёт!', 'alert alert-warning')
    ]
    html_keys = {
        'planet_name': name,
        'css_url': url_for('static', filename='css/choice.css'),
        'planet_info': sample(ordered_planet_info, k=4)
    }
    return render_template('choice.html', **html_keys)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level: int, rating: float):
    html_keys = {
        'nickname': nickname,
        'level': level,
        'rating': rating
    }
    return render_template('results.html', **html_keys)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    html_keys = {
        'css_url': url_for('static', filename='css/load_photo.css'),
        'is_picture_sent': False,
        'picture_url': None
    }

    if request.method == 'GET':
        html_keys['is_picture_sent'] = False
        html_keys['picture_url'] = None
        return render_template('load_photo.html', **html_keys)

    if request.method == 'POST':
        html_keys['is_picture_sent'] = True
        html_keys['picture_url'] = abspath(request.files['sent_image'].filename)
        return render_template('load_photo.html', **html_keys)


@app.route('/carousel')
def carousel():
    html_keys = {
        'css_url': url_for('static', filename='css/carousel.css'),
        'images_url': [url_for('static',
                               filename=f'img/carousel_pictures/{i}.jpg')
                       for i in range(1, 5)]
    }
    return render_template('carousel.html', **html_keys)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
