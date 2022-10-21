from flask import Flask, request, redirect, url_for
from flask import render_template
from servicios import autenticacion

app = Flask(__name__)


@app.route('/')
def index():
    titulo_psicologia = "Mind Psychology Consultory"
    return render_template('inicio.html', titulo = titulo_psicologia)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['correo'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            return redirect(url_for('inicio'))
    return render_template('login.html', error=error)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['correo'], request.form['password'], request.form['nombre'], request.form['apellido'], request.form['telefono']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('inicio'))
    return render_template('registro.html', error=error)


@app.route('/inicio')
def inicio():
    usuarios = autenticacion.obtener_usuarios()
    return render_template('inicio.html', usuarios=usuarios)

@app.route('/listarUsuarios')
def ListarUsuarios():
    usuarios = autenticacion.obtener_usuarios()
    return render_template('ListarUsuarios.html', usuarios=usuarios)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)