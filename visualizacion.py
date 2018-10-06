#-*-coding: utf-8-*-
#!/usr/bin/env python
# Edgar Andrade, Septiembre 2018

# Visualizacion de tableros de ajedrez 4x4 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay un caballo en la casilla.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 9;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere tambien un numero natural, para servir de indice del tablero,
# toda vez que puede solicitarse visualizar varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un numero natural


def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./8
    tangulos = []
    # Creo los cuadrados claros en el tablero
    tangulos.append(patches.Rectangle(*[(0, step), step, step],\
            facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step, 0), step, step],\
            facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(2 * step, step), step, step],\
            facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step],\
           facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(0, 3 * step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(2 * step, 3 * step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step, 4 * step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(0, 5 * step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(0, 7 * step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step, 6 * step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 2, 5 * step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 2, 7 * step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 3, 0), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 5, 0), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 7, 0), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 4, step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 6, step), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 3, step*2), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 5, step*2), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 7, step*2), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 4, step*3), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 6, step*3), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 3, step*4), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 5, step*4), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 7, step*4), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 4, step*5), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 6, step*5), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 3, step*6), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 5, step*6), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 7, step*6), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 4, step*7), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(step * 6, step*7), step, step],\
    		facecolor='#F3F3F3'))
    # Creo los cuadrados oscuros en el tablero
    tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step],\
            facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step],\
            facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step],\
            facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step, step), step, step],\
            facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(0, 0), step, step],\
            facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 4, 0), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 6, 0), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 3, step), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 5, step), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 7, step), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 4, step*2), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 6, step*2), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 3, step*3), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 5, step*3), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 7, step*3), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 4, step*4), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 6, step*4), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 3, step*5), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 5, step*5), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 7, step*5), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 4, step*6), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 6, step*6), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 3, step*7), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 5, step*7), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 7, step*7), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step, step*3), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step , step*5), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step, step*7), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 2, step*4), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 2, step*6), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(0, step*4), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(0, step*6), step, step],\
    		facecolor='#D44020'))
    # Creo las líneas del tablero
    for j in range(8):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagen de una dama
    arr_img = plt.imread("dama.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.05)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.165, 0.835]
    direcciones[2] = [0.5, 0.835]
    direcciones[3] = [0.835, 0.835]
    direcciones[4] = [0.165, 0.5]
    direcciones[5] = [0.5, 0.5]
    direcciones[6] = [0.835, 0.5]
    direcciones[7] = [0.165, 0.165]
    direcciones[8] = [0.5, 0.165]
    direcciones[9] = [0.835, 0.165]
    #
    direcciones[10] = [0.835, 0.165]
    direcciones[11] = [0.835, 0.165]
    direcciones[12] = [0.835, 0.165]
    direcciones[13] = [0.835, 0.165]
    direcciones[14] = [0.835, 0.165]
    direcciones[15] = [0.835, 0.165]
    direcciones[16] = [0.835, 0.165]
    direcciones[17] = [0.835, 0.165]
    direcciones[18] = [0.835, 0.165]
    direcciones[19] = [0.835, 0.165]
    direcciones[20] = [0.835, 0.165]

    for l in f:
        if '~' not in l:
            ab = AnnotationBbox(imagebox, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)

    # plt.show()
    fig.savefig("tablero_" + str(n) + ".png")


#################
# importando paquetes para dibujar
print "Importando paquetes..."
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import csv
from sys import argv
print "Listo!"

script, data_archivo = argv

with open(data_archivo) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    contador = 1
    for l in data:
        print "Dibujando tablero:", l
        dibujar_tablero(l, contador)
        contador += 1

csv_file.close()
