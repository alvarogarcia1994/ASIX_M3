#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Bloque de variables
num = int
numA = int
numB = int
numC = int
numin = int
numax = int 


#Primera función
def numax(numA, numB, numC):
	if(numA > numB) and (numA > numC):
		numax = numA
	if(numB > numA) and (numB > numC):
		numax = numB
	if(numC > numA) and (numC > numB):
		numax = numC
	return numax

#Segunda funcion
def numin(numA, numB, numC):
	if(numA < numB) and (numA < numC):
		numin = numA
	if(numB < numA) and (numB < numC):
		numin = numB	
	if(numC < numA) and (numC < numB):
		numin = numC
	return numin

#Al ejecutarlo, el programa nos pedirá 3 números
print("Introduce el primer numero");
numA = int(input())
print();
print("Introduce el segundo numero");
numB = int(input())
print();
print("Introduce el tercer numero");
numC = int(input())

print();

numax=(numax(numA,numB,numC))
numin=(numin(numA,numB,numC))

#En función de los 3 valores que hemos introducido previamente, imprimirá y nos dirá cual es el número mayor y cual es el número menor
print("El número", numax, "Es el más grande");
print("El número", numin, "Es el más pequeño");

#Acto seguido imprimirá los 3 números
