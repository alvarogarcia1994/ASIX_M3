from mc import *
import random
import sys

def dibuixa_linia(mc,x,y,z,tipus_bloc_inicial,longitud_costat):
    for j in range(longitud_costat):
        mc.setBlock(x+j,y,z,tipus_bloc_inicial)
        tipus_bloc_inicial = OBSIDIAN.id
       
   
mc = Minecraft()
x,y,z=mc.player.getTilePos()
x_inicial = x + 5
y_inicial = y
z_inicial = z
num_files = int(sys.argv[1])
blocs_fila = int(sys.argv[2])
tipus_bloc_inicial=OBSIDIAN.id

dibuixa_linia(mc,x_inicial,y_inicial,z_inicial,tipus_bloc_inicial,num_files)

for files in range(0,num_files):
    dibuixa_linia(mc,x_inicial,y_inicial,z_inicial,tipus_bloc_inicial,num_files)
    z_inicial = z_inicial + 1
    tipus_bloc_inicial = WOOL_ORANGE
    