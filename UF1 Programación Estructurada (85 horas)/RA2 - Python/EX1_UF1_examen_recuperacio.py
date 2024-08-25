# !/usr/bin/python
# -*- coding: utf-8 -*-
import random;
import os;

#Variable para definir los números.
num = int;
#Matriz
matriu = [	[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			];
			
# A partir d'aquí va el teu codi...
# Cal que es reompli ta laula de 5x6 que tens a dalt amb números aleatoris
# de 1 al 8.
# Imprimirem la taula.
# Després cal demanar a l'usuari un número de 1 a 8 i el programa ha de trobar
# tots els que coincideixin i substitruir-los a la taula per un 9.
# Tornar a imprimir la taula.
# Les impressions han de ser amb el següent format:
#  x x x x x x
#  x x x x x x 
#  x x x x x x 
#  x x x x x x 
#  on cada x és un dels nombres.

#Creamos 2 bucles for: el primero para definir las filas y el segundo para definir las columnas
for a in range(0,5):
	
	for b in range(0,6):
		#Ahora modificamos la matriz para que solo hayan valores númericos comprendidos entre el 1 y el 8
		matriu[a][b]= random.randrange(1,8);

#Inicio de los 2 bucles para que imprima la matriz al iniciar el programa
for a in range(0,5):
	print();
	for b in range(0,6):
		print(matriu[a][b], end=" ");
print();
#Al ejecutar el programa, el mismo nos pedirá que introduzcamos un valor comprendido entre 1 y 8
print("Introduzca un número del 1 al 8");
num = int(input());
#Añadimos un while para evitar que el usuario introduzca el 0 o el 9
while (num == 0 or num == 9):
	print("ERROR, Solo se admiten valores entre 1 y 8");
	num = int(input());
while(num is 1-8):
#El programa volverá a ejecutar los dos bucles for para correr la matriz
	for a in range(0,5):
	#Tras el segundo bucle añadimos un if para indicarle al programa debe substituir por un 9 los números que coincidan
		for b in range(0,6):
			if (matriu[a][b]==num):
				matriu[a][b]=="9";

#Último recorrido de los 2 bucles for.			
for a in range(0,5):
	print();
	for b in range(0,6):
		print(matriu[a][b], end=" ");		
