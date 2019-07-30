def pedir_entero(texto, li, ls):
	while True:
		try:
			op = int(input(texto))
		except ValueError:
			pass
		else:
			if li <= op <= ls:
				break

	return op

def imprime_libro(l):
	print("Nombre:", l[1])
	print("Autor:", l[2])
	print("Editorial:", l[3])
	print("Genero:",l[4])

	if len(l[5]) > 0:
		print("Descripción:")
		print(l[5])

	print("Ejemplares:", l[6])

def entero_lista(texto, lista):
	while True:
		try:
			op = int(input(texto))
		except ValueError:
			pass
		else:
			if op in lista:
				return op

	return op