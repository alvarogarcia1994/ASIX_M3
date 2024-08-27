#Bloque de variables
contar = int(input("Dime cuántas palabras hay en esta lista: "))

#Buenas prácticas
if contar <= 0:
    print("Imposible")
else:
    #Lista de trabajo
    lista = []
    for a in range(contar):
        print("Dime la palabra ",str(a+1),":",end=" ")
        palabra = input()
        lista.append(palabra)
    print("La lista es ahora: ", lista)
    
    #Recorremos a la inversa la misma lista
    for b in range(len(lista)-1,-1,-1):
        #Si algún elemento aparece 2 o más de 2 veces lo borramos.
        if lista[b] in lista[:b]:
            del(lista[b])
    print("La lista sin repeticiones es: ",lista)
            