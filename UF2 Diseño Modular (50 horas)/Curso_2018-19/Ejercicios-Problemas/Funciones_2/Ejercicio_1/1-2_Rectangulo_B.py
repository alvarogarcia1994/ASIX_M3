#Función del ejercicio anterior pero utilizando tres parámetros en lugar de dos parámetros.
def rectangulo(anchura, altura, letra):
    for a in range(anchura):
        for b in range(altura):
            print(letra, end=" ")
        print()

#Programa principal
def main():
    #Variables necesarias
    anchura = int(input("Dime la anchura: "))
    altura = int(input("Dime la altura: "))
    letra = str(input("Introduce una letra: "))
    #Llamamos a la función.
    rectangulo(altura, anchura, letra)
main()