import os

Exa2 = ["23", "34", "6", "779", "123", "7", "6"]

#Función encargada de convertir a entero el array unidimensional.
def stringAEnter(Exa2):
    for x in range(len(Exa2)):
        #Conversión a entero
        Exa2[x] = int(Exa2[x])

#Llamada a la función de conversión
stringAEnter(Exa2)


#Función que se encargará de adivinar los números pares para obtener la suma de ellos posteriormente.
def esbrinaParell(Exa2):
    #Inicializamos variable local suma con valor de 0
    suma = 0
    #Recorremos el array convertido
    for j in range(0,7):
        #Si hay algún numero par dentro de ese array unidimensional...
        if Exa2[j] % 2 == 0:
            #Se realizará la suma de sus valores pares.
            suma = suma + Exa2[j]
    #Solo nos interesa el resultado.        
    return suma

#Llamando a la segunda función
print(esbrinaParell(Exa2))