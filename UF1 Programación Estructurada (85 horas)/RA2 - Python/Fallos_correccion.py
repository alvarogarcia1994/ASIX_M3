frase = str;
caracter = str;

comptaCaractersUsuari = int;
comptaTotalCaracters = int;

comptaCaracterUsuari = 0;
comptaTotalCaracters = 0;

print("dime un texto");
frase = str(input());
print("dime un carácter");
caracter = str(input());

for i in range (0, len(frase) );
	if (frase[0]==caracter):
		comptaCaracterUsuari = comptaCaractersUsuari + 1;

	if (frase[i]!=" "):
		comptaTotalCaracters = comptaTotalCaracters + 1;

print("el caracter demanat '",caracter, "' s'ha trobat ", comptaCaractersUsuari, " vegades");
print("en total s'han trobat ", comptaTotalCaracters, " sense comptar espais");
print("l'últim caràcter del text és ", frase,[len(frase)]);

