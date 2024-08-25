#!/usr/bin/env python
# -*- coding: utf-8 -*-

llista = []

def calcula_nota(llista):	
	iteracions=len(llista)
	nota = 0
	for i in llista:
		nota+=i
	mitjana = nota / iteracions
	if nota < 0 and nota > 10:
	    print("Aquesta nota no és vàlida, nomès s'accepten qualificacions del 0 al 10.")
	else:
	    if mitjana <=10 and mitjana >= 9:
                qualif = ("Excel·lent")
	    elif mitjana <= 8.99 and mitjana >= 7:
                qualif = ("Notable")
	    elif mitjana <= 6.99 and mitjana >= 6:
                qualif = ("Bé")
	    elif mitjana <= 5.99 and mitjana >= 5:
                qualif = ("Suficient")
	    else:
                qualif = ("Insuficient")
	return mitjana,qualif


print("Quantes notes té l'alumne: ", end="")
iteracions = int(input())

for x in range(iteracions):
	print("Nota", str(x + 1) + ": ", end="")
	nota = float(input())
	llista += [nota]
'''
llista = calcula_nota(llista)
mitjana = llista / iteracions
'''
mitjana,qualif=calcula_nota(llista)
print ("La mitjana és: ", mitjana, "La nota és: ", qualif)
