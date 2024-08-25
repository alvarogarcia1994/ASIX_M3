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
	
	if cont != "s" and cont != "n":
		print("Opción incorrecta")

for i in range(a-1,-1,-1):
	print(" ",ListaNotas[i], end=" ")
