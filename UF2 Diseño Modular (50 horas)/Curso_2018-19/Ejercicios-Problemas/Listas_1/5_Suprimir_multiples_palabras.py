#Bloque de variables
contar = int(input("Cuántas palabras hay en esta lista: "))

#Buenas prácticaas
if contar <= 0:
    print("Eso es imposible")
else:
    #Lista de trabajo
    lista = []
    for a in range(contar):
        print("Dime la palabra ",str(a+1),":",end=" ")
        palabra = input()
        lista += [palabra]
    print("La lista creada es: ",lista)
    
    #Cantidad de palabras que el usuario desea suprimir
    palabras_suprimir = int(input("Cuántas palabras hay en esta lista: "))
    
    #Buenas prácticas
    if palabras_suprimir <= 0:
        print("Eso es imposible")
    else:
        #Lista de palabras a eliminar
        lista_del = []
        #La misma praxis que cuando agregamos las palabras en la otra lista
        for b in range(palabras_suprimir):
            print("Palabra a eliminar ",str(b+1),":",end=" ")
            suprimir = input()
            lista_del.append(suprimir)
        print("Las palabras a eliminar son: ",lista_del)
        
        #Recorremos la lista de palabras a eliminar
        for c in lista_del:
            #Paralelamente recorremos la lista principal de forma inversa, si alguna de las palabras de la segunda lista coinciden con las de la primera, las borramos de la primera lista.
            for d in range(len(lista)-1,-1,-1):
                if lista[d] == c:
                    del(lista[d])
        print("La lista ahora es: ", lista)     