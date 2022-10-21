import sqlite3

sql_tabla_usuarios = '''
CREATE TABLE USUARIOS(
ID_USUARIO INTEGER PRIMARY KEY, 
NOMBRE VARCHAR(50), 
CORREO VARCHAR(50) NOT NULL,
APELLIDO VARCHAR(50),
CLAVE TEXT NOT NULL,
TELEFONO VARCHAR(50),
ESTADO_LOGICO BOOLEAN NOT NULL DEFAULT TRUE
)
'''

sql_tabla_rango_precios = '''
CREATE TABLE RANGO_PRECIOS(
ID_RANGO_PRECIO INTEGER PRIMARY KEY, 
DESCRIPCION INTEGER NOT NULL
)
'''

sql_tabla_corrientes = '''
CREATE TABLE CORRIENTES(
ID_CORRIENTE INTEGER PRIMARY KEY, 
DESCRIPCION TEXT NOT NULL
)
'''

sql_tabla_agendas = '''
CREATE TABLE AGENDAS(
ID_AGENDA INTEGER PRIMARY KEY,
FECHA VARCHAR(50),
PSICOLOGO_ELEGIDO VARCHAR(50),
FOREIGN KEY(PSICOLOGO_ELEGIDO) REFERENCES PSICOLOGOS(ID_PSICOLOGO)
)
'''

sql_tabla_psicologos = '''
CREATE TABLE PSICOLOGOS(
ID_PSICOLOGO INTEGER PRIMARY KEY,
NIVEL_ACADEMICO TEXT,
CERTIFICADOS TEXT,
ID_AGENDA INTEGER,
ID_RANGO_PRECIO INTEGER,
ESTADO_LOGICO BOOLEAN NOT NULL DEFAULT TRUE, 
FOREIGN KEY(ID_AGENDA) REFERENCES AGENDAS(ID_AGENDA),
FOREIGN KEY(ID_RANGO_PRECIO) REFERENCES RANGO_PRECIOS(ID_RANGO_PRECIO))
'''

sql_tabla_pacientes = '''
CREATE TABLE PACIENTES(
ID_PACIENTE INTEGER PRIMARY KEY,
NOMBRE_PACIENTE TEXT, 
EDAD INTEGER NOT NULL,
NOMBRE_TUTOR TEXT, 
PSICOLOGOS_CONSULTADOS TEXT, 
ID_AGENDA INTEGER,
ESTADO_LOGICO BOOLEAN NOT NULL DEFAULT TRUE,
FOREIGN KEY(NOMBRE_TUTOR) REFERENCES USUARIOS(ID_USUARIO),
FOREIGN KEY(ID_AGENDA) REFERENCES AGENDAS(ID_AGENDA))
'''

sql_tabla_consultorios = '''
CREATE TABLE CONSULTORIOS(
ID_CONSULTORIO INTEGER PRIMARY KEY, 
PSICOLOGOS_DISPONIBLES TEXT, 
UBICACION VARCHAR(150) NOT NULL,
ID_AGENDA INTEGER,
ESTADO_LOGICO BOOLEAN NOT NULL DEFAULT TRUE,
FOREIGN KEY(ID_AGENDA) REFERENCES AGENDAS(ID_AGENDA))
'''

sql_tabla_corrientes_psicologos = '''
CREATE TABLE CORRIENTES_PSICOLOGOS(
ID_PSICOLOGO INTEGER,
ID_CORRIENTE INTEGER,
FOREIGN KEY(ID_PSICOLOGO) REFERENCES PSICOLOGOS(ID_PSICOLOGO),
FOREIGN KEY(ID_CORRIENTE) REFERENCES CORRIENTES(ID_CORRIENTE)
)
'''

sql_tabla_sesiones = '''
CREATE TABLE SESIONES(
ID INTEGER PRIMARY KEY,
ID_USUARIO TEXT,
FECHA_HORA TEXT,
FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(ID_USUARIO) 
)
'''

if __name__ == '__main__':
    try:
        print('Creando Base de datos..')
        conexion = sqlite3.connect('./mindpsychologyconsultory.db')

        print('Creando Tablas..')
        conexion.execute(sql_tabla_usuarios)
        conexion.execute(sql_tabla_corrientes)
        conexion.execute(sql_tabla_rango_precios)
        conexion.execute(sql_tabla_agendas)
        conexion.execute(sql_tabla_psicologos)
        conexion.execute(sql_tabla_pacientes)
        conexion.execute(sql_tabla_consultorios)
        conexion.execute(sql_tabla_corrientes_psicologos)
        conexion.execute(sql_tabla_sesiones)

        conexion.close()
        print('Creacion Finalizada.')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)
