### Imprimir y contar los numeros multiplos de 3 que hay entre 1 y 100.

#variables
n = 1
h = 0

while n < 100:
    if n%3 == 0:
        print (n),
        h += 1
    n += 1
print ('\nEntre 1 y 100 hay %i numeros multiplos de 3' % h)
