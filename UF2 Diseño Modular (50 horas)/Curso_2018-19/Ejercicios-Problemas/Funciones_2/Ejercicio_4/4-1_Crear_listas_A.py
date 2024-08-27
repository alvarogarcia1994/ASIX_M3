#Primera parte del ejercicio 4.
#Este ejercicio consta de una repetición del ejercicio de listas 1-1 en la que había que crear listas.
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

def main():
    print(f"La lista creada es: ", crear_lista())
main()
