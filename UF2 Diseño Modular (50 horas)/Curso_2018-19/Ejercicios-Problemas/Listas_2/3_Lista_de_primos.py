#Bloque de variables
numero = int(input("Dime un número: "))

#Best practices
if numero < 1:
    print("Eso no tiene sentido")
else:
   #Declaramos lista de primos.
   lista_primos = []
   #Usamos un bucle for anidado, el primero recorre desde a hasta el número +1 introducido por el usuario
   for a in range(numero+1):
       #Contador de divisores en cero
       contador = 0
       #Segundo bucle for, desde 1 hasta el valor auxiliar del primer for (a+1)
       for b in range(1, a+1):
           #Validamos que el número actual sea divisible por b, en caso afirmativo incrementamos en 1 el contador de divisores.
           if a % b == 0:
               contador += 1
        #Al terminar el segundo bucle for, si cada valor del primer bucle (a) tiene 2 divisores(el 1 y el numero actual entre si mismo). Añadimos ese valor a la lista de números primos.
       if contador == 2:
           lista_primos +=[a]

print(f"Primos hasta {numero}: {lista_primos}")