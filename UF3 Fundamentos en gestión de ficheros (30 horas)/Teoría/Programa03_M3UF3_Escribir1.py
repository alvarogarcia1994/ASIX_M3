#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def llegirText(text="Introdueix un text \n"):
    '''
    La funció llegirText() llegeix l'entrada del teclat de l'usuari i si
    té un format correcte de text, el retorna.
    * paràmetres d'entrada: text (str): és el text amb que es demana a l'usuari
							la introducció del valor. Té un valor per 
							defecte si l'usuari no ho especifica
    * paràmetres de sortida: textRetorn (str)
    '''
     #declarem variables
    numRetorn = str;
    error = int;
    
    #inicialitzem variables
    error= 1;
    
    while(error):  #mentre la captura de  l'enter no sigui exitosa, continuem...
        try:  #provem de reclamar el nombre enter
            textRetorn = input(text);
            error = 0;   #només canviem l'estat de la variable en cas de captura correcta.
        except:  #en cas d'error...
            print("S'ha produit un error en la introducció. Torna a provar...");
    
    return textRetorn;

try:
	file = open("hola2.txt", "w");	
except:
	print("ERROR DEL FICHERO");
	exit

text = str("");

while(text != "."):
	text = llegirText("Introduce texto.... ");
	file.write(text + os.linesep)

print("Fin Programa, cerrando archivo");
file.close()
