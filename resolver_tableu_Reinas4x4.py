# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:40:24 2018

@author: user
"""

#-*-coding: utf-8-*-
"""
                                        CÓDIGO PARA CREAR LA FÓRMULA AL PROBLEMA DE LAS 8 DAMAS

 Hecho por: Juan Camilo Llanos Gómez & Edwin Alejandro Forero Gómez

 Lógica para ciencias de la computación
 2018-II

En esta entrega crearemos la solución al problema de 4 reinas en un tablero de 4x4.

"""
#------------------------------------------------------------------------------------------------------------------------------------

print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
print "Importados!"

# Guardamos el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente ocho reinas en el tablero

# Creamos las letras proposicionales
letrasProposicionales = []
for i in range(97, 113):
    letrasProposicionales.append(str(i))

# print "Letras proposicionales: ", letrasProposicionales

# Regla 1: Debe haber exactamente ocho reinas en el tablero
conjunciones = '' # Para ir guardando las conjunciones de óctuples de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion

for p in letrasProposicionales:
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto p
    for q in aux1:
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        for r in aux2:
            aux3=[x for x in aux2 if x != r]# Todas las letras excepto p, q y r
            for s in aux3:
                literal = s + r + q + p + 'Y' + 'Y' + 'Y' 
                aux4 = [x + '-' for x in aux3 if x != s] # Todas las letras excepto p,q,r y s
                for j in aux4:
                    literal = j + literal + 'Y' # Agregamos la demás letras a la formula 
                if inicial:
                    conjunciones = literal      # Asignamos la primera conjuncion
                    inicial = False             # Se cambia el valor de inicial para agregar las demas con 'O'
                else:
                    conjunciones = literal + conjunciones +'O' # Se agregan las demas conjunciones con 'O'

# Regla 2: Ninguna reina debe poder atacar a otra

conjunciones = 'b-c-d-e-i-m-f-k-p-YYYYYYYYa>' + conjunciones + 'Y'                                                              #1
conjunciones = 'a-c-d-e-f-g-l-j-n-YYYYYYYYb>' + conjunciones + 'Y'                                                              #2
conjunciones = 'a-b-d-f-i-h-g-k-o-YYYYYYYc>' + conjunciones + 'Y'                                                               #3
conjunciones = 'a-b-c-h-l-p-g-j-m-YYYYYYYYd>'+ conjunciones + 'Y'                                                               #4
conjunciones = 'a-b-f-i-m-j-o-g-h-YYYYYYYYe>' + conjunciones + 'Y'                                                              #5
conjunciones = 'b-a-c-e-g-h-i-k-p-j-n-YYYYYYYYYY6f>' + conjunciones + 'Y'                                                       #6
conjunciones = 'c-d-b-f-e-h-j-m-l-k-o-YYYYYYYYYYg>' + conjunciones + 'Y'                                                        #7
conjunciones = 'd-c-g-f-e-k-n-l-p-YYYYYYYYh>' + conjunciones + 'Y'                                                              #8
conjunciones = 'a-e-m-f-c-j-k-l-n-YYYYYYYYi>' + conjunciones + 'Y'                                                              #9
conjunciones = 'i-k-l-n-f-b-e-g-d-m-o-YYYYYYYYYYj>' + conjunciones + 'Y'                                                        #10
conjunciones = 'i-j-l-c-g-o-f-a-h-n-p-YYYYYYYYYYk>' + conjunciones + 'Y'                                                        #11
conjunciones = 'h-d-p-i-j-k-o-g-b-YYYYYYYYl>' + conjunciones + 'Y'                                                              #12
conjunciones = 'i-e-a-j-g-d-n-o-p-YYYYYYYYm>' + conjunciones + 'Y'                                                              #13
conjunciones = 'm-o-p-j-f-b-i-k-h-YYYYYYYYn>' + conjunciones + 'Y'                                                              #14
conjunciones = 'm-n-p-j-e-l-k-g-c-YYYYYYYYo>' + conjunciones + 'Y'                                                              #15
conjunciones = 'l-h-d-m-n-o-k-f-a-YYYYYYYYp>' + conjunciones + 'Y'                                                              #16


# Creamos la fórmula como objeto

A = T.StringtoTree(conjunciones, letrasProposicionales)
print "Formula: ", T.Inorder(A)

lista_hojas = [[A]] # Inicializa la lista de hojas

OK = '' # El tableau regresa Satisfacible o Insatisfacible
interpretaciones = [] # Lista de lista de literales que hacen verdadera lista_hojas

OK, INTS = T.Tableaux(lista_hojas, letrasProposicionales)

print "Tableau terminado!"
# Guardamos el tiempo al terminar el procedimiento
end = timer()
print u"El procedimiento demoró: ", end - start

print OK
print INTS

if OK == 'Satisfacible':
    if len(INTS) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'damas.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print "Interpretaciones guardadas  en " + archivo

        import visualizacion as V
        contador = 1
        for i in INTS:
            print "Trabajando con literales: ", i
            V.dibujar_tablero(i,contador)
            contador += 1

print "FIN"
