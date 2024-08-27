#Tercera y última parte del ejercicio 4
#Reutilizando las funciones del ejercicio 4-2 vamos a hacer que el programa muestre las listas creadas con sus valores al final del programa en lugar de al final de introducir la última palabra de cada lista.
#Primera función (Recibe por parámetro el número de la lista)
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
            lista.append(palabra)
    return lista

#Segunda función la cual utilizaremos para validar cuántas listas queremos crear
def cuantas_listas():
    numero = int(input("Cuántas listas quieres: "))
    if numero <= 0:
        print("Imposible")
    else:
        return numero

#Programa principal
def main():
    vuelta = cuantas_listas()
    listas = []

    for x in range(vuelta):
        listas += [crear_lista(x)]

    for y in range(vuelta):
        print(f"La lista {y + 1} es: {listas[y]}")
main()