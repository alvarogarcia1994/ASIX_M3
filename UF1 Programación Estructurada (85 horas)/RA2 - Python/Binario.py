#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

#variables
numero = int
numero = int(input("Define un numero ")); 
binario = ""

#Ahora creamos el bucle para que el programa al introducir un número del 0 al 255. Lo transforme en binario
#Con la función IF especificamos hasta que número podemos convertir (máximo 255) 
if (numero) > 255:
	print ("ERROR. El número es mayor que 255")
#Si nos pasamos de 255, el programa enviará al usuario un mensaje de error
else:
	#Aquí definimos el bucle while, que SOLO se ejecutará mientras introduzcamos un número menor que 255. 
	while(numero) > 0:
		if (numero%2) == 0:
			binario = "0" + binario
		else:
			binario = "1" + binario
		numero = int(math.floor(numero/2))
	print("El resultado de la conversion es: "+binario)
print ("fin programa")
#Ya hemos construido un programa que pase un número decimal a binario.
#Si el número está entre 0 y 255 sale el 2do y el 3er print.
#Si el número es mayor que 255 saldrá el mensaje de error que hemos definido en la linea 14 y el 3er print.
