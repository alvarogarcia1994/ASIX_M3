#Segunda parte del ejercicio 5.
#Este ejercicio consta de una repetición del ejercicio de listas 1-7 en el que se trabaja eliminación de repeticiones
#En esta ocasión se trata de repetir el mismo ejercicio pero usando las funciones

#Primera función (No recibe parámetros en la primera parte)
def crear_lista(contador):
    #Número de listas a crear por el usuario
    numero = int(input(f"Cuántas palabras tiene la lista {contador}: "))

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
    #Recorremos lista de borrado, si encontramos palabra en la lista la eliminamos
    for palabra in lista_borrado:
        while palabra in lista:
            lista.remove(palabra)
    #Retornamos la lista
    return lista
            
#Programa principal
def main():
    #Creamos las dos listas
    lista_1 = crear_lista(1)
    lista_2 = crear_lista(2)

    #Antes de procesar el borrado
    print("Las listas generadas son: ")
    print(lista_1)
    print(lista_2)

    #Después de procesar el borrado de las palabras que se repiten.
    print("Las listas sin repeticiones son: ")
    lista_1 = borrado(lista_1, lista_2)
    print(lista_1)
    print(lista_2)

main()