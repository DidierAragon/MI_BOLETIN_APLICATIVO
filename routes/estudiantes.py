from flask import Blueprint

estudiantes_routes = Blueprint("estudiantes", __name__)

@estudiantes_routes.route("/estudiantes")
def estudiantes():
    return "Lista de estudiantes"