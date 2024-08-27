#Tercera y última parte del ejercicio 5.
#Este ejercicio consta de una repetición del ejercicio de listas 1-7 en el que se trabaja eliminación de repeticiones
#En esta ocasión se trata de repetir el mismo ejercicio pero usando las funciones.
#En lugar de 2 listas como en el ejercicio 5-2, esta vez hay que crear N listas.

#Primera función (No recibe parámetros en la primera parte)
def crear_lista(contador):
    #Número de listas a crear por el usuario
    numero = int(input(f"Cuántas palabras tiene la lista {contador + 1}: "))

    #Buenas prácticas
    if (numero <= 0):
        print("Se creará una lista vacía")
    else:
        #Lista de trabajo
        lista = []
        for x in range(numero):
            palabra = str(input(f"Dime la palabra {x + 1} : "))
            if (palabra not in lista):
                lista.append(palabra)
            else:
                palabra = str(input(f"{palabra} ya está en la lista, dime la palabra {x + 1}: "))
    return lista

#Función que se encargará de procesar el borrado de los elementos de la primera lista que se repitan en la segunda.
def borrado(lista, lista_borrado):
    for palabra in lista_borrado:
        while palabra in lista:
            lista.remove(palabra)
    return lista

#A modo de buenas prácticas creamos una tercera función con N listas
def cuantas_listas():
    numero = int(input("Cuántas listas quieres: "))
    if numero <= 0:
        print("Imposible")
        return 0
    else:
        return numero

#Programa principal
def main():
    #Variables principales
    vuelta = cuantas_listas()
    listas = []

    #Generando las listas
    for x in range(vuelta):
        listas.append(crear_lista(x))
    
    print("Las listas generadas son: ")
    #Después de generar la listas
    for x in range(vuelta):
        print(f"{listas[x]}")

    #Listas sin repeticiones
    print("Las listas sin repeticiones son: ")
    for x in range(vuelta):
        for y in range(x+1, vuelta):
            listas[x] = borrado(listas[x], listas[y])
        print(f"{listas[x]}")

main()