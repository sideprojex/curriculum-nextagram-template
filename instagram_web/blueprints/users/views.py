from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.user import User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


users_blueprint = Blueprint("users", __name__, template_folder="templates")


@users_blueprint.route("/new", methods=["GET"])
def new():
    return render_template("users/new.html")


@users_blueprint.route("/new", methods=["POST"])
def create():

    user_name = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")

    # hashed_password = generate_password_hash(password)  # store this in the database

    user = User(username=user_name, email=email, password=password)

    if user.save():
        flash("Succesfully Signed up!,")
        return redirect(url_for("users.new"))
    else:
        flash("Error logging in,")
        return redirect(url_for("home"))


@users_blueprint.route("/<username>", methods=["GET"])
def show(username):
    pass


@users_blueprint.route("/", methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route("/<id>/edit", methods=["GET"])
def edit(id):
    pass


@users_blueprint.route("/<id>", methods=["POST"])
def update(id):
    pass
