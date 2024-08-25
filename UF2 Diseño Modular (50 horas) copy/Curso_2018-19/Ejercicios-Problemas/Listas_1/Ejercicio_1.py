#!/usr/bin/env python
# -*- coding: utf-8 -*-

cont = int(input("Dime cuántas palabras hay en esta lista: "))

if cont <= 0:
    print("Imposible!")
else:
    lista = []
    for x in range(cont):
        print("Dime la palabra ", str(x+1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)