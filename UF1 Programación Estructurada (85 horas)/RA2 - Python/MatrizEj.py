# !/usr/bin/python
# -*- coding: utf-8 -*-
import random;
import os;

#Bloque de variables
nom = int;

#Creamos la matriz
matriz = [	["Alvaro", "Cristian", "Jaume"],
			["Farhan", "Segio", "Julio"],
			["Gines", "Ruben", "Ivo"],
			["Alberto", "Oscar", "Jordi"],
			["Juan Carlos", "Adrian", "Hector"],
			["Miquel", "Oriol", "Pau"],
			["Jiasheng", "Hong", "Moises"],
			];

#Para correr la matriz creamos 2 bucles for, el primero para las filas y el segundo para las columnas
for a in range(0,7):
	print();
	for b in range(0,3):
		print(matriz[a][b]," ", end="");

#Al ejecutar el programa, nos pedirá que introduzcamos 1 carácter
print("dime 1 caracter");
caracter = str(input());

#Dentro de los 2 bucles definimos el contenido de la matriz
for a in range(0,7):
	for b in range(0,3):
		nom= (matriz[a][b]);
		
		#Creamos un 3er bucle for para hacer que imprima los nombres de la matriz
		for c in range(0, len(nom) ):
		#Finalmente con un if haremos que solo imprima los nombres que contengan el carácter que hemos introducido antes
				if(nom[c] == caracter):
						print (nom.upper());
						print (nom.lower());
						
						print(nom[0].lower() + nom[1:len(nom)].upper());
