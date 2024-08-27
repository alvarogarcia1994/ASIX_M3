#Reutilizamos la función del ejercicio anterior
def es_bisiesto(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

#Programa principal
def main():
    #Necesitaremos un año de inicio y otro de finalización
    year = int(input("Dime un año: "))
    end = int(input(f"Dime un año posterior a {year}: "))
    #Validamos que el año de inicio sea inferior al de finalización.
    if year > end:
        print(f"{end} no es superior a {year}")
    else:
        #Contador de años bisiestos
        leap_counter = 0
        #Recorremos entre el año de incio y el de finalización más 1.
        for a in range(year, end + 1):
            #Validamos año recibiendo como parámetro la variable auxiliar del for.
            if es_bisiesto(a):
                #Si es bisiesto en contador incrementará en 1.
                leap_counter +=1
        print(f"Entre {year} y {end} hay {end - year + 1} años, {leap_counter} de ellos son bisiestos")
main()