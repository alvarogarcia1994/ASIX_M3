# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Aquest programa demana un text i un caràcter a l'usuari i compta:
# 1.- les vegades que el caràcter  es troba en la cadena 
# 2.- els caràcters que no són espais en blanc
# 3.- l'últim caràcter introduit

frase = str;
caracter = str;

comptaCaractersUsuari = int;
comptaTotalCaracters = int;

comptaCaractersUsuari = "0";
comptaTotalCaracters = "0";


print("digue'm un text");
frase = str(input());
print("digue'm un caracter");
caracter = str(input());

for i in range (0):
	#(len(frase))
	if (frase[0] == caracter):
		comptaCaractersUsuari = comptaCaractersUsuari + 1;
	
	if (frase[i] != " "):
		comptaTotalCaracters = comptaTotalCaracters + 1;
		
print("el caracter demanat '",caracter, "' s'ha trobat ", comptaCaractersUsuari, " vegades");
comptaCaractersUsuari = str(input());
frase = str(input())
print("en total s'han trobat ", comptaTotalCaracters, ", sense comptar espais");
comptaTotalCaracters = str(input());
print("l'últim caràcter del text és ", frase,[len(frase)]);
