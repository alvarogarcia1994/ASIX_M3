#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Definimos el nombre de la lista que almacenará los números de la dicha sucesión
fibonacci=[]

#Creamos 3 variables las cuales se llamarán x, y, num concretamente
x=0
y=1
num = int(input("Numero de elementos:"))

#Creamos un bucle for que hará que se cree un ciclo que se repitirá X número de veces y en el mismo se van almacenando
#los números de la serie de fibonacci
for n in range(num):
    fibonacci.append(x+y)
    aux = x + y
    x = y
    y = aux

#Solo se imprimirá la lista
print(fibonacci)
