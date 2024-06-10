from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'w53y4yhnf8gnfgsdgdhhfdfgdgdgdgdfhf'

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О портале", "url": "about"},
]


@app.route("/")
@app.route("/index")
def index():
    print(url_for("index"))
    return render_template("index.html", title="Новостной портал 'ПроСвет'", menu=menu)


@app.route("/about")
def about():
    print(url_for("about"))
    return render_template('about.html', title="О портале", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template("page404.html", title="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
