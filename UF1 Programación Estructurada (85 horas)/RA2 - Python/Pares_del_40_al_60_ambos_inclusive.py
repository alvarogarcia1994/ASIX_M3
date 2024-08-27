#Imprimir los numeros pares del 40 al 60 ambos inclusive

#variables
n = 40
h = ''
while n <= 60:
	if n%2 == 0:
		h += ' %i' % n
	n += 1
print(h)
