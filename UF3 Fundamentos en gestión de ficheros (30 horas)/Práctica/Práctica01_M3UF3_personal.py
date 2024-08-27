#Lectura
import os
try:
    file = open("personal.txt",  "r");
except FileNotFoundError:
    print("No existe el archivo");

#Bloque de variables
texto = str
linea = str
categoria = str
empleados = int
total = 0
total_admin = 0
total_nodoc = 0
total_exadmin = 0
empleados = 0
blinky = 0
tinky = 0
inky = 0

#Primero vamos a sacar el numero de trabajadores
texto= file.readline()
texto= file.readline()

#Calculamos la suma de los 3 salarios restantes
while (texto !="end file\n"):
	categoria = texto.split(" ")
	empleados = empleados +1
	if (texto=="end file\n"):
		break
	categoria[4]= categoria[4][:len(categoria[4])-5]
	total= total+int(categoria[4])
	if (categoria[3]!="Docente"):
		total_nodoc= total_nodoc+int(categoria[4])
		
	if (categoria[3] == "Administrativo"):
		total_admin = total_admin+int(categoria[4])
	else:
		total_exadmin = total_exadmin+int(categoria[4])
	texto = file.readline();

# Si todo ha ido bien, saldrá este mensaje
print("Informe generado")

# Proceso de generación
file=open("Personal_Alvaro.txt", "w");
file.write("       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "+ os.linesep)
file.write("				INFORME DE PERSONAL"+ os.linesep)
file.write("       - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"+ os.linesep)
file.write(""+ os.linesep)
file.write("NOMBRE DE TREBALLADORS: ")
file.write(str((empleados)))
file.write(""+ os.linesep)
file.write("SUMA TOTAL EN SOUS:")
file.write(str((total)))
file.write(""+ os.linesep)
file.write(""+ os.linesep)
file.write("SUMA TOTAL DE SOUS EN PERSONAL ADMINISTRATIU:")
file.write(str((total_admin)))
file.write(""+ os.linesep)
file.write("SUMA TOTAL DE SOUS EN PERSONAL NO DOCENT: ")
file.write(str((total_nodoc)))
file.write(""+ os.linesep)
file.write(""+ os.linesep)

file.write("3 Trabajadores Con Sueldo Mas Alto: "+ os.linesep)
file.write("1.- PINKY -  sou: "+ os.linesep)
file.write("2.- BLINKY -  sou: "+os.linesep)
file.write("3.- INKY -  sou: " +os.linesep)
file.write(""+ os.linesep)
file.close();
