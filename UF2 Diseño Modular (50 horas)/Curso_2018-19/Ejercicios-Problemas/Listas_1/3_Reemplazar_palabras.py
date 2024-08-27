#Bloque de variables
counter = int(input("Cuántas palabras tiene esta lista: "))

#Buenas prácticas
if counter <= 0:
    print("Eso es imposible !!!")
else:
    #Lista de trabajo
    lista = []
    #Pedimos tantas palabras como solicite el usuario
    for a in range(counter):
        print ("Dime la palabra ",str(a+1), ": ",end="")
        nombre = input()
        lista += [nombre]
    print("La lista creada es: ",lista)
    
    #Igual que en el ejercicio anterior, declaramos dos nuevas variables: palabra que queremos reemplazar, palabra de reemplazo.
    substituir = str(input("Dime que palabra quieres substituir: "))
    buscar = str(input("Por la palabra: "))
    
    #Recorremos la lista y si hay coincidencias reemplazamos esa palabra por otra palabra.
    for b in range(len(lista)):
        if lista[b] == substituir:
            lista[b] = buscar
            
    print("La lista es ahora: ",lista)