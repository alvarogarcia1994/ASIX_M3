# tres_tiempos.py
def print_asegundos (horas, minutos, segundos):
    """ Transforma en segundos una medida de tiempo expresada en
        horas, minutos y segundos """
    segsal = 3600 * horas + 60 * minutos + segundos;
    return segsal;
 
def main():
    """ Lee tres tiempos expresados en hs, min y seg, y usa
        print_asegundos para mostrar en pantalla la conversión a
        segundos """
    tarifa = float;
    ntrucades = int;
    totalsegons = int;
    totalsegons=0;
    a = int;
    
    print("introdueix la tarifa");
    tarifa = float(input());
    print("Quantes trucades has fet?");
    ntrucades = int(input());
    
    for x in range(ntrucades):
        hs = int(input("Cuantas horas?: "))
        minutos = int(input("Cuantos minutos?: "))
        seg = int(input("Cuantos segundos?: "))
        a = print_asegundos(hs,minutos,seg);
        totalsegons = totalsegons + a;
    
    return totalsegons * tarifa;
        
    
		
print (main())
