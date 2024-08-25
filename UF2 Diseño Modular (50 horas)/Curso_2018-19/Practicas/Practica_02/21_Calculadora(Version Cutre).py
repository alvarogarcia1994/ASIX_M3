#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math

#Variables
a = int;
b = int;

#Main Menu
def menu_principal():
	print("####Calculadora de Álvaro######")
	print("Menú principal\n")
	print("1. Sumar")
	print("2. Restar")
	print("3. Multiplicar")
	print("4. Dividir")
	print("5. Salir")

#Calculadora
def Calculadora():
	#Llamamos a la primera función
	menu_principal()
	opcion = int(input("Por favor, elige una opción\n"))
	while (opcion > 0 and opcion < 5):
		a = float(input("Introduce un número: "))
		b = float(input("Introduce otro número: "))
		if (opcion == 1):
			print("La suma de los dos números introducidos es: ", a+b)
			opcion = int(input("Por favor, elige una opción\n"))
		elif (opcion == 2):
			print("La resta de los dos números introducidos es: ", a-b)
			opcion = int(input("Por favor, elige una opción\n"))
		elif (opcion == 3):
			print("La multiplicación de los dos números introducidos es: ", a*b)
			opcion = int(input("Por favor, elige una opción\n"))
		elif (opcion == 4):
			try:
				print("La división de los dos números introducidos es: ", a/b)
				opcion = int(input("Por favor, elige una opción\n"))
			except ZeroDivisionError:
				print("Lo siento, no puedo dividir entre 0 ")
				opcion = int(input("Por favor, elige una opción\n"))
Calculadora()
		
		
		
		
