#!/usr/bin/env python
# -*- coding: utf-8 -*-

cantidad = int(input("Cuántas palabras hay en esta lista: "))

if cantidad <= 0:
    print("No es posible")
else:
    lista_4 = []
    for a in range(cantidad):
        print("Dime la palabra ",str(a+1)+":",end=" ")
        palabra = input()
        lista_4 += [palabra]
    print("La lista creada es: ", lista_4)
    
    delete = str(input("Palabra a eliminar: "))
    
    for b in range(len(lista_4)-1,-1,-1):
        if lista_4[b] == delete:
            del(lista_4[b])
    
    print("La lista es ahora: ", lista_4)