def de_seg(sec):
	horas = int(sec/3600)
	minutos = int((sec-(horas*3600))/60)
	segundos = sec-((horas*3600)+(minutos*60))
	print(str(horas)+"h "+str(minutos)+"m "+str(segundos)+"s")

sec = int(input("Introduce el número de segundos: "))

de_seg(sec)
