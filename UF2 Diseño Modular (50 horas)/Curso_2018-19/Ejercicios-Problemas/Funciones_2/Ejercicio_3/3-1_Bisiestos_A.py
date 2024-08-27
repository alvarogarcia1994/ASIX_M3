#Función para determinar si un año es bisiesto
def es_bisiesto(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

#Programa principal
def main():
    #Pedimos año
    year = int(input("Dime un año: "))
    #Validamos si ese año es o no bisiesto.
    if es_bisiesto(year):
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")
main()