#Imprimir los numeros impares del 1 al 25, ambos inclusive

#Variables
n = 1
h = ''
while n <= 25:
	if n%2 != 0:
		h += ' %i' % n
	n += 1
print h
