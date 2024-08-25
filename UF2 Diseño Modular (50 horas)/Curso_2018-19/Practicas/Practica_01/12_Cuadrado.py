#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
intro = int(input("Introduce un número mayor que 0: "))

def cuadrado():
	if intro > 0:
		for a in range(1, intro +1):
			for b in range(1,intro+1):
				print(b, end=" ")
			print()
	else: 
		print("Solo números desde el 1: ")
		
cuadrado()
