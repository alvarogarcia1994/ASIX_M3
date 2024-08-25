#!/usr/bin/env python
#-*- coding: utf-8 -*-



def numerets():
    l11 = []
    for i in range(intro):
        nombre = int(input())
        l11.append(nombre)
    return l11
        

def majors_que_5(l11):
    print("Son majors que 5: ", end=" ")
    for j in range(len(l11)):
        if l11[j] > 5:
            print(l11[j], end=" ")
    return l11

intro = int(input("Quants nombres vols ? "))
Llista = numerets()
majors_que_5(Llista)