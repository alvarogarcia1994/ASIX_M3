#Segunda parte del ejercicio 4
#Con dos funciones, la primera para crear la lista (la cuál recibe un parámetro y la segunda función la utilizamos para validar la cantidad de listas) 
#Primera función (Esta vez recibe por parámetro el número de la lista)
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
        return 0
    else:
        return numero

#Programa principal
def main():
    vuelta = cuantas_listas()
    for x in range(vuelta):
        print(f"La lista {x + 1} es: ", crear_lista(x))
main()
