###Programa que pida introducir al usuario un numero y 

#Inicio de la ejecución
import math

#Bloque de variables y datos que saldrán al ejecutar el programa
#Pedirá que introduzcamos un número
num = int()
print ("Introduce un número:")
num = int(input())

#Ejecución de la raíz cuadrada
while num != 9999 :
	print ("Su cuadrado es:")
	print (num**2)
	if num > 0 :
		print ("Su raíz cuadrada es:")
		print (num**(1/2))
	if num < 0 :
		print ("Su raíz cuadrada es:")
		print ("Math Error")
	print ("Introduce otro número:")
	num = int(input())
print ("Fin del programa")

#Primer he definit el número com enter, després he posat un bucle while per 
