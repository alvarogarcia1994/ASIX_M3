#!/usr/bin/env python
# -*- coding: utf-8 -*-

contar = int(input("Cuántas palabras hay en esta lista: "))

if contar <= 0:
    print("Eso es imposible")
else:
    lista_5 = []
    for a in range(contar):
        print("Dime la palabra ",str(a+1),":",end=" ")
        palabra = input()
        lista_5 += [palabra]
    print("La lista creada es: ",lista_5)
    
    delete = int(input("Cuántas palabras hay en esta lista: "))
    
    if delete <= 0:
        print("Eso es imposible")
    else:
        lista_del = []
        for b in range(delete):
            print("Palabra a eliminar ",str(b+1),":",end=" ")
            suprimir = input()
            lista_del.append(suprimir)
        print("Las palabras a eliminar son: ",lista_del)
        
        for c in lista_del:
            for d in range(len(lista_5)-1,-1,-1):
                if lista_5[d] == c:
                    del(lista_5[d])
        print("La lista ahora es: ", lista_5)
                
                    
                    
                    
                    
            