from http import HTTPStatus

from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import or_
from werkzeug.exceptions import NotFound

from .forms import UserForm
from models import db, User

users_app = Blueprint(
    "users_app",
    __name__,
    url_prefix="/users",
)


@users_app.get("/", endpoint="list")
def get_users():
    users = db.session.query(User).all()
    search = request.args.get("search") or ""
    query = User.query
    if search:
        query = query.filter(
            or_(
                User.name.ilike(f"%{search}%"),
                User.short_description.ilike(f"%{search}%"),
            ),
        )
    users = query.order_by(User.id).all()

    return render_template(
        "users/list.html",
        users=users,
        search=search,
    )


def get_user_or_raise(user_id: int) -> User:
    user = User.query.get(user_id)
    if user:
        return user
    raise NotFound(f"User #{user_id} not found!")


@users_app.get("/<int:user_id>/", endpoint="details")
def get_user_details(user_id: int):
    user = get_user_or_raise(user_id)
    return render_template("users/details.html", user=user)


@users_app.route("/<int:user_id>/delete/", methods=["GET", "POST"], endpoint="delete")
def create_user(user_id: int):
    form = UserForm()
    user = get_user_or_raise(user_id)

    if request.method == "GET":
        return render_template("users/delete.html", user=user, form=form)

    user_name = user.name
    db.session.delete(user)
    db.session.commit()
    flash(f"User {user_name} deleted!", category="warning")
    url = url_for("users_app.list")
    return redirect(url)


@users_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/create.html", form=form)

    if not form.validate_on_submit():
        return (
            render_template("users/create.html", form=form),
            HTTPStatus.BAD_REQUEST,
        )

    user = User(
        name=form.data["name"],
        short_description=form.data["short_description"],
    )
    db.session.add(user)
    db.session.commit()
    flash(f"User {user.name} has been successfully created!", category="success")
    url = url_for("users_app.details", user_id=user.id)
    return redirect(url)
