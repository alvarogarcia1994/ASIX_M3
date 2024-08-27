def triangulo(intro):
	if intro >= 1:
		for a in range(1, intro +1):
			print(a, end=" ")
	else:
		print("No vale")

intro = int(input("Introduce un número: "))
for a in range(1, intro +1):
	triangulo(a)
	print()
