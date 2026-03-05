from flask import Blueprint, render_template

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/")
def login():
    return render_template("login.html")