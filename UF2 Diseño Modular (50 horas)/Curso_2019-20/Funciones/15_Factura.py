def ompleMatriu(matriu,comanda):
    for x in range(comanda):
        print("Nom del producte", str(x+1)+": ",end="")
        producte = str(input())
        print("Preu del producte", str(x+1)+": ",end="")
        preu = int(input())
        print("Quantitat del producte", str(x+1)+": ",end="")
        quantitat = int(input())
        sumatori = preu*quantitat###
        matriu[x]= [producte, preu, quantitat, sumatori]
    return matriu

print("Quants productes has comprat: ", end="")
comanda = int(input())
matriu= [[0 for j in range(4)] for i in range(comanda+1)]
matriu_plena=ompleMatriu(matriu,comanda)
print(matriu_plena)
#print("Resultat: ", (Factura))
#producte,preu,quantitat,sumatori = ompleMatriu(Factura)
#print(Factura)

sumatori = 0
for i in range(comanda):
    sumatori=sumatori+matriu[i][3]
    matriu[comanda][3]=sumatori
print("La suma es: ", sumatori)