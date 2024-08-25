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
print(ListaNotas)
nota = int(input("Introduce la nota que quieras buscar: "))

cont = 0
for x in range(0,len(ListaNotas)):
	if ListaNotas[x]==nota:
		cont += 1
		print(x)

Lista2 = []

print("Aparece ",cont,"veces")
