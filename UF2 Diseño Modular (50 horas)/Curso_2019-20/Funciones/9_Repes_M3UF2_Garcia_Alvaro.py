#from random import randint, uniform, random
import random

def escriu_repes(*args):
    l=[0,0,0,0,0,0,0,0,0,0,0]
    for num in args:
        l[num]=l[num]+1
        
    print(l)
    print("Es repeteixen els nombres: ")    
    for num in range(1,11):
        if l[num] > 1:
            print(num," ",end="")
    print()

a1=random.randint(1,10)
a2=random.randint(1,10)
a3=random.randint(1,10)
a4=random.randint(1,10)
a5=random.randint(1,10)
a6=random.randint(1,10)
a7=random.randint(1,10)
a8=random.randint(1,10)
a9=random.randint(1,10)
a10=random.randint(1,10)

escriu_repes(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)

print("He generat els valors: ", a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)go