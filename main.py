from flask import Flask, url_for, render_template

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


@app.route('/promotion_image')
def mars_greeting():
    html_keys = {
        'picture_url': url_for('static', filename='img/mars.jpg'),
        'css_url': url_for('static', filename='css/style.css')
    }
    return render_template('index.html', **html_keys)


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


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
