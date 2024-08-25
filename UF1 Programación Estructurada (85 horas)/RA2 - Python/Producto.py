#Programa que pide al usuario dos números positivos o negativos y le indique si su producto es 0, mas grande o mas pequeño que 0

#El primer paso es introducir las variables y después con la función input entre paréntesis escribimos una frase.
#Una frase que pida al usuario introducir 2 números.
#Variables
num1 = int(input("introduce un numero: "));
num2 = int(input("introduce otro numero: "));

#Ahora hay hacer que el programa calcule el producto de los 2 números. Para ello introduciremos 3 veces la función IF.
#Para que en cada uno de los 3 casos, el programa indique si el producto es igual, mayor o menor que 0.
if (num1*num2) == 0:
	print("El producto es igual a 0")

if (num1*num2) > 0:
	print("El producto es mayor que 0")
	
if (num1*num2) < 0:
	print("El producto es menor que 0")

#Hemos conseguido hacer un programa que al cálcular el producto de los 2 números indique si es igual, mayor o menor que 0.
