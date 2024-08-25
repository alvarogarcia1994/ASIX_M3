#!/usr/bin/env python
# -*- coding: utf-8 -*-

Lista = []	 

def buscar_nota(Lista):
	nota = int(input("Introduce la nota que quieras buscar: "))
	cont = 0
	for x in range(0,len(Lista)):
		if Lista[x]==nota:
			cont += 1
		return x	
	Lista = []
	print("Aparece ",cont,"veces")

def cambiar_nota(Lista):
	pos = int(input("Introduce una posición: "))
	nota = int(input("Introduce otra nota: "))
	Lista[pos] = nota

def vaciar_notas(Lista):
	del Lista [:]

def mostrar_notas(Lista):
	if len(Lista) > 0:
		for j in range(len(Lista)):
			if j == len(Lista)-1:
				print(Lista[j])
			else:
				print(Lista[j],",", end=" ")
	else:
		print("No hay notas")

def afegir_nota(Lista):
	nota = int(input("Introducir una nota: "))
	Lista.append(nota)
	
def aprobar_todos(Lista):
	for j in range(len(Lista)):
		if Lista[j] < 5:
			Lista[j] = 5

def insertar_nota(Lista, pos, nota):
	Lista[pos] = nota

def eliminar_nota(Lista, pos):
	Lista.pop(pos)

def ordenar_notas(Lista):
	Lista.sort()
	
def ayuda():
	print("m): Esta opción mostrará todas las notas guardadas en la array")
	print("c): Al seleccionar esta opción podrás mover una nota de una posición a otra")
	print("a): Sirve para añadir una nueva calificación en la array")
	print("b): Esta opción limpia las notas de la matriz")
	print("t): Otorgar una calificación de 5 a todos los alumnos que estén suspensos")
	print("d): Localizar una calificación en concreto")
	print("i): Inserta una nota a partir de la posición especificada por el usuario")
	print("e): Elimina una nota a partir de la posición especificada por el usuario")
	print("o): Ordena en orden ascendiente las notas guardadas en la array")
	print("?): Muestra la ayuda de todas las opciones posibles ")
	print("x): Cierra el programa")
	
def final():
	print()

def menu():
	print("m) Mostrar notas")
	print("c) Cambiar nota de posición")
	print("a) Añadir una nota a la lista")
	print("b) Vaciar las notas")
	print("t) Aprobar a todos")
	print("d) Buscar una nota")
	print("i) Insertar una nota")
	print("e) Eliminar una nota")
	print("o) Ordenar notas")
	print("?) Ayuda ")
	print("x) Finalizar ejecución")

menu()
opc = str(input("Que tipo de operación desea realizar: "))
 
while opc != "x":
	if (opc == "m"):
		mostrar_notas(Lista)
	elif (opc == "c"):
		cambiar_nota(Lista)
	elif (opc == "a"):
		afegir_nota(Lista)    
	elif (opc == "b"):
		vaciar_notas(Lista)
	elif (opc == "t"):
		aprobar_todos(Lista)
	elif (opc == "d"):
		buscar_nota(Lista)
	elif (opc == "i"):
		pos = int(input("Introduce una posición: "))
		nota = int(input("Introduce otra nota: "))
		insertar_nota(Lista, pos, nota)
	elif (opc == "e"):
		pos = int(input("Introduce la posición de la nota que quieras suprimir: "))
		eliminar_nota(Lista, pos)
	elif (opc == "o"):
		ordenar_notas(Lista)
	elif (opc == "?"):
		ayuda()
	elif (opc == "x"):
		final()
	opc = str(input("Que tipo de operación desea realizar: "))

    	
