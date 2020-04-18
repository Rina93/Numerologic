from flask import Flask
from datetime import datetime
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'index.html',
        title='Главная',
        year=datetime.now().year,
    )

@app.route('/facts')
def facts():
    return render_template(
        'facts.html',
        title='Фибоначчи',
        year=datetime.now().year,
    )

@app.route('/focus')
def focus():
    return render_template(
        'focus.html',
        title='Фокус',
        year=datetime.now().year,
    )

@app.route('/happiness')
def happiness():
    return render_template(
        'happiness.html',
        title='Счастливые',
        year=datetime.now().year,
    )

@app.route('/unhappiness')
def unhappiness():
    return render_template(
        'unhappiness.html',
        title='Несчастливые',
        year=datetime.now().year,
    )

@app.route('/history')
def history():
    return render_template(
        'history.html',
        page='История',
        title='История',
        year=datetime.now().year,
    )

@app.route('/numerologic')
def numerologic():
    return render_template(
        'numerologic.html',
        title='Нумерология',
        year=datetime.now().year,
    )


if __name__ == '__main__':
    app.run()
