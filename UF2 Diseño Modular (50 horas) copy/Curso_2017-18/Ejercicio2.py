def canviaStrAEnter(text):
		
	return str(text);

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

def llegir1Caracter(text = "Introdueix un caràcter \n"):
    '''
    La funció llegir1Caracter() llegeix l'entrada del teclat de l'usuari i si
    té un format correcte de text (només un caràcter), el retorna.
    * paràmetres d'entrada: text (str): és el text amb que es demana a l'usuari
							la introducció del valor. Té un valor per 
							defecte si l'usuari no ho especifica
    * paràmetres de sortida: textReturn (str): només un caràcter.
    '''
     #declarem variables
    numRetorn = str;
    error = int;
    
    #inicialitzem variables
    error= 1;
    
    while(error):  #mentre la captura de  l'enter no sigui exitosa, continuem...
        try:  #provem de reclamar el nombre enter
            textRetorn = input(text);
            if (len(textRetorn) != 1): #en cas d'introducció de més d'un caràcter
                print("has d'introduir només un caràcter");
            else:
                error = 0;   #només canviem l'estat de la variable en cas de captura correcta.
        except:  #en cas d'error...
            print("S'ha produit un error en la introducció. Torna a provar...");
    
    return textRetorn;

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


#Variables
numero = int;
caracter = str;
texto = str;


while(1):
	numero = llegirEnterInterval(0,9, "\nIntroduce un entero entre 0 y 9: ");
	caracter = llegir1Caracter(text="\nIntroduce un caracter: ");
	texto = llegirText(text="\nIntrodueix un text: ");
		
	print(numero, caracter, texto);
	
		
