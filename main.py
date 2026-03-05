from flask import Flask
from app1 import app1
from app import admin

app = Flask(__name__)

app.secret_key = "clave_secreta"

app.register_blueprint(app1, name='')
app.register_blueprint(admin)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)