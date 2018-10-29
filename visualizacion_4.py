#-*-coding: utf-8-*-
#!/usr/bin/env python

# Lógica para ciencias de la computación

#Proyecto desarrollado por Juan Camilo Llanos Gómez y Edwin Alejadro Forero Gómez
#2018 - II

#--------------------------------------------------- CUATRO DAMAS EN UN TABLERO DE AJEDRÉZ ----------------------------------------------------

# Visualizacion de tableros de ajedrez 4x4 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay una dama en la casilla.

# Formato de la entrada: - las letras proposionales seran: a, ..., p;
#                        - solo se aceptan literales (ej. a, ~b, c, ~d, etc.)
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
    direcciones['a'] = [0.125, 0.97]
    direcciones['b'] = [0.377, 0.97]
    direcciones['c'] = [0.63, 0.97]
    direcciones['d'] = [0.877, 0.97]
    #2
    direcciones['e'] = [0.125, 0.733]
    direcciones['f'] = [0.377, 0.733]
    direcciones['g'] = [0.63, 0.733]
    direcciones['h'] = [0.877, 0.733]
    #3
    direcciones['i'] = [0.125, 0.466]
    direcciones['j'] = [0.377, 0.466]
    direcciones['k'] = [0.63, 0.466]
    direcciones['l'] = [0.877, 0.466]
    #4
    direcciones['m'] = [0.125, 0.199]
    direcciones['n'] = [0.377, 0.199]
    direcciones['o'] = [0.63, 0.199]
    direcciones['p'] = [0.877, 0.199]

    #---------------------------------------------------------------------------------------------------------------------------------------

    for l in f:
        if '~' not in l:
            ab = AnnotationBbox(imagebox, direcciones[l], frameon=False)
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
    for y in data:
        print "Dibujando tablero:", y
        dibujar_tablero(y, contador)
        contador += 1

csv_file.close()
