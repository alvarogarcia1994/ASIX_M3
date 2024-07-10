#!/usr/bin/env python
# -*- coding: utf-8 -*-

numero = int(input("Dime un número: "))

if numero < 1:
    print("Eso no tiene sentido")
else:
   lista_primos = []
   for a in range(numero+1):
       contador = 0
       for b in range(1, a+1):
           if a % b == 0:
               contador += 1
       if contador == 2:
           lista_primos +=[a]

print("Primos hasta ",numero,": ",lista_primos)