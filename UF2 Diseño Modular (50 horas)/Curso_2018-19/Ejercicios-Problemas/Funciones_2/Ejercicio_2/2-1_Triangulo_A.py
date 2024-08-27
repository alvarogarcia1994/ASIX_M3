#Para este ejercicio necesitamos dos funciones, la primera para hacer el lado creciente del triángulo y la segunda para el decreciente.
#Ambas funciones solo reciben un parámetro

#Función lado creciente
def creciente(anchura):
    for a in range(1, anchura+1):
        for b in range(a):
            print("*", end=" ")
        print()

#Función decreciente
def decreciente(anchura):
    for a in range(1, anchura):
        for b in range(anchura - a):
            print("*", end=" ")
        print()

#Programa principal
def main():
    #Bloque de variables
    anchura = int(input("Anchura del triángulo: "))
    #Llamando a las funciones
    creciente(anchura)
    decreciente(anchura)
main()