def triangulo(intro):
	if intro > 0:
		for a in range(0, intro, 1):
			for b in range(a+1,0,-1):
				print(b, end=" ")
			print()
	else:
		print("Por favor, introduce un número a partir del 1 ")

intro = int(input("Introduce un número: "))
triangulo(intro)
