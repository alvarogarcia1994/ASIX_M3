def subrutina_1():
    a = 20
    print(a)
    return

def subrutina_2():
    global a
    a = 30
    print(a)
    return

a = 10
subrutina_1()
print(a)
subrutina_2()
print(a)