#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Variable inicial
uno = int(input("Dime cuántos elementos hay en esta lista: "))

#Validacion de la variable necesaria, para poder añadir esos valores a la lista
if uno <= 0:
    print("Eso es imposible")
else:
    lista_81 = []
    #Si la validación es correcta introduciremos valores y recorremos la lista
    for a in range(uno):
        print("Dime la palabra ",str(a+1),":",end=" ")
        palabra = input()
        lista_81 += [palabra]
    
    #Nuevamente volvemos a recorrer la lista, pero al revés.
    for b in range(len(lista_81)-1,-1,-1):
        if lista_81[b] in lista_81[:b]:
            #Si algun elemento se repite será eliminado
            del(lista_81[b])
    print("La primera lista sin repeticiones es: ",lista_81)
    
    #Necesitamos una segunda variable para validar la segunda lista
    dos = int(input("Dime cuántos elementos hay en esta lista: "))
    
    if dos <= 0:
        print("Eso es imposible")
    else:
        lista_82 = []
        #Incio segunda lista
        for c in range(dos):
            print("Dime la palabra ",str(c+1),":",end=" ")
            word = input()
            lista_82 += [word]
        
        #Repito el mismo proceso que hice con la primera lista
        for d in range(len(lista_82)-1,-1,-1):
            if lista_82[d] in lista_82[:d]:
                del(lista_82[d])
        print("La segunda lista sin repeticiones es: ",lista_82)
        
        #Es esta tercera lista se añadirán las palabras que hayan salido en ambas listas
        comunes = []
        for e in lista_81:
            if e in lista_82:
                comunes += [e]
        print("Aparece en todas las listas: ", comunes)
        
        #En la cuarta lista solo queremos las palabras de la primera
        solo_81 = []
        for f in lista_81:
            if f not in lista_82:
                solo_81 += [f]
        print("Estas palabras solo están en la primera lista: ",solo_81)
        
        #En la quinta, solo nos interesan las palabras que hayan salido en la segunda
        solo_82 = []
        for g in lista_82:
            if g not in lista_81:
                solo_82 += [g]
        print("Estas palabras solo están en la segunda lista: ",solo_82)
        
        #Todas las palabras
        todo = comunes + solo_81 + solo_82
        print("Todas las palabras: ",todo)