def cuenta_A(texto):
    cont = 0
    for a in range(0, len(texto)):
        if (texto[a] == "a" or texto[a] == "A"):
            cont += 1
    return cont

texto = str(input("Introduce un texto: "))
print(cuenta_A(texto))
