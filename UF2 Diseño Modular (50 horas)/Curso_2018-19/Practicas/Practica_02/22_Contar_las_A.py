#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def cuenta_A(texto):
	cont = int()
	for a in range(len(texto)):
		if texto[a] == "a" or texto[a] == "A":
		    cont += 1
	return cont

texto = str(input("Introduce un texto: "))
cont = int

print(cuenta_A(texto))
