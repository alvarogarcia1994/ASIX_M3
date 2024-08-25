#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Variables
Text = str;
caracter = str;
enter = int;
contador = 0;

#Función
def detectaLletra(Text, caracter, enter):
	
	if (caracter == Text):
		for a in Text:
			if (contador == enter):
				print("Sí");
			else:
				print("No");

Text = str(input("Introduce un texto: "));
caracter = str(input("Introduce un caracter: "));
enter = int(input("Introduce un entero: "));
detectaLletra(Text, caracter, enter)
