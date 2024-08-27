stringGran = str; 
stringPetit = str;


comptadorNum = int(0);
trobat = 0;


print("digue'm un text")
stringGran = str(input())
print("digue'm què he de trobar")
stringPetit = str(input())



#començo iteració
for i in range(0, len(stringGran)-1):
	print("recorrent principal ",i, stringGran[i]); 
	if stringGran[i] == stringPetit[0]:
		
		print("dintre principal", stringGran[0], stringPetit[0])
		input();
		trobat = 1;
		for x in range(1,len(stringPetit)):
			 
			print("recorrent petit", x, len(stringPetit));
			print("xivato false", i, x, stringGran[i+x], stringPetit[x]);
			 
			input()
			if ((stringGran[i+x] != stringPetit[x]) or trobat==0):
				print("no trobat");
				trobat = 0;
				 
		if trobat:
			print ("encert", comptadorNum);
			comptadorNum = comptadorNum + 1;
					
print(comptadorNum);
