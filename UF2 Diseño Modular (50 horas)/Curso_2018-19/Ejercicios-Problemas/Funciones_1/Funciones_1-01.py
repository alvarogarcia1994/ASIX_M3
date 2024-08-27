def subrutina():
    global a
    print(a)
    a += 10
    return

a = 33
subrutina()
print(a)

#Respuesta: el programa pinta los valores 33 y 43