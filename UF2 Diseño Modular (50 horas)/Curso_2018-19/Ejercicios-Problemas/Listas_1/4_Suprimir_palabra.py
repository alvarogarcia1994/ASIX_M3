#Bloque de variables
cantidad = int(input("Cuántas palabras hay en esta lista: "))

#Buenas prácticas
if cantidad <= 0:
    print("No es posible")
else:
    #Lista de trabajo
    lista = []
    for a in range(cantidad):
        print("Dime la palabra ",str(a+1)+":",end=" ")
        palabra = input()
        lista += [palabra]
    print("La lista creada es: ", lista)
    
    #Palabra que el usuario desea suprimir
    delete = str(input("Palabra a eliminar: "))
    
    #Recorremos la lista de forma inversa y en caso de que la palabra que queremos eliminar aparece, la eliminamos de la lista.
    for b in range(len(lista)-1,-1,-1):
        if lista[b] == delete:
            del(lista[b])
    
    print("La lista es ahora: ", lista)