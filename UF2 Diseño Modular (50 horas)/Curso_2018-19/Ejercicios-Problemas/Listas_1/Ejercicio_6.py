#!/usr/bin/env python
# -*- coding: utf-8 -*-

contar = int(input("Cuántas palabras tiene esta lista: "))

if contar <= 0:
    print("Eso es imposible")
else:
    lista_6 = []
    for a in range(contar):
        print("Dime la palabra ",str(a+1),":",end=" ")
        palabra = input()
        lista_6.append(palabra)
    print("La lista creada es: ",lista_6)
    
    inversa = []
    for b in lista_6:
        inversa = [b] + inversa
    print("La lista inversa es: ", inversa)