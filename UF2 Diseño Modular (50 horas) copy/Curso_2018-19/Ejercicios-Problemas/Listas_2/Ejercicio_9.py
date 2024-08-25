#!/usr/bin/env python
# -*- coding: utf-8 -*-

numero = int(input("Dime cuántas palabras tiene esta lista: "))

if numero < 1:
    print("Eso es imposible")
else:
    lista_9 = []
    for a in range(numero):
        print("Dime la palabra ",str(a+1),":",end=" ")
        palabra = input()
        lista_9 += [palabra]
    print("La lista generada es: ", lista_9)
    
    for b in range(len(lista_9)):
        if lista_9[b] in lista_9[b]:
            lista_9.sort()
       
    print("La lista ordenada es: ",lista_9)        