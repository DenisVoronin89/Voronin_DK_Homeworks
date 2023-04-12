"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""


from flask import Flask, request, render_template, flash

from views.users import users_app


app = Flask(__name__)
app.config.update(
    SECRET_KEY="qwerty",
)

app.register_blueprint(users_app)


@app.get("/")
def index_view():
    return render_template("index.html")


@app.get("/about/")
def hello_view():
    name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"

    flash("* * * * * Homework_05 started successfully * * * * *")
    return render_template("about.html", name=name)



if __name__ == "__main__":
    app.run(
        debug=True,
    )
