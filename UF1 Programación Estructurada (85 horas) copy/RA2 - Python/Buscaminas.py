#!/usr/bin/env python
# -*- coding: utf-8 -*-

# !/usr/bin/python
# -*- coding: utf-8 -*-
import random;
import os;

opcio = int;

matriu1 = [	["0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0"]
			]
filera = random.randrange(6);
columna = random.randrange(6);

#print (filera);
#print (columna);

matriu1[filera][columna]="X"

#matriu2 = [[0]*6]*6;

matriu2 = [	["0", "0", "0", "0", "0", "0"],
			["10", "11", "12", "13", "14", "15"],
			["20", "21", "22", "23", "24", "25"],
			["30", "31", "32", "33", "34", "35"],
			["40", "41", "42", "43", "44", "45"],
			["50", "51", "52", "53", "54", "55"]
			]

for i in range(0,6):
	print();
	for x in range(0,6):
		print(matriu1[i][x]," ", end="");
		matriu2[i][x]='?';
		
print();		
	
		
for i in range(0,6):
	print();
	for x in range(0,6):
		print(matriu2[i][x]," ", end="");
		

####
# Comença el joc!!!!!
####

print("prem Enter...");
input();
os.system("clear");
#os.system("cls");

print("MENU \n");

print("Situació actual del tauler de joc:");

for i in range(0,6):
	print();
	for x in range(0,6):
		print(matriu2[i][x]," ", end="");
		
		
		
noSortir=1;

while noSortir:
	os.system("clear");		
	
	for i in range(0,6):
		print();
		for x in range(0,6):
			print(matriu2[i][x]," ", end="");
	
	print("\n");		
	print("1. Resoldre el joc");
	print("2. Provar sort");
	print("3. Sortir");

	
	
	print();

	opcio = int(input());
	if opcio == 1:
		print("1");
		
	if opcio == 2:
		print("introdueix la filera...");
		filera = int(input());
		print("introdueix la columna...");
		columna = int(input());
			
		if matriu1[filera][columna]=="X":
			print("Has picat la mina. Has perdut!!!");
			noSortir=0;
		
		else:			
			valor=0;
			
			#comprovem esquerra
			if columna != 0:
				if matriu1[filera][columna-1]=="X":
					valor=1;
			
			#comprovem dreta
			if columna != 5:
				if matriu1[filera][columna+1]=="X":
					valor=1;
					
			#comprovem a dalt
			if filera != 0:
				if matriu1[filera-1][columna]=="X":
					valor=1;
			
			#comprovem a baix
			if filera != 5:
				if matriu1[filera+1][columna]=="X":
					valor=1;
		
			if valor:
				matriu2[filera][columna]="1";
			else:
				matriu2[filera][columna]="0";		
		
		
	
	if opcio == 3:
		print("Adéu!!!");
		noSortir=0;
			## codi per l'opcio 3
	else:
		print("Opció no correcta");
		#noSortir = 1;
