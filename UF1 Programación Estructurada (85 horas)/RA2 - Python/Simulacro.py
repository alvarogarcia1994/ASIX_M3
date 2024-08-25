# !/usr/bin/python
# -*- coding: utf-8 -*-
import random;
import os;

num1 = int;
matriu = [	[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			];
			
# A partir d'aquí va el teu codi...
# Cal que es reompli ta laula de 4x4 que tens a dalt amb números aleatoris
# de 0 a 9.
# Imprimirem la taula.
# Després cal demanar a l'usuari un número de 0 a 9 i el programa ha de trobar
# tots els que coincideixin i substitruir-los a la taula per una @.
# Tornar a imprimir la taula.
# Les impressions han de ser amb el següent format:
#  x x x x 
#  x x x x 
#  x x x x 
#  x x x x 
#  on cada x és un dels nombres o bé, la @.


for i in range(0,4):
	
	for x in range(0,4):
		matriu[i][x]= random.randrange(10);
		
for i in range(0,4):
	print();
	for x in range(0,4):
		print(matriu[i][x], end=" ");
print();
print("Dime un número")
num1 = int(input());

for i in range(0,4):
	
	for x in range(0,4):
		if (matriu[i][x]==num1):
			matriu[i][x]=="@";
		
for i in range(0,4):
	print();
	for x in range(0,4):
		print(matriu[x][i], end=" ");		
