#!/usr/bin/env python
# -*- coding: utf-8 -*-

ListaNotas = []
continuar = "s"

while continuar == "s":
	notas = int(input("Introduce una nota: "))
	ListaNotas.append(notas)
	if notas < 0 or notas > 10:
		print("Error, vuelve a introducir una nota entre 0 y 10: ")
	continuar = input("Deseas introducir otra nota: (s/n)")
	if continuar !="s" and continuar !="n":
		print("Opción incorrecta")
	
	ListaNotas.sort()

print(ListaNotas)
