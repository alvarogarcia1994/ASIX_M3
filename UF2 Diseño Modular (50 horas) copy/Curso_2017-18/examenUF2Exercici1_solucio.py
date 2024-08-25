#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#funcions importades

def llegirEnterInterval(num1, num2):
    '''
    La funció llegirEnterInterval() llegeix l'entrada del teclat de l'usuari i si
    el nombre introduit té un format correcte de nombre enter i es troba en l’intèrval
    demanat pels paràmetres introduïts, el retorna.
    * paràmetres d'entrada: num1 (enter), num2 (enter)
    * paràmetres de sortida: numReturn (enter)
    '''
     #declarem variables
    numRetorn = int;
    error = int;
    aux = int;
    
    #inicialitzem variables
    error= 1;
    
    if (num1 > num2):
        aux = num1;
        num1 = num2;
        num2 = aux;
        
    while(error):  #mentre la captura de  l'enter no sigui exitosa, continuem...
        try:  #provem de reclamar el nombre enter
            print("Introdueix un enter entre ", num1, " i ", num2, "\n");
            numRetorn = int(input());
            if (numRetorn >= num1 and numRetorn <= num2):
                error = 0;   #només canviem l'estat de la variable en cas de captura correcta.
            else:
                print("El nombre no està dins l'intèrval");
        except:  #en cas d'error...
            print("S'ha produit un error en la introducció. Torna a provar...");
    
    return numRetorn;  


#funcions del programa

def imprimeixMatriu(matriu):
	for x in range (len(matriu)):
		print (matriu[x]," ",end="");

def intercanvia(matriu, a, b):
	aux = str;
	aux = matriu[a];
	matriu[a] = matriu[b];
	matriu[b] = aux;


def comprovaMatriu(matriu, text):
	resultat = "";
	for x in range (len(matriu)):
		resultat = resultat + matriu[x];
	if (resultat == text):
		return 1;
	else: 
		return 0;

#programa principal
	
#matriu de treball... 
matriu = ["N","X","A","M","E","E"];


bucle=1;
while(bucle):
	imprimeixMatriu(matriu); 
	print(); 
	a = llegirEnterInterval(0,5);
	b = llegirEnterInterval(0,5);
	intercanvia(matriu, a, b); 
	if comprovaMatriu(matriu):
		print("FELICITATS!!!, Ho has aconseguit!!!");
		bucle = 0;   
