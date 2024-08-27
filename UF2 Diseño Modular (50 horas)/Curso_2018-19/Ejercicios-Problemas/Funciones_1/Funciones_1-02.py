def subrutina():
    global a
    print(a)
    a = 21
    return

subrutina()
a = 20
print(a)

#Respuesta: el programa falla en la linea 3 porque la función pretende imprimir el valor de a justo antes de asignarle un valor.