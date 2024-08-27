#Bloque de variables
numero = int(input("Dime cuántas palabras tiene esta lista: "))

#Buenas prácticas
if numero < 1:
    print("Eso es imposible")
else:
    #Lista de trabajo
    lista = []
    #Iteramos con un for
    for a in range(numero):
        palabra = str(input(f"Dime la palabra {a + 1}: "))
        lista += [palabra]
    print("La lista generada es: ", lista)
    
    #Nuevamente, recorremos la lista para ordenarla
    for b in range(len(lista)):    
        lista.sort()
    
    #Resultado
    print(f"La lista ordenada es: {lista}")        