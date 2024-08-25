#Abrir y leer


try:
	file = open("/home/alvaro/M4UF2exercici45/acta.xsd", "r");
except FileNotFoundError:
	print("NO SE ENCUENTRA EL ARCHIVO");
	
texto = str;

#Leer todo el documento
texto = file.read();
print(texto);

#Leer una linea
file.seek(0);
print();
text = file.readline();
print(text);
	


file.close();
