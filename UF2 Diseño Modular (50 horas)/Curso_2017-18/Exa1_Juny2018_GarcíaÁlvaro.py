import os

#Función que recibirá por parámetros: un texto, un carácter y un entero
def detectaLletra(text,caracter,enter):
    contador = int()
    for a in range(0,len(text)):
        if caracter in text[a]:
            contador += 1
    if contador == enter:
        return True
    else:
        return False


#Variables
text = str(input("Text: "))
caracter = str(input("Caracter: "))
enter = int(input("Enter: "))

print(detectaLletra(text,caracter,enter))