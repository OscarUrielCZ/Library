import sgbd
from funciones import *

def menu():
	print("--CATÁLOGO--")
	print("1) Ver todos los libros.")
	print("2) Buscar un libro por nombre.")
	print("3) Buscar genero.")
	print("4) Buscar autor.")
	print("5) Buscar editorial.")

def imprimir_libros(lista):
	for l in lista:
		imprime_libro(l)
		print("")

def monitorea():
	lista_libros = sgbd.traer_todos_libros()

	menu()
	opcion = pedir_entero("Opción\n> ", 1, 5)

	if opcion == 1:
		info = lista_libros
	elif opcion == 2:
		campo = input("Nombre del libro\n> ")
		info = sgbd.traer_libros("nombre", campo)
	elif opcion == 3:
		campo = input("Genero\n> ")
		info = sgbd.traer_libros("genero", campo)
	elif opcion == 4:
		campo = input("Autor\n> ")
		info = sgbd.traer_libros("autor", campo)
	elif opcion == 5:
		campo = input("Editorial\n> ")
		info = sgbd.traer_libros("editorial", campo)

	print("")
	if len(info) == 0:
		print("No hay resultados.")
	else:
		imprimir_libros(info)
