"""Módulo que gestiona la base de datos de la biblioteca."""

import sqlite3

nombre_db = "biblioteca.db"

def crear_tablas():
	"""Función que crea las tablas necesarias en la base de datos si no existen."""

	conexion = sqlite3.connect(nombre_db)
	db = conexion.cursor()

	try:
		db.execute("""CREATE TABLE usuarios (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				usuario VARCHAR(40) UNIQUE NOT NULL,
				nombres VARCHAR(40) NOT NULL,
				apellidos VARCHAR(40) NOT NULL,
				constrasena VARCHAR(40) NOT NULL,
				sexo VARCHAR(10) NOT NULL,
				nacimiento VARCHAR(30) NOT NULL,
				prestamos INTEGER NOT NULL,
				tipo VARCHAR(20) NOT NULL
			) """)
	except sqlite3.OperationalError:
		print("La tabla 'usuarios' ya existe.")
	else:
		print("La tabla 'usuarios' se ha creado.")

	try:
		db.execute("""CREATE TABLE libros (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(40) NOT NULL,
				autor VARCHAR(40) NOT NULL,
				editorial VARCHAR(40) NOT NULL,
				genero VARCHAR(30) NOT NULL,
				descripcion TEXT,
				ejemplares VARCHAR(40) NOT NULL

			) """)
	except sqlite3.OperationalError:
		print("La tabla 'libros' ya existe.")
	else:
		print("La tabla 'libros' se ha creado.")

	conexion.close()

def registrar_usuario(u, n, a, c, s, b, t):

	conexion = sqlite3.connect(nombre_db)
	db = conexion.cursor()

	try:
		db.execute("INSERT INTO usuarios VALUES (null, '{}', '{}', '{}', '{}', '{}', '{}', 0, '{}')"\
			.format(u, n, a, c, s, b, t))
	except sqlite3.IntegrityError:
		print("Error: El nombre de usuario '{}' ya existe.".format(u))
	else:
		print("Registro exitoso,", n)

	conexion.commit()
	conexion.close()

def registrar_libro(n, a, e, g, d, ej):
	conexion = sqlite3.connect(nombre_db)
	db = conexion.cursor()

	db.execute("INSERT INTO libros VALUES (null, '{}', '{}', '{}', '{}', '{}', {})".format(n, a, e, g, d, ej))

	conexion.commit()
	conexion.close()

def traer_usuario(nombre_usuario):

	conexion = sqlite3.connect(nombre_db)
	db = conexion.cursor()

	valor = db.execute("SELECT * FROM usuarios WHERE usuario='{}'".format(nombre_usuario)).fetchone()

	conexion.close()

	return valor

def traer_todos_libros():

	conexion = sqlite3.connect(nombre_db)
	db = conexion.cursor()

	lista_libros = db.execute("SELECT * FROM libros").fetchall()

	conexion.close()

	return lista_libros

def traer_libros(campo, dato):

	conexion = sqlite3.connect(nombre_db)
	db = conexion.cursor()

	info = db.execute("SELECT * FROM libros WHERE {}='{}'".format(campo, dato)).fetchall()

	conexion.close()

	return info

def eliminar_libro(id_libro):

	conexion = sqlite3.connect(nombre_db)
	db = conexion.cursor()

	db.execute("DELETE FROM libros WHERE id={}".format(id_libro))

	conexion.commit()
	conexion.close()