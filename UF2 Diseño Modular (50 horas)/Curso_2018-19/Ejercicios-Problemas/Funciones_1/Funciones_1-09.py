def subrutina():
    def sub_subrutina():
        a = 3
        print(a)
        a = 5
        return

    a = 3
    sub_subrutina()
    print(a)
    return

a = 4
sub_subrutina()
print(a)

#Respuesta: el programa falla porque no reconoce a la función sub_subrutina dentro del main. 
# El programa falla dado que esa función está declarada dentro de otra función subrutina()