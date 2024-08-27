#Bloque de variables
numero = int(input("Cuántas palabras tiene esta lista: "))

#Best practices
if numero <= 0:
    print("Imposible!")
else:
    #Declaramos la lista
    lista = []
    #Pedimos tantas palabras como el usuario solicite
    for x in range(numero):
        print("Dime la palabra ",str(x+1),": ",end="")
        palabra = input()
        lista.append(palabra)
    print("La lista creada es: ", lista)
    
    #Una vez generada la lista, necesitaremos dos variables más: una para filtrar por palabra y la segunda para contar cuántas veces sale en la lista.
    buscador = str(input("Dime la palabra que quieres que busque: "))
    contador = 0
    
    #Recorremos la lista
    for y in lista:
        #En caso de coincidencia el contador incrementa en 1.
        if y == buscador:
            contador += 1
    #Mensajes en función de cuántas veces aparezca la palabra solicitada.
    if contador == 0:
        print("Esta palabra no está en esta lista")
    elif contador == 1:
        print("Esta palabra aparece una vez en esta lista")
    elif contador >= 2:
        print("Esta palabra aparece ",contador," veces en esta lista") 