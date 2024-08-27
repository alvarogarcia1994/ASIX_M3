#Bloque de variables
cont = int(input("Dime cuántas palabras hay en esta lista: "))

#Buenas prácticas
if cont <= 0:
    print("Imposible!")
else:
    #Declaramos la lista
    lista = []
    #Pediremos al usuario tantas palabras como especifique el usuario
    for x in range(cont):
        print("Dime la palabra ", str(x+1) + ": ", end="")
        palabra = input()
        #Guardamos la palabra
        lista += [palabra]
    print("La lista creada es:", lista)