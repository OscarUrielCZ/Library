"""Programa para gestionar una biblioteca."""

from os import system
from datetime import datetime

import sgbd
from catalogo import monitorea
from funciones import *

# funciones

def menu_logout():
	print("-- MENÚ --")
	print("1) Catálogo.")
	print("2) Iniciar sesión.")
	print("3) Registrarse.")
	print("")
	print("0) Salir.")

def menu_login_admin():
	print("-- MENÚ --")
	print("1) Catálogo.")
	print("2) Registrar un libro.")
	print("3) Borrar un libro.")
	print("4) Ver usuarios.")
	print("5) Borrar usuarios.")
	print("6) Ver perfil.")
	print("7) Cerrar sesión.")
	print("")
	print("0) Salir.")


def pedir_datos_usuario_signup():
	usuario = input("Nombre de usuario\n> ")
	nombre = input("Nombre(s)\n> ")
	apellidos = input("Apellidos\n> ")
	contrasena = pedir_contrasena()
	sexo = pedir_sexo()
	nacimiento = pedir_nacimiento()
	tipo = pedir_tipo_usuario()

	return usuario, nombre, apellidos, contrasena, sexo, nacimiento, tipo

def pedir_datos_libro_signup():
	nombre = input("Nombre\n> ")
	autor = input("Autor\n> ")
	editorial = input("Editorial\n> ")
	genero = input("Genero\n> ")
	descripcion = input("Descripción\n> ")
	ejemplares = pedir_entero("Ejemplares\n> ", 0, 1000)

	return nombre, autor, editorial, genero, descripcion, ejemplares

def pedir_contrasena():
	while True:
		contrasena = input("Contraseña\n> ")
		repeticion = input("Repite tu contraseña\n> ")

		if contrasena == repeticion:
			break
		else:
			print("Error: Las contraseñas no coinciden.")

	return contrasena

def pedir_sexo():
	while True:
		sexo = input("Sexo [Masculino/ Femenino]\n> ")
		if sexo.lower() == "femenino":
			return "Femenino"
		elif sexo.lower() == "masculino":
			return "Masculino"

def pedir_nacimiento():
	print("Fecha de nacimiento.")
	dia = pedir_entero("Dia\n> ", 1, 31)
	mes = pedir_entero("Mes\n> ", 1, 12)
	ano = pedir_entero("Año\n> ", 1900, datetime.now().year)

	return "{}/{}/{}".format(dia, mes, ano)

def pedir_tipo_usuario():
	while True:
		tipo = input("Tipo de usuario [Administrador/ Normal]\n> ")
		if tipo.lower() == "administrador":
			return "Administrador"
		elif tipo.lower() == "normal":
			return "Normal"


def pedir_datos_login():
	usuario = input("Usuario\n> ")
	contrasena = input("Contraseña\n> ")

	return usuario, contrasena

def eliminar_libro():
	nombre_libro = input("Nombre del libro\n> ")
	libros = sgbd.traer_libros("nombre", nombre_libro)

	if len(libros) == 0:
		print("Sin resultados.")
	else:
		lista = []

		print("")
		for l in libros:
			lista.append(l[0])
			print("{}. ".format(l[0]), end='')
			imprime_libro(l)
			print("")

		op = entero_lista("Numero de libro\n> ", lista)

		sgbd.eliminar_libro(op)

# variables globales

sesion = False
opcion = None
usuario = None
tipo_usuario = None

# main

def main():
	global sesion
	global opcion
	global usuario
	global tipo_usuario

	while True:
		hora_fecha = datetime.now().strftime("%I:%M || %A, %d %B %Y")

		if usuario == None:
			print(hora_fecha.rjust(80))
		else:
			if tipo_usuario == "Administrador":
				print("Admin {} · {}".format(usuario[2], hora_fecha).rjust(80))
			else:
				print("{} · {}".format(usuario[2], hora_fecha).rjust(80))

		if sesion is False:
			menu_logout()
			opcion = pedir_entero("opcion\n> ", 0, 3)

			if opcion == 1:
				monitorea()

			elif opcion == 2: #inciar sesión
				u, c = pedir_datos_login()

				usuario = sgbd.traer_usuario(u)

				if usuario == None or c != usuario[4]:
					usuario = None
					print("Nombre de usuario o contraseña incorrectos.")
				else:
					sesion = True
					tipo_usuario = usuario[8]
					print("Bienvenid@,", usuario[2])

			elif opcion == 3: #registrarse
				u, n, a, c, s, b, t = pedir_datos_usuario_signup()
				sgbd.registrar_usuario(u, n, a, c, s, b, t)

		else:

			if tipo_usuario == "Administrador":
				menu_login_admin()
				opcion = pedir_entero("Opción\n> ", 0, 7)

				if opcion == 1:
					monitorea()
				elif opcion == 2:
					n, a, e, g, d, ej = pedir_datos_libro_signup()
					sgbd.registrar_libro(n, a, e, g, d, ej)
				elif opcion == 3:
					eliminar_libro()

				elif opcion == 7:
					sesion = False
					usuario = None
					tipo_usuario = None
					print("Saliendo...")
			else:
				print("Usuario normal :D ·", usuario[8])

		if opcion == 0:
			print("Fin del programa.")
			break		

		input()
		system("clear")


if __name__ == "__main__":
	system("clear")
	#sgbd.crear_tablas()
	main()
