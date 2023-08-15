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
