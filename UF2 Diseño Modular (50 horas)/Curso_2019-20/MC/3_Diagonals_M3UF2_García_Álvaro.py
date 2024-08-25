from mc import *
import random
import sys

def dibuixa_diagonal(mc,x,y,z,alt):
    tipus_block=OBSIDIAN.id
    for i in range(alt):
        mc.setBlock(x+i,y+i,z,tipus_block)
'''    for i in range(alt):
       
        mc.setBlock(x, y, z, tipus_block)
'''
mc = Minecraft()
x,y,z=mc.player.getTilePos()
x_inicial = x + 5
y_inicial = y
z_inicial = z + 4
total_diagonals = int(sys.argv[1])
alt = int(sys.argv[1])

for vegades in range(0,total_diagonals):
    dibuixa_diagonal(mc,x_inicial,y_inicial,z_inicial,vegades+1)
    x_inicial = x_inicial + total_diagonals
