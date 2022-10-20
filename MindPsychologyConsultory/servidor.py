from flask import Flask, request, jsonify
from servicios import autenticacion


app = Flask(__name__)


@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'correo' not in datos_usuario or datos_usuario['correo'] == '':
        return 'El correo es requerido', 412
    elif 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    try:
        autenticacion.crear_usuario(datos_usuario['correo'], datos_usuario['clave'], datos_usuario['nombre'], datos_usuario['apellido'], datos_usuario['telefono'])
    except Exception:
        return 'El usuario ya existe'
    return 'OK', 200

@app.route('/usuarios/<id_usuario>', methods=['PUT'])
def modificar_usuario(id_usuario):
    datos_usuario = request.get_json()
    if 'correo' not in datos_usuario or datos_usuario['correo'] == '':
        return 'El correo es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    autenticacion.modificar_usuario(id_usuario, datos_usuario)
    return 'OK', 200

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(autenticacion.obtener_usuarios())

@app.route('/usuarios/<id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    try:
        usuario = autenticacion.obtener_usuario(id_usuario)
        return jsonify(usuario)
    except Exception:
        return 'Usuario no encontrado', 404

@app.route('/usuarios/<id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    try:
        autenticacion.obtener_usuario(id_usuario)
        autenticacion.borrar_usuario(id_usuario)
        return "El usuario ha sido borrado"
    except Exception:
        return 'Usuario no encontrado'


@app.route('/login', methods=['POST'])
def login():
    datos_usuario = request.get_json()
    if 'correo' not in datos_usuario:
        return 'El correo es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    id_sesion = autenticacion.login(datos_usuario['correo'], datos_usuario['clave'])
    return jsonify({"id_sesion": id_sesion})


if __name__ == '__main__':
    app.debug = True
    app.run()
