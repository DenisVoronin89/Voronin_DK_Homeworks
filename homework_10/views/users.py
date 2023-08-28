from dataclasses import dataclass

from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import BadRequest, NotFound


users_app = Blueprint(
    "users_app",
    __name__,
    url_prefix="/users",
)


@dataclass(frozen=False)
class User:
    id: int
    name: str
    short_description: str = ""


@dataclass(frozen=False)
class UsersStorage:
    users: dict[int, User]
    last_index: int = 0

    @property
    def next_index(self):
        self.last_index += 1
        return self.last_index

    def create(self, name: str) -> User:
        user = User(id=self.next_index, name=name)
        self.users[user.id] = user
        short_description = f"User #{user.id} ({user.name}) short description"
        user.short_description = short_description
        return user


storage = UsersStorage(users={})
storage.create("Den")
storage.create("Suren")
storage.create("Evgeniy")


@users_app.get("/", endpoint="list")
def get_users():
    users = list(storage.users.values())
    return render_template("users/list.html", users=users)


def get_user_or_raise(user_id: int) -> User:
    user = storage.users.get(user_id)
    if user:
        return user
    raise NotFound(f"User #{user_id} not found!")


@users_app.get("/<int:user_id>/", endpoint="details")
def get_user_details(user_id: int):
    user = get_user_or_raise(user_id)
    return render_template("users/details.html", user=user)


@users_app.route("/<int:user_id>/delete/", methods=["GET", "POST"], endpoint="delete")
def create_user(user_id: int):
    user = get_user_or_raise(user_id)

    if request.method == "GET":
        return render_template("users/delete.html", user=user)

    storage.users.pop(user_id)
    flash(f"Deleted user {user.name}!", category="warning")
    url = url_for("users_app.list")
    return redirect(url)


@users_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_user():
    if request.method == "GET":
        return render_template("users/create.html")

    user_name = request.form.get("user-name", "")
    user_name = user_name.strip()
    if not user_name:
        raise BadRequest("Field user-name is required!")

    user = storage.create(user_name)
    flash(f"User {user.name} was created!", category="success")
    url = url_for("users_app.details", user_id=user.id)
    return redirect(url)
