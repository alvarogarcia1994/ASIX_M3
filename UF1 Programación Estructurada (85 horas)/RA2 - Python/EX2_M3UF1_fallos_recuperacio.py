# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Aquest programa demana un número i un text. Després de convertir el text 
# a majúscules ho imprimeix tantes vegades com el número demanat seguits
# i separats per un guió.

num = int;
text = str;


print("digue'm un número");
num = int(input());
print("digue'm un text");
text = str(input());

text = text.lower();

for i in range (0,num):			
		print (text, end=" ");
		if (i != num):
			print("-", end=" ");
