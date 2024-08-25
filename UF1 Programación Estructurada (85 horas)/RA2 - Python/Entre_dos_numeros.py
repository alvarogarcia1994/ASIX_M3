#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Variables
numA = int
numB = int

#Inicio
numA = int(input("Introduce un número: "));
numB = int(input("Introduce otro número: "));

#Bucle
if int(numA) > int(numB):
	print("El número más grande entre", numA, "y", numB, "es", numA);
	
elif numA<numB:
	print("El número más grande entre", numA, "y", numB, "es", numB);
	
else: 
	print("Los números son iguales");
