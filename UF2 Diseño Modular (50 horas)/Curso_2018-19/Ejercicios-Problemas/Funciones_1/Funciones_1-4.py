def subrutina():
    nonlocal a
    print(a)
    a = 32
    return

a = 31
subrutina()
print(a)

