#Primera parte del ejercicio 5.
#Este ejercicio consta de una repetición del ejercicio de listas 1-5 en el que se trabaja la supresión de múltiples elementos.
#En este ocasión se trata de repetir el mismo ejercicio pero usando las funciones

#Primera función (No recibe parámetros en la primera parte)
def crear_lista():
    #Número de listas a crear por el usuario
    numero = int(input("Cuántas palabras tiene esta lista: "))

    #Buenas prácticas
    if (numero <= 0):
        print("Se creará una lista vacía")
    else:
        #Lista de trabajo
        lista = []
        for x in range(numero):
            palabra = str(input(f"Dime la palabra {x + 1} : "))
            lista.append(palabra)
    return lista

def borrado(lista, lista_borrado):
    for palabra in lista_borrado:
        while palabra in lista:
            lista.remove(palabra)
    return lista
            

def main():
    lista_palabras = crear_lista()
    
    # Crear la lista de palabras a borrar
    numero_borrar = int(input("¿Cuántas palabras deseas borrar? "))
    lista_borrar = []
    for x in range(numero_borrar):
        palabra = str(input(f"Dime la palabra a borrar {x + 1}: "))
        lista_borrar.append(palabra)
    
    # Borrar las palabras de la lista original
    lista_actualizada = borrado(lista_palabras, lista_borrar)
    
    # Mostrar la lista actualizada
    print("Lista actualizada:", lista_actualizada)
main()