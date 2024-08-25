Proceso sin_titulo
	
	// bloque de variables
	Definir A como entero;
	Definir B como entero;
	Definir C como entero;
	Definir X1 como entero;
	Definir X2 como entero;
	Definir discriminante como entero;
	
	// Entrada de datos
	Escribir "Calculadora de ecuaciones de 2º grado";
	Escribir "AX^2 + BX + C";
	Escribir "=========";
	Escribir Sin Saltar "Introduce el valor de A ----> ";
	Leer A;
	Limpiar Pantalla;
	Escribir "Calculadora de ecuaciones de 2º grado";
	Escribir A,"X^2 + BX + C ";
	Escribir "===========";
	Escribir Sin Saltar "Introduce el valor de B ----> ";
	Leer B;
	Limpiar Pantalla;
	Escribir "Calculadora de ecucaciones de 2º grado";
	Escribir A,"X^2 + ",B,"X + C ";
	Escribir "============";
	Escribir Sin Saltar "Introduce el valor de C ----> ";
	Leer C;
	Limpiar Pantalla;
	Escribir "Calculadora de ecuaciones de 2º grado";
	Escribir A,"X^2 + ",B,"X"," + ",C;
	Escribir "============";
	discriminante<-(B^2)-(4*A*C);
	X1<- ((-B)+ rc(discriminante))/2*A;
	X2<- ((-B)- rc(discriminante))/2*A;
	
	//salida de datos
	Escribir "X1: ",X1;
	Escribir "X2: ",X2;
	Escribir "D: ",discriminante;
	
FinProceso
