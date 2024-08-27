#Bloque de variables
contar = int(input("Cuántas palabras tiene esta lista: "))

#Buenas prácticas
if contar <= 0:
    print("Eso es imposible")
else:
    #Lista de trabajo
    lista = []
    for a in range(contar):
        print("Dime la palabra ",str(a+1),":",end=" ")
        palabra = input()
        lista.append(palabra)
    print("La lista creada es: ",lista)
    
    #Lista inversa
    inversa = []
    #Recorremos la primera lista hacia atrás
    for b in lista:
        #En orden inverso vamos agregando los valores de la primera lista a la segunda lista.
        inversa = [b] + inversa
    print("La lista inversa es: ", inversa)