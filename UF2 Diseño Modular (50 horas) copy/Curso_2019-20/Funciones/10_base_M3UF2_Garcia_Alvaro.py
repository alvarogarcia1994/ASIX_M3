def retorna_canvi_base(num,base):
    l=[]
    while num!=0:
        quocient = num//base
        residu = num%base
        if residu == 10:
            residu = 'A'
        if residu == 11:
            residu = 'B'
        if residu == 12:
            residu = 'C'
        if residu == 13:
            residu = 'D'
        if residu == 14:
            residu = 'E'
        if residu == 15:
            residu = 'F'       
        l.append(residu)
        num=quocient
    l.reverse()
    return(l)
        

num=100
base=2
print(retorna_canvi_base(num,base))


num=65535
base=16
print(retorna_canvi_base(num,base))

num=777
base=8
print(retorna_canvi_base(num,base))
