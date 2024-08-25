#!/usr/bin/env python
# -*- coding: utf-8 -*-

inicial = int(input("Introdueix un nombre: "))
final = int(input("Introdueix un altre nombre: "))

def calcula_suma_numeros(inicial, final):
	suma = 0
	for numero in range(inicial, final+1):
		suma = suma + numero
	return suma
suma = calcula_suma_numeros(inicial, final)
print("El resultat és: ", suma)

