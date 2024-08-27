#Cálculo de la conjetura de collatz U*(n+1)=3*U(n)+1 si n es impar y U*(n)=U*(n)/2 si n es par.

#Bloque de variables
U0 = int(input("Dime el valor de U(0): "))
cantidad = int(input("Cuántos términos quieres: "))

#Una vez introducidos los datos, prodecemos a las buenas prácticas
if (cantidad <= 0):
    print("Debes introducir un número igual o superior a 1")
else:
    #Lista de trabajo
    collatz = [U0]
    #En base a la cantidad de terminos introducida por el usuario hacemos un recorrido de la lista y durante ese recorrido realizamos los cálculos pertinentes
    for x in range(cantidad-1):
        #Si el valor de n es impar aplicamos el calculo de multiplicar por 3 al valor de collatz[x] y le sumamos 1 (ejemplo: si U0=7 7*3+1 = 21 + 1 = 22 en la posicion collatz[1])
        if (collatz[x] % 2 == 1):
            resultado = int (3 * collatz[x]) + 1
            #Guardamos el resultado
            collatz.append(resultado)
        #Si por el contrario el numero es par diviremos por 2 (ejemplo: si U0=6 6/2 = 3 en la posicion collatz[1])
        else:
            resultado = int (collatz[x] / 2)
            collatz.append(resultado)
        
    #Respuesta
    print(f"Los términos de la sucesión númerica son: {collatz}")