#!/usr/bin/env python
# -*- coding: utf-8 -*-

ListaNotas = []
cont = "s"
a=0

while cont == "s":
	nota = int(input("Introducir una nota: "))
	ListaNotas.append(nota)
	if nota > 10 or nota < 0:
		print("Error, solo se aceptan notas del 0 al 10, por favor, introduce una nota comprendida entre 0 y 10")
	cont = input("Quieres introducir otra nota (s/n)")
	a=a+1
	print(ListaNotas)
	
	if cont != "s" and cont != "n":
		print("Opción incorrecta")
print(ListaNotas[0],end=" ")
for i in range (1,a):
	print(",",ListaNotas[i], end=" ")
	
