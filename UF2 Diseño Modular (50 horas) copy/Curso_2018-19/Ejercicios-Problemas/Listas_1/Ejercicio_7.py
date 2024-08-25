#!/usr/bin/env python
# -*- coding: utf-8 -*-

contar = int(input("Dime cuántas palabras hay en esta lista: "))

if contar <= 0:
    print("Imposible")
else:
    lista_7 = []
    for a in range(contar):
        print("Dime la palabra ",str(a+1),":",end=" ")
        palabra = input()
        lista_7.append(palabra)
    print("La lista es ahora: ", lista_7)
    
    for b in range(len(lista_7)-1,-1,-1):
        if lista_7[b] in lista_7[:b]:
            del(lista_7[b])
    print("La lista sin repeticiones es: ",lista_7)
            