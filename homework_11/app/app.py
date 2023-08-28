"""
Домашнее задание №6
Взят код веб-приложения из домашнего задания №6

"""

import os

from flask import Flask, request, render_template, flash
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from models import db
from views.users import users_app

config_name = os.getenv("CONFIG_NAME", "ProductionConfig")

app = Flask(__name__)

app.config.from_object(f"config.{config_name}")
app.register_blueprint(users_app)

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)


@app.cli.command("create-all")
def command_create_all():
    with app.app_context():
        db.create_all()


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
    app.run(host="0.0.0.0")

