def a_sec(horas, minutos, segundos):
	horas = int((horas * 3600))
	minutos = int((minutos * 60))
	return(horas+minutos+segundos)

def de_seg(sec):
	horas = int(sec/3600)
	minutos = int((sec-(horas*3600))/60)
	segundos = sec-((horas*3600)+(minutos*60))
	print(str(horas)+"h "+str(minutos)+"m "+str(segundos)+"s")

horas = 0
minutos = 0
segundos = 0

for b in range(0,2,1):
	horas = horas+int(input("Introduce las horas: "));
	minutos = minutos+int(input("Introduce los minutos: "));
	segundos = segundos+int(input("Introduce los segundos: "));

total = a_sec(horas, minutos, segundos)
print(str(total)+"s")
de_seg(total)
