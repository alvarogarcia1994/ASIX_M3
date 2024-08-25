caracter = str;
nom = str;

for i in range(0,5):
	print();
	for  x in range(0,5):
		print(matriu1[i][x]," ", end="");
		
print("\dona un caracter");
caracter = str(input());
for i in range(0,5):
	for x in range(0,5):
		nom= (matriu1[i][x]);
		
		for n in range(0, len(nom) ):
			
			if(nom[n] == caracter):
				print (nom.upper());
				print (nom.lower());
				
				print(nom[0].lower() + nom[1:len(nom)].upper());
