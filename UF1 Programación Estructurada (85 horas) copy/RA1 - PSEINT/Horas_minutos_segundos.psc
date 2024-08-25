Algoritmo sin_titulo
	
	//bloque de variables
	Definir datos Como entero;
	Definir horas como real;
	Definir minutos como real;
	Definir nsegundos como real;
	
	//entrada de datos
	Escribir "define el numero de segundos";
	leer datos;
	
	//calculos
	horas <- datos/3600;
	minutos <- (datos mod 3600) / 60;
	nsegundos <- (datos mod 3600) mod 60;

	
	//salida de datos
	Escribir datos, " éstos segundos son ", TRUNC(horas), " horas ", TRUNC(minutos), " minutos ", TRUNC(nsegundos), " segundos ";
	
FinAlgoritmo
