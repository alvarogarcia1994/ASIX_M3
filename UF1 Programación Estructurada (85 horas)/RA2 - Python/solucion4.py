frase = str;
caracter = str;

comptaCaractersUsuari = int;
comptaTotalCaracters = int;

comptaCaractersUsuari = 0;
comptaTotalCaracters = 0;

print("digue'm un text");
frase = str(input());
print("digue'm un caracter");
caracter = str(input());

for i in range(0, (len(frase))):
	if (frase[i]==caracter):
		comptaCaractersUsuari = comptaCaractersUsuari + 1;
	
	if (frase[i]!= " "):
		comptaTotalCaracters = comptaTotalCaracters + 1;
		
print("el caracter demanat ",caracter, "s'ha trobat ", comptaCaractersUsuari, "vegades ");
print("en total s'han trobat ", comptaTotalCaracters, ", sense comptar espais");
print("l'últim caràcter del text és ", frase[len(frase)-1])