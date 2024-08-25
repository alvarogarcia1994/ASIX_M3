#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma(x,y):
	z = x+y
	return z
	
x = int(input("Introduce un número: "))
y = int(input("Introduce otro número: "))
z = int(input("Introduce otro número: "))
a = suma(x,y)
b = suma(a,z)
print (b)
