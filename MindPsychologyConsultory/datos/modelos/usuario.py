from datos.base_de_datos import BaseDeDatos

def obtener_usuario(id_usuario):
    obtener_usuarios_sql = f"""
        SELECT ID_USUARIO, NOMBRE, APELLIDO, CORREO
        FROM USUARIOS 
        WHERE ID_USUARIO = {id_usuario} AND ESTADO_LOGICO = 1
    """
    bd = BaseDeDatos()
    return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "APELLIDO": registro[2],
             "CORREO": registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]

def obtener_usuarios():
    obtener_usuarios_sql = f"""
        SELECT ID_USUARIO, NOMBRE, APELLIDO, CORREO 
        FROM USUARIOS
        WHERE ESTADO_LOGICO = 1
    """
    bd = BaseDeDatos()
    return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "APELLIDO":registro[2],
             "CORREO": registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]



def crear_usuario(correo, clave, nombre, apellido, telefono):
    crear_usuario_sql = f"""
        INSERT INTO USUARIOS (CORREO, CLAVE, NOMBRE, APELLIDO, TELEFONO)
        VALUES ('{correo}', '{clave}', '{nombre}', '{apellido}', '{telefono}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)


def modificar_usuario(id_usuario, datos_usuario):
    modificar_usuario_sql = f"""
        UPDATE USUARIOS
        SET NOMBRE='{datos_usuario["nombre"]}', CLAVE='{datos_usuario["clave"]}', APELLIDO='{datos_usuario["apellido"]}', CORREO='{datos_usuario["correo"]}', TELEFONO='{datos_usuario["telefono"]}'
        WHERE ID_USUARIO='{id_usuario}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)

def obtener_usuarios_por_correo_clave(correo, clave):
    obtener_usuario_sql = f"""
            SELECT ID_USUARIO, NOMBRE, CORREO 
            FROM USUARIOS u
            WHERE CORREO='{correo}' AND CLAVE='{clave}'
        """
    bd = BaseDeDatos()
    return [{"ID_USUARIO": registro[0],
             "NOMBRE": registro[1],
             "CORREO": registro[2],
             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]

def borrar_usuario(id_usuario):
    borrar_usuarios_sql = f"""
            UPDATE USUARIOS 
            SET ESTADO_LOGICO = 0 
            WHERE ID_USUARIO = '{id_usuario}'
        """
    bd = BaseDeDatos()
    bd.ejecutar_sql(borrar_usuarios_sql)

def obtener_usuario_por_id(id_usuario):
    obtener_usuario_por_id_sql = f"""
        SELECT ID_USUARIO 
        FROM USUARIOS 
        WHERE ID_USUARIO = {id_usuario}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_usuario_por_id_sql)



def crear_sesion(id_usuario, dt_string):
    crear_sesion_sql = f"""
               INSERT INTO SESIONES(ID_USUARIO, FECHA_HORA)
               VALUES ('{id_usuario}', '{dt_string}')
           """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)

def obtener_sesion(id_sesion):
    obtener_sesion_sql = f"""
        SELECT ID, ID_USUARIO, FECHA_HORA FROM SESIONES WHERE ID = {id_sesion}
    """
    bd = BaseDeDatos()
    return [{"ID": registro[0],
             "ID_USUARIO": registro[1],
             "FECHA_HORA": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_sql)]