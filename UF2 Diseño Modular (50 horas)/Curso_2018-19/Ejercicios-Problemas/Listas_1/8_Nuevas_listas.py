#Variable inicial
uno = int(input("Dime cuántos elementos hay en esta lista: "))

#Validacion de la variable necesaria, para poder añadir esos valores a la lista
if uno <= 0:
    print("Eso es imposible")
else:
    primera = []
    #Si la validación es correcta introduciremos valores y recorremos la lista
    for a in range(uno):
        print("Dime la palabra ",str(a+1),":",end=" ")
        palabra = input()
        primera += [palabra]
    
    #Nuevamente volvemos a recorrer la lista, pero al revés.
    for b in range(len(primera)-1,-1,-1):
        if primera[b] in primera[:b]:
            #Si algun elemento se repite será eliminado
            del(primera[b])
    print("La primera lista sin repeticiones es: ",primera)
    
    #Necesitamos una segunda variable para validar la segunda lista
    dos = int(input("Dime cuántos elementos hay en esta lista: "))
    
    if dos <= 0:
        print("Eso es imposible")
    else:
        segunda = []
        #Incio segunda lista
        for c in range(dos):
            print("Dime la palabra ",str(c+1),":",end=" ")
            word = input()
            segunda += [word]
        
        #Repito el mismo proceso que hice con la primera lista
        for d in range(len(segunda)-1,-1,-1):
            if segunda[d] in segunda[:d]:
                del(segunda[d])
        print("La segunda lista sin repeticiones es: ",segunda)
        
        #Es esta tercera lista se añadirán las palabras que hayan salido en ambas listas
        comunes = []
        for e in primera:
            if e in segunda:
                comunes += [e]
        print("Aparece en todas las listas: ", comunes)
        
        #En la cuarta lista solo queremos las palabras de la primera
        solo_primera = []
        for f in primera:
            if f not in segunda:
                solo_primera += [f]
        print("Estas palabras solo están en la primera lista: ",solo_primera)
        
        #En la quinta, solo nos interesan las palabras que hayan salido en la segunda
        solo_segunda = []
        for g in segunda:
            if g not in primera:
                solo_segunda += [g]
        print("Estas palabras solo están en la segunda lista: ",solo_segunda)
        
        #Todas las palabras
        todo = comunes + solo_primera + solo_segunda
        print("Todas las palabras: ",todo)