def calc_asegundos (horas, minutos, segundos):
	
	
	#Transformación
	segsal = 3600 * horas + 60 * minutos + segundos;
	return segsal;

a = int;	
a=calc_asegundos (0, 56, 2);
print("",a);
