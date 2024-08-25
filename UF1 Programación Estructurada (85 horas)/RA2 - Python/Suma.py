#Suma

#Variables
num1 = int 
num2 = int

contadorNum = int(0)
contadorPares = int(0)
sumatorio = int(0)

print("dime un numero")
num1 = int(input())
print("dime otro numero")
num2 = int(input())

for i in range(num1, num2+1):
	print (i)
	contadorNum = contadorNum +1
	if i%2 == 0:
		contadorPares = contadorPares + 1
		sumatorio = sumatorio + i
	
print("Hay...", contadorNum, " Numeros")
print("Hay...", contadorPares, " Pares") 
print("La suma de los numeros pares es...", sumatorio) 
