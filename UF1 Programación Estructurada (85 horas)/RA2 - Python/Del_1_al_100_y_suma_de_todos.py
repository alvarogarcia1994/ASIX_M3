#Imprimir los numeros del 1 al 100 y calcular la suma de todos los numeros
###pares por un lado, y por otro, la de los impares.

#variables
n = 1
p = 0
i = 0

#calculos
while n <= 100:
	print (n),
	if n%2 == 0:
		p += n
	else:
		i += n
	n += 1
print ('La suma de los numeros pares es igual a %i' %p)
print ('La suma de los numeros impares es igual a %i' %i)
