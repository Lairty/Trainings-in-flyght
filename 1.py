from flask import Flask
from flask import render_template
from flask import url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app = Flask(__name__)


def main():
    app.run()


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title="Главная страница")


@app.route('/training/<prof>')
def training(prof):
    if "инженер" in prof or "строитель" in prof:
        tr = 1
        path = url_for('static', filename='img/us.png')
    else:
        tr = 2
        path = url_for('static', filename='img/ns.png')
    return render_template('training.html', title="Тренировки", tr=tr, path=path)


if __name__ == '__main__':
    main()