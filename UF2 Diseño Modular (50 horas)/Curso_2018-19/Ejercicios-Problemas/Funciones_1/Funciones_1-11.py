def subrutina():
    def sub_subrutina():
        global a
        a = 5
        print(a)
        return

    global a
    a = 4
    sub_subrutina()
    print(a)
    return

a = 3
subrutina()
print(a)

#El programa escribe tres veces el número 5 (5, 5, 5)