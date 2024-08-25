def retorna_llista_divisors(num):
    llista_div = []
    for i in range(1, num+1):
            if num % i == 0:
               
                llista_div.append(i)
   
    return llista_div
       
       
def retorna_es_primer(num):
    if len(retorna_llista_divisors(num)) == 2:
        return True
    else:
        return False
   
def retorna_es_perfecte(num):
    llista_divisors = retorna_llista_divisors(num)
    suma = 0
    for i in llista_divisors:
           
        suma += i
    suma =suma-num
    if suma == num:
        return True
    else:
        return False


       
   
       
for i in range(1,101):
    if retorna_es_primer(i)==True:
        print(i,"És primer? Sí ",end="")
    else:
        print(i,"És primer? No ",end="")
    if retorna_es_perfecte(i)==True:
        print("És perfecte? Sí ")
    else:
        print("És perfecte? No ")