#!/usr/bin/env python
# -*- coding: utf-8 -*-

contadorA = int(input("Cuántas palabras tiene esta lista: "))

if contadorA <= 0:
    print("Imposible!")
else:
    lista = []
    for x in range(contadorA):
        print("Dime la palabra ",str(x+1),": ",end="")
        palabra = input()
        lista.append(palabra)
    print("La lista creada es: ", lista)
    
    buscador = str(input("Dime la palabra que quieres que busque: "))
    cont = 0
    
    for y in lista:
        if y == buscador:
            cont += 1
    if cont == 0:
        print("Esta palabra no está en esta lista")
    elif cont == 1:
        print("Esta palabra aparece una vez en esta lista")
    elif cont >= 2:
        print("Esta palabra aparece ",cont," veces en esta lista") 