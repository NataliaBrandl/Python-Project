from datos.modelos import usuario as modelo_usuario
from datetime import datetime

def _existe_usuario(correo, clave):
    usuarios = modelo_usuario.obtener_usuarios_por_correo_clave(correo, clave)
    return not len(usuarios) == 0

def _existe_usuario_id(id_usuario):
    usuarios = modelo_usuario.obtener_usuario_por_id(id_usuario)
    return not len(usuarios) == 0

def _crear_sesion(id_usuario):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario.crear_sesion(id_usuario, dt_string)

def obtener_usuarios():
    return modelo_usuario.obtener_usuarios()

def obtener_usuario(id_usuario):
    usuarios = modelo_usuario.obtener_usuario(id_usuario)
    if len(usuarios) == 0:
        raise Exception("El usuario no existe")
    return usuarios[0]

def crear_usuario(correo, clave, nombre, apellido, telefono):
    if not _existe_usuario(correo,clave):
        modelo_usuario.crear_usuario(correo, clave, nombre, apellido, telefono)
    else:
        raise Exception("El usuario ya existe")

def modificar_usuario(id_usuario, datos_usuario):
    modelo_usuario.modificar_usuario(id_usuario, datos_usuario)

def borrar_usuario(id_usuario):
    modelo_usuario.borrar_usuario(id_usuario)


def login(correo, clave):
    if _existe_usuario(correo, clave):
        usuario = modelo_usuario.obtener_usuarios_por_correo_clave(correo, clave)[0]
        return _crear_sesion(usuario['ID_USUARIO'])
    else:
        raise Exception("El usuario no existe o la clave es invalida")

def validar_sesion(id_sesion):
    sesiones = modelo_usuario.obtener_sesion(id_sesion)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Sesion expirada
        return False
    else:
        return True