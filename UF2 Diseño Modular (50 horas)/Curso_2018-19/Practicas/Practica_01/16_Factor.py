#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factor(numA, numB, numC, numD):
	A = numA*numB
	B = numA*numC
	C = numA*numD
	D = numB*numC
	E = numB*numD
	F = numC*numD
	return(max(A,B,C,D,E,F))
	
numA = int(input("Introduce un número: "))
numB = int(input("Introduce un número: "))
numC = int(input("Introduce un número: "))
numD = int(input("Introduce un número: "))

print(factor(numA,numB,numC,numD))
