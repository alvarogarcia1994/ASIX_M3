Contactes = []

def entrar_tel_pers(Contactes):
     num = int(input("Numero: "))
     pers = str(input("Persona: "))
     print("Ok. Dades entrades")
     Contactes.append((num,pers))

def cercar_tel_pers(Contactes):
    pers = str(input("Persona: "))
    num = int
    for contacte in Contactes:
        if contacte[1] == pers:
            print("Aquest contacte té aquest número: ", contacte[0])
        else:
            print("ERROR!")
    return pers
    Contactes = []

def cercar_pers_tel(Contactes):
    num = int(input("Numero: "))
    pers = str
    for contacte in Contactes:
        if contacte[0] == num:
            print("Aquest contacte té aquest número: ", contacte[1])
        else:
            print("ERROR!")
    return num
    Contactes = []

def esborrar(Contactes, pos):
    Contactes.pop(pos)
            
def menu():
    print("1: Entrar número de telèfon i nom de persona")
    print("2: Cercar número de telèfon de persona")
    print("3: Cercar nom de persona per telèfon")
    print("4: Esborrar número")
    
menu()
op = int(input("Què vols fer ? "))

while op!= 5:
    if (op == 1):
        entrar_tel_pers(Contactes)
        
    elif (op == 2):
        cercar_tel_pers(Contactes)
    
    elif (op == 3):
        cercar_pers_tel(Contactes)
    
    elif (op == 4):
        pos = int(input("Posicio a esborrar: "))
        print("Ok. Numero esborrat")
        esborrar(Contactes, pos)
        
    op = int(input("Què vols fer ? "))