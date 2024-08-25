#!/usr/bin/env python
# -*- coding: utf-8 -*-

counter = int(input("Cuántas palabras tiene esta lista: "))

if counter <= 0:
    print("Eso es imposible !!!")
else:
    lista = []
    for a in range(counter):
        print ("Dime la palabra ",str(a+1), ": ",end="")
        nombre = input()
        lista += [nombre]
    print("La lista creada es: ",lista)
    
    substituir = str(input("Dime que palabra quieres substituir: "))
    buscar = str(input("Por la palabra: "))
    
    for b in range(len(lista)):
        if lista[b] == substituir:
            lista[b] = buscar
            
    print("La lista es ahora: ",lista)