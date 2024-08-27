#Bloque de variables
numero = int(input("Dime un número: "))
#Contador de divisores
cont = 0

#Best practices
if numero < 1:
    print("Eso no tiene sentido")
else:
    #Declaramos la lista de divisores
    divisores = []
    #Recorremos desde 1 hasta el número introducido por el usuario
    for a in range(1,numero+1):
        #Validamos cada iteración si es divisible el numero entre el valor de a (auxiliar del bucle for)
        if numero % a == 0:
            #Si el residuo de la división es cero incrementa el contador de divisores en 1 y lo guardamos en la lista.
            cont += 1
            divisores += [a]
    #Resultado final
    print(f"Este número tiene {cont} divisores: {divisores}")