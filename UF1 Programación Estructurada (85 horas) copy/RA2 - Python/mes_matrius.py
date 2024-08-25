#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print ("Entrada de dades del soci")
print ("-------------------------")
#Entrada de dades

print ("Nom del soci:")
nom = str(input())

print ("Cognoms del soci:")
cognom = str(input())

print ("Es home o dona:")
print ("(Si es home introdueixi el valor 0, en cas de ser dona, el valor 1.)")
sexe = int(input())
genere = str
home = str("Home")
dona = str("Dona")

#Per a asegurar la correcta introducció de les dades.
while sexe != 0 and sexe != 1:
	print ("Aquesta opcio no es valida, introduiula un altre cop si us plau.")
	sexe = int(input())
	
if sexe == 0:
	genere = home
if sexe == 1:
	genere = dona

print ("Quants anys té:")
edat = int(input())
categoria = str
infantil = str("Infantil")
juvenil = str("Juvenil")
senior = str("Senior")

#Per a asegurar la correcta introduccio de les dades.
while edat < 4:
	print ("Aquestes edats no son valides, introduiula un altre cop si us plau.")
	edat = int(input())
while edat > 150:
	print ("Aquestes edats no son valides, introduiula un altre cop si us plau.")
	edat = int(input())	

	
	
if edat <= 14:
	categoria = infantil
if edat > 14 and edat <= 18:
	categoria = juvenil
if edat > 18:
	categoria = senior

print ("A quina poblacio  viu?")
poblacio = str(input())

#Generació del codi
#Podar el nom al codi
pNom = nom[0]
sNom = nom[1]
#Posar el cognom al codi
pCog = cognom[0]
longitud = len(cognom)
uCog = cognom[longitud-1]
 
if sexe == 0:
	pGen = home[0]
if sexe == 1:
	pGen = dona[0]

codi = pNom + sNom + pCog + uCog + str(edat) + pGen
dades = [codi, nom, cognom, genere, edat, poblacio, categoria]

#Neteja de pantalla
print ("prem Enter...")
input()
os.system("clear")


#Sortida de dades
print ("Dades del soci")
print ("--------------")

print (dades)
