def subrutina():
    nonlocal a
    print(a)
    a = 32
    return

a = 31
subrutina()
print(a)

#Respuesta: el programa falla por la variable a dentro de subrutina()