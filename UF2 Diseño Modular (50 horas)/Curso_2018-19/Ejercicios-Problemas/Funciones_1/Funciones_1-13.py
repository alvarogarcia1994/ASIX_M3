def subrutina():
    def sub_subrutina():
        global a
        a = 5
        print(a)
        return

    a = 4
    sub_subrutina()
    print(a)
    return

a = 3
subrutina()
print(a)

#El programa escribe los valores númericos 5 4 5