#!/usr/bin/env python
# -*- coding: utf-8 -*-

nombre = str;
longitud = int;

print("Dime tu nombre");
nombre = str(input());

longitud = len(nombre);

for i in range(0, longitud):
	print(nombre[i])
