#!/usr/bin/env python
# -*- coding: utf-8 -*-
ListaNotas = []
continuar = "s"

while continuar == "s":
	nota = int(input("Introduce una nota: "))
	ListaNotas.append(nota)
	if nota < 0 or nota > 10:
		print("Error, vuelve a introducir una nota entre 0 y 10: ")
	continuar = input("Deseas introducir otra nota: (s/n)")
	if continuar !="s" and continuar !="n":
		print("Opción incorrecta")
print(ListaNotas)
pos = int(input("Introduce una posición: "))
nota = int(input("Introduce otra nota: "))
ListaNotas.insert(pos, nota)
print(ListaNotas)
