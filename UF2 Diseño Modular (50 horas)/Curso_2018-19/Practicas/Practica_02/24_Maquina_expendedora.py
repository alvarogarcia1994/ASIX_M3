#!/usr/bin/env python
# -*- coding: utf-8 -*-

def saldo(dinero):
	billete_500 = dinero//500
	sobra = dinero - 500 * billete_500
	billete_200 = sobra//200
	sobra = sobra - 200 * billete_200
	billete_100 = sobra//100
	sobra = sobra - 100 * billete_100
	billete_50 = sobra//50
	sobra = sobra - 50 * billete_50
	billete_20 = sobra//20
	sobra = sobra - 20 * billete_20
	billete_10 = sobra//10
	sobra = sobra - 10 * billete_10
	billete_5 = sobra//5
	sobra = sobra - 5 * billete_5
	coin_2 = sobra//2
	sobra = sobra - 2 * coin_2
	coin_1 = sobra//1
	sobra = sobra - 1 * coin_1
	
	return billete_500, billete_200, billete_100, billete_50, billete_20, billete_10, billete_5, coin_2, coin_1, sobra

dinero = int(input("Introduce una cantidad: "))
billete_500, billete_200, billete_100, billete_50, billete_20, billete_10, billete_5, coin_2, coin_1, sobra = saldo(dinero)

print("Cambio de 500: ", billete_500)
print("Cambio de 200: ", billete_200)
print("Cambio de 100: ", billete_100)
print("Cambio de 50: ", billete_50)
print("Cambio de 20: ", billete_20)
print("Cambio de 10: ", billete_10)
print("Cambio de 5: ", billete_5)
print("Cambio de 2: ", coin_2)
print("Cambio de 1: ", coin_1)
