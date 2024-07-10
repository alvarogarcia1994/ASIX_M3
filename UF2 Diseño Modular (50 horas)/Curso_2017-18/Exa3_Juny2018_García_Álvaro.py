import os

#programa principal
#matriu de treball...
matriuExa3 = [ [1000,876,44,65,17,232],
[343,67,55,76,15,344],
[567,57,66,87,14,454],
[457,34,99,98,13,565],
[23,789,88,43,12,676],
[678,26,77,32,11,787], ];

# a partir d'aquí, el teu codi....
#Primera función. Detectar números impares.
def deteccio_senar(matriuExa3):
    #Recorremos filas y columnas
    for j in range(0,6):
        for k in range(0,6):
            #Una vez recorrida toda la matriz, con un if indicamos que si hay algún número impar que lo imprima.
            if matriuExa3[j][k] % 2 != 0:
                print("Son senars: ", matriuExa3[j][k])

#Segunda función. Obtener los números del 11 al 199.
def detecta_rang(matriuExa3):
    #Recorremos al array.
    for a in range(0,6):
        for b in range(0,6):
            #Si el número está entre 11 y 199 hay que mostrarlo.
            if (matriuExa3[a][b] > 10) and (matriuExa3[a][b] < 200):
                print("Dins d'aquest rang: ", matriuExa3[a][b])

#Llamamos a las funciones.
deteccio_senar(matriuExa3)
detecta_rang(matriuExa3)