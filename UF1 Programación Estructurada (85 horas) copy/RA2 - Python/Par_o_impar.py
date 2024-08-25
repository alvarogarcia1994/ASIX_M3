#Introducir un numero por teclado y decir si es par o impar


#variables
num = input("Introduce un número: ")
num = int(num)

if num%2 == 0:
    print ("Este numero es par")
else:
    print ("Este numero es impar")
