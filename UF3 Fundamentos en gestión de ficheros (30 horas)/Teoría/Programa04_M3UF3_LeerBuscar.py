#Abrir y leer.
	
try:
	file = open("hola2.txt", "r");
except FileNotFoundError:
	print("NO SE ENCUENTRA EL ARCHIVO");
	
texto = str;
file.seek(0);

#Leer 1 linea
texto = file.readline();
contadorlin = int(0);
contadorA = int(0);

while (texto!=""):
	contadorA = 0;
	for a in range(0, len(texto)):
		if texto[a]=="a":
			contadorA = contadorA +1;
	print("La linea " + str(contadorlin) + " Contiene " + str(contadorA) + " a");
	contadorlin = contadorlin +1;
	texto = file.readline();
	
print ("Cerrando archivo....");
file.close()
