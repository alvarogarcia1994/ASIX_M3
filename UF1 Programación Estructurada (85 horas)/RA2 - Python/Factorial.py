#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Variables
factorial = int(1);
número = int(input("> Por favor introduce el número a calcular el factorial: "));

#Incio del bucle while
while(número !=0):
	factorial = factorial * número;
	número = número - 1;
print("El factorial del número leído es: "+str(factorial));
