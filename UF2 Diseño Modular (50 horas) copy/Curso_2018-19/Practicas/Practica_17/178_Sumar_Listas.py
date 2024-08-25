#!/usr/bin/env python
# -*- coding: utf-8 -*-

Lista1 = []
Lista2 = []
Lista3 = []

A=int(input("Introduce un número, Lista 1: "))
B=int(input("Introduce un número, Lista 2: "))

for i in range(0,10):
	
	Lista1.append(A+i)
	Lista2.append(B+i)
	Lista3.append(A+i+B+i)

print(Lista1)
print(Lista2)
print(Lista3)
