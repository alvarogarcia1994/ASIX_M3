def retorna_factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

n = 10
print("El factorial de", n, "és: ", retorna_factorial(n))
print()

n = 20
print("El factorial de", n, "és: ", retorna_factorial(n))
print()

n = 400
print("El factorial de", n, "és: ", retorna_factorial(n))
print()

n = 2000
print("El factorial de", n, "és: ", retorna_factorial(n))