#-*-coding: utf-8-*-
#!/usr/bin/env python

# Lógica para ciencias de la computación

#Proyecto desarrollado por Juan Camilo Llanos Gómez y Edwin Alejadro Forero Gómez
#2018 - II

#--------------------------------------------------- OCHO DAMAS EN UN TABLERO DE AJEDRÉZ ----------------------------------------------------

# Visualizacion de tableros de ajedrez 8x8 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay una dama en la casilla.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 64;
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
    #   - archivo de imagen Dama_n.png

    # Inicializo el plano que contiene la figura---------------------------------------------------------------------------------------------
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero_______________________________________________________________________________________________________________________
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
    # Creo los cuadrados oscuros en el tablero________________________________________________________________________________________________
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
    # Creo las líneas del tablero--------------------------------------------------------------------------------------------------------------
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

    # Cargando imagen de una dama--------------------------------------------------------------------------------------------------------------
    arr_img = plt.imread("dama.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.03)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal--------------------------------------------------------------------------------
    direcciones = {}
    direcciones[1] = [0.063, 1]
    direcciones[2] = [0.19, 1]
    direcciones[3] = [0.315, 1]
    direcciones[4] = [0.44, 1]
    direcciones[5] = [0.568, 1]
    direcciones[6] = [0.69, 1]
    direcciones[7] = [0.815, 1]
    direcciones[8] = [0.94, 1]
    #2
    direcciones[9] = [0.063, 0.875]
    direcciones[10] = [0.19, 0.875]
    direcciones[11] = [0.315, 0.875]
    direcciones[12] = [0.44, 0.875]
    direcciones[13] = [0.568, 0.875]
    direcciones[14] = [0.69, 0.875]
    direcciones[15] = [0.815, 0.875]
    direcciones[16] = [0.94, 0.875]
    #3
    direcciones[17] = [0.063, 0.75]
    direcciones[18] = [0.19, 0.75]
    direcciones[19] = [0.315, 0.75]
    direcciones[20] = [0.44, 0.75]
    direcciones[21] = [0.568, 0.75]
    direcciones[22] = [0.69, 0.75]
    direcciones[23] = [0.815, 0.75]
    direcciones[24] = [0.94, 0.75]
    #4
    direcciones[25] = [0.063, 0.625]
    direcciones[26] = [0.19, 0.625]
    direcciones[27] = [0.315, 0.625]
    direcciones[28] = [0.44, 0.625]
    direcciones[29] = [0.568, 0.625]
    direcciones[30] = [0.69, 0.625]
    direcciones[31] = [0.815, 0.625]
    direcciones[32] = [0.94, 0.625]
    #5
    direcciones[33] = [0.063, 0.5]
    direcciones[34] = [0.19, 0.5]
    direcciones[35] = [0.315, 0.5]
    direcciones[36] = [0.44, 0.5]
    direcciones[37] = [0.568, 0.5]
    direcciones[38] = [0.69, 0.5]
    direcciones[39] = [0.815, 0.5]
    direcciones[40] = [0.94, 0.5]
    #6
    direcciones[41] = [0.063, 0.375]
    direcciones[42] = [0.19, 0.375]
    direcciones[43] = [0.315, 0.375]
    direcciones[44] = [0.44, 0.375]
    direcciones[45] = [0.568, 0.375]
    direcciones[46] = [0.69, 0.375]
    direcciones[47] = [0.815, 0.375]
    direcciones[48] = [0.94, 0.375]
    #7
    direcciones[49] = [0.063, 0.25]
    direcciones[50] = [0.19, 0.25]
    direcciones[51] = [0.315, 0.25]
    direcciones[52] = [0.44, 0.25]
    direcciones[53] = [0.568, 0.25]
    direcciones[54] = [0.69, 0.25]
    direcciones[55] = [0.815, 0.25]
    direcciones[56] = [0.94, 0.25]
    #8
    direcciones[57] = [0.063, 0.125]
    direcciones[58] = [0.19, 0.125]
    direcciones[59] = [0.315, 0.125]
    direcciones[60] = [0.44, 0.125]
    direcciones[61] = [0.568, 0.125]
    direcciones[62] = [0.69, 0.125]
    direcciones[63] = [0.815, 0.125]
    direcciones[64] = [0.94, 0.125]

    #---------------------------------------------------------------------------------------------------------------------------------------

    for l in f:
        if '~' not in l:
            ab = AnnotationBbox(imagebox, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)

    # plt.show()----------------------------------------------------------------------------------------------------------------------------
    fig.savefig("Dama_" + str(n) + ".png")


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
    data = csv.reader(csv_file, delimiter=';')
    contador = 1
    for l in data:
        print "Dibujando tablero:", l
        dibujar_tablero(l, contador)
        contador += 1

csv_file.close()
