import os

file = open("holaEv4", "a")

file.write(os.linesep)
file.write("1era linea" + os.linesep)
file.write("2da linea" + os.linesep)
file.close()
