#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def llegirText(text="Introdueix un text \n"):
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
            print("Se ha producido un error....");
    
    return textRetorn;

def llegir1Caracter(text = "Introdueix un caràcter \n"):
    
     #declarem variables
    numRetorn = str;
    error = int;
    
    #inicialitzem variables
    error= 1;
    
    while(error):  #mentre la captura de  l'enter no sigui exitosa, continuem...
        try:  #provem de reclamar el nombre enter
            textRetorn = input(text);
            if (len(textRetorn) != 1): #en cas d'introducció de més d'un caràcter
                print("has d'introduir només un caràcter");
            else:
                error = 0;   #només canviem l'estat de la variable en cas de captura correcta.
        except:  #en cas d'error...
            print("S'ha produit un error en la introducció. Torna a provar...");
    
    return textRetorn;

Nombre = str("");
Apellidos = str("");
Edad = str("");
MarcaVehiculo = str("");
ModeloVehiculo = str("");
Matricula = str("");
Exit = str("");

try:
	file = open("conductor.txt", "w");	
except:
	print("ERROR DEL FICHERO");
	exit


while( Exit!= "&"):
	Nombre = llegirText("Introduce Nombre.... ");
	Apellidos = llegirText("Intoduce los apellidos.... ");
	Edad = llegirText("Introduce la edad.... ");
	MarcaVehiculo = llegirText("Introduce el fabricante del vehiculo.... ");
	ModeloVehiculo = llegirText("Introduce el modelo del vehiculo.... ");
	Matricula = llegirText("Introduce el numero de matricula.... ");
	Exit = llegir1Caracter("Si deseas salir introduce &.... ");
	file.write("Datos del conductor" + "(" + Nombre + "," + Apellidos + "," + Edad + "," + MarcaVehiculo + "," + ModeloVehiculo + "," + Matricula + ")" + os.linesep)

print("Fin Programa, cerrando archivo");
file.close()
