#!/usr/bin/env python
# -*- coding: utf-8 -*-  

def iniciales_mayusculas(nombre):
	nombre = nombre.title()
	
	return nombre

nombre = str(input("Introduce tu nombre: "));

print(iniciales_mayusculas(nombre))
