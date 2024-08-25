Proceso sin_titulo
	
		//bloque de variables
		Definir nota,i,peor Como entero;
		Definir nombre,nomb_menor como caracter;
		
		//Entrada de datos y cálculo de las notas
		Escribir "define el numero de alumnos ";
	Leer nota;
	peor<-300;
	suma<-0;
	Para i<-0 Hasta nota-1 Con Paso 1 Hacer
		Escribir "alumno ", i+1;
		Leer nombre;
		Escribir "introduce nota del alumno ";
		Leer nota;
		suma<-suma+nota;
		Si nota < peor Entonces
			peor<-nota;
			nomb_menor<-nombre;
		FinSi
	FinPara
	mediana<-suma/nota;
	
	//Resultados obtenidos
Escribir "La mediana es ", mediana;
Escribir "La peor nota es del alumno: ", nomb_menor ," con la nota: ", peor;
FinProceso