caselles = 64

def retorna_grans_per_casella():
    for x in range(caselles+1):
        gr = 2 ** x
        print("A la casella ", str(x+1), "n'hi ha ", gr, "grans de blat")
    return gr

'def retorna_tones_metriques():'
    'gr = int'
    'grans_per_kilo = 1200'
    'produccio_UE = 142896000'
    'x = gr / grans_per_kilo'
    'ton = x / 1000'
    'total = ton / produccio_UE'
    'print("Li portara", total, "anys de producció")
    'return total'

print(retorna_grans_per_casella())
'print(retorna_tones_metriques())'
