import os
import math

def suma(a,b):
	return a+b
	 
def resta(a,b):
	return a-b

def multiplica(a,b):
	return a*b

def dividir(a,b):
	return a/b


preg = str(input("Desea hacer algún tipo de operación Si o No: "))
while preg != "No":
	a = int(input("Introduce un número: "))
	b = int(input("Introduce otro número: "))
	operacion_mat = str(input("Elige un tipo de operación aritmética: sumar, restar, multiplicar o dividir\n:  "))
	
	if operacion_mat == "sumar":
		sumar = suma(a,b) 
		print (sumar)
	
	elif operacion_mat == "restar":
		restar = resta(a,b)
		print (restar)
	
	elif operacion_mat == "multiplicar":
		multiplicar = multiplica(a,b)
		print (multiplicar)
	
	elif operacion_mat == "dividir":
		divide = dividir(a,b)
		print (dividir)
		
	
	preg = str(input("Quieres hacer otra operación Si o No: "))
	
else:
	print("Hasta pronto !!!! ")
