import requests

from servicios import rest_api


def validar_credenciales(correo, clave):
    body = {"correo": correo,
            "clave": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    # Solo verificamos el codigo de la respuesta en este caso
    return respuesta.status_code == 200


def crear_usuario(correo, clave, nombre, apellido, telefono):
    body = {"correo": correo,
            "clave": clave,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()