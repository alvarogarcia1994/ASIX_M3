def retorna_grans_per_casella():
    caselles = 64
    total_gr = 0
    for x in range(caselles):
        gr = 2 ** x
        print("A la casella ", str(x+1), "n'hi ha ", gr, "grans de blat")
        total_gr += gr
    return total_gr

def retorna_tones_metriques():
    gr = retorna_grans_per_casella()
    grans_per_kilo = 1200
    produccio_UE = 142896000
    x = gr / grans_per_kilo
    ton = x / 1000
    total = ton / produccio_UE
    return total

print("Total de grans de blat: ", retorna_grans_per_casella())
print("Li portarà ", retorna_tones_metriques(), " anys de producció")
