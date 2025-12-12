from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal que renderiza loginuser.html
@app.route('/')
def index():
    return render_template('loginuser.html')

# Ruta para loginuser (mismo que la principal)
@app.route('/loginuser')
def loginuser():
    return render_template('loginuser.html')

# Ruta para solicitud_user
@app.route('/solicitud_user')
def solicitud_user():
    return render_template('solicitud.html')

if __name__ == '__main__':
    app.run(debug=True)