	
	
	co = int;
	cd = int;
	fo = int;
	fd = int;
	
	if (len(coordenadas)=! 5):
		return 0;
		
	fo = int(coordenadas[0]);
	co = int(coordenadas[1]);
	fd = int(coordenadas[3]);
	cd = int(coordenadas[4]);
	
	if (matriu[fo][co])[0]!=="P")
		return 0;
	else:
		if ((fd != 0) and (fd !=7)):
			return 0;
	else:
		return 1;
		

while(1):
	a = str; 
	a= llegirText();
	print("Resultado "+ a + " " + str(promocioPeo(matriu,a)));


	
	


