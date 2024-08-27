#Creamos una tabla
tabla=[]

# Ahora definimos que al iniciar el programa, pida al usuario 10 números enteros
for a in range(1, 11):
	numero = int(input("Introduce el numero ", str(a+1),": " ))
	if (numero % 2 == 0):
		print("El número ", numero, "es par")
