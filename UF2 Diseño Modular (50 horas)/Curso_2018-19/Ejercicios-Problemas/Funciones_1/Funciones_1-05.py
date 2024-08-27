def subrutina():
    print(a)
    a = 11
    return

a = 10
subrutina()
print(a)

#Respuesta: el programa falla porque la variable local de a en subrutina se ha declarado después del print.