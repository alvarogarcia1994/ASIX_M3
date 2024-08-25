# tres_tiempos.py
def print_asegundos (horas, minutos, segundos):
    """ Transforma en segundos una medida de tiempo expresada en
        horas, minutos y segundos """
    segsal = 3600 * horas + 60 * minutos + segundos
    print ("Son",segsal, "segundos")
 
def main():
    """ Lee tres tiempos expresados en hs, min y seg, y usa
        print_asegundos para mostrar en pantalla la conversión a
        segundos """
    segsal=1
    for x in range(1):
        hs = int(input("Cuantas horas?: "))
        minutos = int(input("Cuantos minutos?: "))
        seg = int(input("Cuantos segundos?: "))
        print_asegundos(hs, minutos, seg)
		
main()
