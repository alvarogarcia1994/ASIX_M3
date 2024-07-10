#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

#definició de funcions

def llegeixEnter():
	
	error = int;
	num = int;
	
	error = 1;
	
	while error:		
		try:			
			num = int(input("Introdueix un nombre enter... "));
			error = 0;
		except:
			print("El valor introduït no és correcte, torna-hi!!!");
	
	return num;
	
def llegeixEnterInterval(num1, num2):
	
	error = int;
	num = int;
	
	error = 1;
	
	while error:		
		try:			
			num = int(input("Introdueix un nombre enter... "));
			if (num>=num1 and  num<=num2):
				error = 0;
		except:
			print("El valor introduït no és correcte, torna-hi!!!");
	
	return num;

def llegeixText():
	
	error = int;
	texto = str;
	
	error = 1;
	
	while error:		
		try:			
			texto = input("Introdueix un text... ");
			error = 0;
		except:
			print("El valor introduït no és correcte, torna-hi!!!");
	
	return texto;

#programa principal.........

#definició de variables

a= int;
b= int;
suma = int;
text = str;

a = llegeixEnter();
i1=6;
i2=12
b = llegeixEnterInterval(i1, i2);

text = llegeixText();

suma = a+b;

print(text, " ", suma);
