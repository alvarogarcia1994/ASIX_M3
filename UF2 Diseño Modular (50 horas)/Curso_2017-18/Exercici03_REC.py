#!/usr/bin/env python
# -*- coding: utf-8 -*-

#programa principal

#matriu de treball... 

matriu = [  [1000,876,44,65,17,2,32],
                  [343,67,55,76,15,344],
                  [567,57,66,87,14,454],
                  [457,34,99,98,13,565],
                  [23,789,88,43,12,676],
                  [678,26,77,32,11,787],   ];


#Variables
a = int;


# a partir d'aquí, el teu codi....
def impares(matriu):
	for a in range(0,7):
		print();
		for b in range(0,6):
			if (matriu>10 and matriu<200):
				print(matriu);
			else:
				print("Este es numero es menor que 10 o mayor que 200");		
				if (matriu==0):
					return
				else:
					if (matriu%2!=0):
						print(matriu);
						impares(matriu-1)
					else:
						impares(matriu-1)				
impares(matriu)

def main(argv): 

    impares(int(argv[1])) 
    pass
     
main(sys.argv) 
