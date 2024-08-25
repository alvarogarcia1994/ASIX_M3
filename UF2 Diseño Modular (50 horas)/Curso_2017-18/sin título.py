def ActualitzaSaldo():
	
	#Variables
	jugador1 = str(input("Introduce tu nombre: "));
	saldoAnterior = int(input("Introduce saldo: "));
	saldoResultante = int(input("Introduce saldo a apostar: "));
	
if(saldoResultante > saldoAnterior):
	print("Has ganado saldo" and saldoAnterior+saldoResultante);
if(saldoResultante < saldoAnterior and saldoResultante > 0):
	print("Has perdido saldo, pero puedes seguir jugando" and saldoAnterior-saldoResultante);
if(saldoResultante<=0):
	print("No puedes continuar jugando");
	
ActualitzaSaldo()
