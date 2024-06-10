import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, g

from FDataBase import FDataBase

DATABASE = None
DEBUG = True
SECRET_KEY = '0202ed47a68326ff5a288fd7b69a919ec7eb6187'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'news.db')))

menu = [
    {"title": "Главная", "url": "/"},
    {"title": "Добавить новость", "url": "/add_news"},
    {"title": "О портале", "url": "/about"},
]


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", title="Новостной портал 'ПроСвет'", menu=menu, news=dbase.get_news_annonce())


@app.route("/about")
def about():
    return render_template('about.html', title="О портале", menu=menu)


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/add_news", methods=["POST", "GET"])
def add_news():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['news']) > 10:
            res = dbase.add_news(request.form['name'], request.form['news'], request.form['url'])
            if not res:
                flash("Ошибка добавления новости", category="error")
            else:
                flash("Новость добавлена успешно", category="success")
        else:
            flash("Ошибка длины", category="error")
    return render_template("add_news.html", title="Добавление новости", menu=menu)


@app.route("/news/<alias>")
def show_news(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, news = dbase.get_news(alias)
    return render_template('news.html', menu=menu, title=title, news=news)


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template("page404.html", title="Страница не найдена", menu=menu)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
