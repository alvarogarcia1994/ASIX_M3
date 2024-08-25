# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Aquest programa demana dos números i troba tots els números que hi 
# ha entre ells i que són múltiples de 2 i de 3, alhora, sense comptar els 
# dos números.

import math;
num1 = int;
num2 = int;


print("digue'm un número");
num1 = int(input());
print("digue'm un altre");
num2 = int(input());

for i in range (num1+1,num2):
	if (i%2 == 0) and (i%3 == 0):		
		print (i, " és múltiple de 2 i 3 alhora");
