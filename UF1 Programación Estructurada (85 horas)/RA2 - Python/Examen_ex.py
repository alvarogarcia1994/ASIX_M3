# !/usr/bin/python
# -*- coding: utf-8 -*-

import os;

nom = str;
matriu1 = [	["Adrian", "Ernest", "Pau", "Albert", "Sergi"],
			["Carlos", "Gines", "Oriol", "Alvaro", "Jaume"],
			["Ruben", "Oscar", "Marc", "Kevin", "Julio"],
			["Jiasheng", "Ivo", "Iosif", "Hong", "Hector"],
			["Farhan", "Eric", "Cristian", "Atif", "Alejandro"],
			]

# A partir d'aquí va el teu codi...

# El primer que es demana és que imprimiu la taula 

# sí la impresió es fa per columnes, és a dir... 

# Adrian Carlos Ruben Jiasheng Farhan
# Ernest Gines Oscar Ivo Eric
# Pau Oriol Marc Iosif Cristian
# Albert Alvaro Kevin Hong Atif
# Sergi Jaume Julio Hector Alejandro

# L'exercici serà considerat òptim. Si la impresió es fa per fileres, 
# descomptarà una mica en la nota final


# Després cal demanar a l'usuari una lletra i el programa ha de trobar
# tots els noms que continguin la lletra demanada (majúscula o minúscula)
# i imprimir-los de tres maneres:

# 1.- tot el nom en majúscules
# 2.- tot el nom en minúscules
# 3.- La primera lletra minúscula i la resta majúscules
# Recordeu les funcions de tractament de Strings:  upper()  lower()  len()
# No cal guardar els noms trobats en cap taula o estructura similar.
# A mesura que es van trobant, s'han d'anar imprimint en les tres maneres.

#Definimos la tabla con un bucle for
for i in range(0,5):
	
	for x in range(0,5):
		matriu1[i][x]= nom.lower(10);

		
for i in range(0,5):
	print();
	for x in range(0,5):
		print(matriu1[i][x], end=" ");

#Salto de linea
print();
#Hay que introducir nombe
print("Digue'm un nom");
nom = str(input());

for i in range(0,5):

	for x in range(0,5):
		if(matriu1[i][x]==nom.lower(10)):
		   matriu1[i][x]==" ";


for i in range(0,5):
	print();
	for x in range(0,5):
		print(matriu[x][i], end=" ");		   
		  
			
		

