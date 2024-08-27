def subrutina():
    def sub_subrutina():
        a += 3
        print(a)
        return

    a += 3
    sub_subrutina()
    print(a)
    return

a = 4
subrutina()
print(a)

#Respuesta el programa falla en la linea 7