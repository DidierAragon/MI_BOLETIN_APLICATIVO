from flask import Blueprint

profesores_routes = Blueprint("profesores", __name__)

@profesores_routes.route("/profesores")
def profesores():
    return "Lista de profesores"