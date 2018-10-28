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
    step = 1./4
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
    tangulos.append(patches.Rectangle(*[(step *3, 0), step, step],\
    		facecolor='#F3F3F3'))
    tangulos.append(patches.Rectangle(*[(3 * step, 2 * step), step, step],\
    		facecolor='#F3F3F3'))
   
    # Creamos los cuadrados oscuros en el tablero________________________________________________________________________________________________
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
    tangulos.append(patches.Rectangle(*[(step * 3, step), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step , step * 3), step, step],\
    		facecolor='#D44020'))
    tangulos.append(patches.Rectangle(*[(step * 3, step * 3), step, step],\
    		facecolor='#D44020'))
    
    # Creamos las líneas del tablero--------------------------------------------------------------------------------------------------------------
    for j in range(4):
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
    imagebox = OffsetImage(arr_img, zoom=0.05)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal--------------------------------------------------------------------------------
    direcciones = {}
    #1
    direcciones[1] = [0.125, 0.97]
    direcciones[2] = [0.377, 0.97]
    direcciones[3] = [0.63, 0.97]
    direcciones[4] = [0.877, 0.97]
    #2
    direcciones[5] = [0.125, 0.733]
    direcciones[6] = [0.377, 0.733]
    direcciones[7] = [0.63, 0.733]
    direcciones[8] = [0.877, 0.733]
    #3
    direcciones[9] = [0.125, 0.466]
    direcciones[10] = [0.377, 0.466]
    direcciones[11] = [0.63, 0.466]
    direcciones[12] = [0.877, 0.466]
    #4
    direcciones[13] = [0.125, 0.199]
    direcciones[14] = [0.377, 0.199]
    direcciones[15] = [0.63, 0.199]
    direcciones[16] = [0.877, 0.199]

    #---------------------------------------------------------------------------------------------------------------------------------------

    for l in f:
        if '~' not in l:
            ab = AnnotationBbox(imagebox, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)

    # plt.show()----------------------------------------------------------------------------------------------------------------------------
    fig.savefig("Dama_" + str(n) + ".png")


#################
# Importando paquetes para dibujar
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
