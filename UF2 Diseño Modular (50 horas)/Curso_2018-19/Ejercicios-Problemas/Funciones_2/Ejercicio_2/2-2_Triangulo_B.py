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
    anchura = int(input("Anchura del triángulo: "))
    #A diferencia del ejercicio anterior, en este hay que generar una sucesión de triángulos. para ello con un bucle for que parte desde la anchura hasta cero decrementando en 1, llamamos a las funciones que hemos creado previamente.
    for a in range(anchura, 0, -1):
        #Esta vez el parámetro que tiene que recibir la función es el de la variable auxiliar del bucle for.
        creciente(a)
        decreciente(a)
main()