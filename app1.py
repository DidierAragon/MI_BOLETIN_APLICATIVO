from flask import Flask, render_template, request, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="miboletin",
        user="postgres",
        password="123456"
    )

# Ruta principal
@app.route('/')
def index():
    return render_template('loginuser.html')

# Ruta para loginuser
@app.route('/loginuser')
def loginuser():
    return render_template('loginuser.html')

# Ruta para solicitud_user con datos del administrador
@app.route('/solicitud_user')
def solicitud_user():
    # Obtener un administrador de la base de datos
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id_admin, nombre_completo, correo_electronico FROM administradores LIMIT 1;')
    admin = cur.fetchone()
    cur.close()
    conn.close()
    
    # Si no hay administrador, usar valores por defecto
    if admin:
        admin_id, admin_name, admin_email = admin
    else:
        admin_id, admin_name, admin_email = 'ADM001', 'Administrador del Sistema', 'admin@sistema.com'
    
    return render_template('solicitud.html', 
                         admin_id=admin_id, 
                         admin_name=admin_name, 
                         admin_email=admin_email)

# Nueva ruta para verificar usuario
@app.route('/verificar_usuario', methods=['POST'])
def verificar_usuario():
    data = request.json
    user_identifier = data.get('userIdentifier')
    user_email = data.get('userEmail')
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Buscar en estudiantes
    cur.execute(
        'SELECT id_estudiante, nombre_completo FROM estudiantes WHERE codigo_estudiante = %s AND correo_electronico = %s;',
        (user_identifier, user_email)
    )
    estudiante = cur.fetchone()
    
    if estudiante:
        cur.close()
        conn.close()
        return jsonify({
            'status': 'success',
            'tipo': 'estudiante',
            'id': estudiante[0],
            'nombre': estudiante[1]
        })
    
    # Buscar en profesores
    cur.execute(
        'SELECT id_profesor, nombre_completo FROM profesores WHERE codigo_profesor = %s AND correo_electronico = %s;',
        (user_identifier, user_email)
    )
    profesor = cur.fetchone()
    
    if profesor:
        cur.close()
        conn.close()
        return jsonify({
            'status': 'success',
            'tipo': 'profesor',
            'id': profesor[0],
            'nombre': profesor[1]
        })
    
    cur.close()
    conn.close()
    return jsonify({
        'status': 'error',
        'message': 'Usuario no encontrado. Verifica tu identificador y correo electrónico.'
    }), 404

if __name__ == '__main__':
    app.run(debug=True)