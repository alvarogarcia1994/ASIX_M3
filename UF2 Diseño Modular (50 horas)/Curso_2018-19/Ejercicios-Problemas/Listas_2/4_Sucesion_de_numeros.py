#Cálculo de términos de una sucesión U*(n+1)=a*U(n)+b.

#Bloque de variables
a = int(input("Dime el valor de a: "))
b = int(input("Dime el valor de b: "))
U0 = int(input("Dime el valor de U(0): "))
cantidad = int(input("Cuántos términos quieres: "))

#Una vez introducidos los datos, prodecemos a las buenas prácticas
if (cantidad <= 0):
    print("Debes introducir un número igual o superior a 1")
else:
    #Lista de trabajo
    sucesion = [U0]
    #En base a la cantidad de terminos introducida por el usuario hacemos un recorrido de la lista y durante ese recorrido realizamos los cálculos pertinentes
    for x in range(cantidad-1):
        resultado = a * sucesion[x] + b
        sucesion.append(resultado)
    
    #Respuesta
    print(f"Los términos de la sucesión númerica son: {sucesion}")