#Función que a partir de dos parámetros altura y anchura dibujará un rectángulo
def rectangulo(anchura, altura):
    #Mediante dos bucles for anidados haremos el recorrido de altura y de anchura
    for a in range(anchura):
        for b in range(altura):
            print("o", end=" ")
        #Salto de linea
        print()

#Programa principal   
def main():
    #Bloque de variables
    anchura = int(input("Dime la anchura: "))
    altura = int(input("Dime la altura: "))
    #Llamada a la función
    rectangulo(altura, anchura)
main()