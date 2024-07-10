

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
def llegirText(text="Introdueix un text \n"):
    '''
    La funció llegirText() llegeix l'entrada del teclat de l'usuari i si
    té un format correcte de text, el retorna.
    * paràmetres d'entrada: text (str): és el text amb que es demana a l'usuari
							la introducció del valor. Té un valor per 
							defecte si l'usuari no ho especifica
    * paràmetres de sortida: textRetorn (str)
    '''
     #declarem variables
    numRetorn = str;
    error = int;
    
    #inicialitzem variables
    error= 1;
    
    while(error):  #mentre la captura de  l'enter no sigui exitosa, continuem...
        try:  #provem de reclamar el nombre enter
            textRetorn = input(text);
            error = 0;   #només canviem l'estat de la variable en cas de captura correcta.
        except:  #en cas d'error...
            print("S'ha produit un error en la introducció. Torna a provar...");
    
    return textRetorn;
def imprimeixMatriu(matriu,perColumnes=False):
	'''  La funció imprimeixMatriu() imprimeix els valors
	d'una matriu passada per paràmetre. Si el paràmetre 
	perColumnes es true (1), la impressió serà per columnes 
    * paràmetres d'entrada: matriu (Matriu de dos dimensions NxM), 
							perColumnes(booleà). Indica si la impressió
							es fa per columnes. 
    * paràmetres de sortida: cap.
    * Autor: Oriol Capdevila 1r ASIX.(2017-2018).
    '''
    
	files = len(matriu)
	columnes = len(matriu[1])
	
	if perColumnes == False:
		for i in range(0,files):
				print();
				for x in range(0,columnes):
					print(matriu[i][x]," ", end="");
		print()
	elif perColumnes == True:
		for i in range(0,files):
				print();
				for x in range(0,columnes):
					print(matriu[x][i]," ", end="");   
        
def canviaStrAEnter(text):
	'''
    Aquesta funció rep un text com a paràmetre, el transforma a Enter i el retorna   
	'''
				
	return str(text);		

			
def completaFilera(matriu,filera):
	'''
	aquesta funció completa una de les fileres de la matriu. Ha de fer la suma de les 
	quantitats de la filera i actualitzar la darrera columna de la filera amb el resultat.
	Per  sumar els str de la matriu és obligatori fer us de la funció canviaStrAEnter()	 
	que heu implementat abans. 
    '''
    
	resultat = int;
	resultat = 0;
    
	for i in range(0,5):
		resultat += int(canviaStrAEnter(matriu[filera][i]));

	matriu[filera][5]= resultat;
		
		
    
    
def completaColumna(matriu, columna):
	'''aquesta funció compta quants elements d'una columna són una xifra major que 5000 
	i actualitza la darrera filera de la columna amb el valor obtingut.
	Per  tractar els str de la matriu és obligatori fer us de la funció canviaStrAEnter()	 
	que heu implementat abans.
	'''   
	 
	resultat = int;
	resultat = 0;
    
	for i in range(0,5):
		if (int(canviaStrAEnter(matriu[i][columna])) > 5000):
			resultat = resultat + 1;
	
	matriu[5][columna]= resultat;
    
    
#programa principal
	'''
	El programa principal ha de demanar l'usuari si vols actualitzar una filera o una columna
	També ha de demanar un enter que serà la filera o la columna que cal actualitzar. 
	Aneu en compte que no hi ha el mateix nombre de fileres i columnes. Quan demaneu a l'usuari
	el valor tingueu això en compte...
	Una vegada tenim  les dades hem de cridar la funció adient per actualigtzar la matriu.
	Després cal imprimir-la. Recordeu que ja tenim una funció que imprimeix matrius.	
    '''  
#matriu de treball... 
''' 
aquesta matriu conté uns valors i una columna i filera extra per actualitzar-la amb les
funcions. Fixeu-vos-hi que els valors són str i els que hem d'actualitzar són enters.
'''
matriu =  [  ['2764', '7650', '8757', '6432', '9822', 0],
             ['5343', '8734', '1112', '0965', '7753', 0],
             ['6556', '5547', '9986', '6653', '1276', 0],
             ['7432', '8932', '1111', '1238', '2346', 0],
             ['5421', '7659', '9873', '4845', '8734', 0],
             [0,        0,      0,      0,      0,    0]
           ]
       

fileraOcolumna = str;
valor = int;
imprimeixMatriu(matriu,0);

while(1):
	fileraOcolumna = llegirText("Què vols actualitzar? filera/columna\n");
	valor = llegirEnterInterval(0,4,"Quina columna/filera vols actualitzar\n");

	if (fileraOcolumna == "columna"):
		completaColumna(matriu, valor);
	if (fileraOcolumna == "filera"):
		completaFilera(matriu,valor); 
		
	imprimeixMatriu(matriu,0);

