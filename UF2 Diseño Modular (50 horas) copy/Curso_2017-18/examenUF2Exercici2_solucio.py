
def llegirEnterInterval(num1, num2, text="Introdueix un enter entre "):
    '''
    La funció llegirEnterInterval() llegeix l'entrada del teclat de l'usuari i si
    el nombre introduit té un format correcte de nombre enter i es troba en l’intèrval
    demanat pels paràmetres introduïts, el retorna.
    * paràmetres d'entrada: num1 (enter), num2 (enter)
    * paràmetres de sortida: numReturn (enter)
    '''
     #declarem variables
    numRetorn = int;
    error = int;
    aux = int;
    
    #inicialitzem variables
    error= 1;
    
    if (num1 > num2):
        aux = num1;
        num1 = num2;
        num2 = aux;
        
    while(error):  #mentre la captura de  l'enter no sigui exitosa, continuem...
        try:  #provem de reclamar el nombre enter
            print(text, num1, " - ", num2, "\n");
            numRetorn = int(input());
            if (numRetorn >= num1 and numRetorn <= num2):
                error = 0;   #només canviem l'estat de la variable en cas de captura correcta.
            else:
                print("El nombre no està dins l'intèrval");
        except:  #en cas d'error...
            print("S'ha produit un error en la introducció. Torna a provar...");
    
    return numRetorn; 
        
        
def nombreMines(mines, a, b):
	'''
        Aquesta funció ens diu quàntes mines (Les cantonades també!!!), 
        hi ha al voltant de la coordenada passada per paràmetre. 
        a representa la filera i b la columna.
        La funció haurà de retornar un valor enter amb el nombre de mines trobades
        Si la coordenada demanada conté una mina, la resposta de la funció haurà de ser
        l'enter 9.
	'''
	resultat = int;
	resultat = 0;
	        
    # mina encertada
	if  (mines[a][b] == 'M'):
		resultat = 9;
	else:
		#mirem els 8 costats
		if (mines[a-1][b-1] == 'M'):
			resultat += 1;
		if (mines[a-1][b] == 'M'):
			resultat += 1;
		if (mines[a-1][b+1] == 'M'):
			resultat += 1;
		if (mines[a][b+1] == 'M'):
			resultat += 1;
		if (mines[a][b-1] == 'M'):
			resultat += 1;
		if (mines[a+1][b-1] == 'M'):
			resultat += 1;
		if (mines[a+1][b] == 'M'):
			resultat += 1;
		if (mines[a+1][b+1] == 'M'):
			resultat += 1;
			
	return resultat;		
			
		  
    
    
#programa principal
	'''En el mètode principal, caldrà que implementeu, un petit codi que, utilitzant la funció
        nombreMines() ens imprimeixi quàntes mines hi ha al voltant d'una coordenada determinada.
        També les cantonades!!!! o si s'ha encertat una mina.
        '''  
#matriu de treball... 
''' Les 'M' representen una mina i les 'x' representen una posició buida. Els '0' només
		delimiten el camp d'acció. De manera que per demanar una posició a la matriu no
		són vàlides la primera i última filera i la primera i última columna.
		Això es fa per evitar problemes de accesos a coordenades invàlides quan cerqueu mines.
		L'usuari haurà de demanar SEMPRE entre les coordenades que NO són '0'.
'''
mines =  [   ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
             ['0', 'x', 'x', 'x', 'M', 'x', 'M', 'x', 'M', '0'],
             ['0', 'x', 'x', 'M', 'x', 'x', 'x', 'x', 'x', '0'],
             ['0', 'M', 'x', 'x', 'x', 'x', 'x', 'x', 'M', '0'],
             ['0', 'x', 'M', 'x', 'M', 'x', 'x', 'x', 'x', '0'],
             ['0', 'x', 'x', 'x', 'x', 'x', 'M', 'x', 'M', '0'],
             ['0', 'M', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '0'],
             ['0', 'x', 'x', 'M', 'x', 'x', 'x', 'M', 'M', '0'],
             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
           ]
       
filera = int;
columna = int;
resposta = int;
while(1):
	filera = llegirEnterInterval(1,7,"Introdueix la coordenada filera");
	columna = llegirEnterInterval(1,8, "Introdueix la coordenada columna");
	resposta = nombreMines(mines, filera,columna);
	if (resposta == 9):
		print("Has encertat amb una mina!!!");
	else:
		print("Al voltant de la coordenada hi ha " + str(resposta) + " mines");

