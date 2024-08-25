#!/usr/bin/env python
# -*- coding: utf-8 -*-

def a_sec(horas, minutos, segundos):
	horas = horas * 3600
	minutos = minutos * 60
	general = horas + minutos + segundos
	print(general, "Segundos")

horas=int(input("Introduce el numero de horas: "))
minutos=int(input("Introduce los minutos: "))
segundos=int(input("Introduce los segundos: "))

a_sec(horas, minutos, segundos)

def de_seg(sec):
	horas = int(sec/3600)
	minutos = int((sec-(horas*3600))/60)
	segundos = sec-((horas*3600)+(minutos*60))
	print(str(horas)+"h "+str(minutos)+"m "+str(segundos)+"s")

sec = int(input("Introduce el número de segundos: "))

de_seg(sec)
