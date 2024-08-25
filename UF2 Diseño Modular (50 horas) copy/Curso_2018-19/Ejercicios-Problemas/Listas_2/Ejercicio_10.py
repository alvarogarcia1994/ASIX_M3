#!/usr/bin/env python
# -*- coding: utf-8 -*-

numero = int(input("Dime un número: "))
cont = 0

if numero < 1:
    print("Eso no tiene sentido")
else:
    divisores = []
    for a in range(1,numero+1):
        if numero % a == 0:
            cont += 1
            divisores += [a]
            
    print("Este número tiene ",cont," divisores: ", divisores)
        