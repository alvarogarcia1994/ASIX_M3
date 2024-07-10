def subrutina():
    def sub_subrutina():
        a = 3
        print(a)
        a = 5
        return

    a = 3
    sub_subrutina()
    print(a)
    return

a = 4
sub_subrutina()
print(a)
