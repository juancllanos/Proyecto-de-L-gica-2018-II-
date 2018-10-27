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
for i in range(1, 17):
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

conjunciones = '2-3-4-5-9-13-6-11-16-YYYYYYYY1>' + conjunciones + 'Y'                                                              #1
conjunciones = '1-3-4-5-6-7-12-10-14-YYYYYYYY2>' + conjunciones + 'Y'                                                             #2
conjunciones = '1-2-4-6-9-8-7-11-15-YYYYYYY3>' + conjunciones + 'Y'                                                                #3
conjunciones = '1-2-3-8-12-16-7-10-13-YYYYYYYY4>'+ conjunciones + 'Y'                                                              #4
conjunciones = '1-2-6-9-13-10-15-7-8-YYYYYYYY5>' + conjunciones + 'Y'                                                              #5
conjunciones = '2-1-3-5-7-8-9-11-16-10-14-YYYYYYYYYY6>' + conjunciones + 'Y'                                                       #6
conjunciones = '3-4-2-6-5-8-10-13-12-11-15-YYYYYYYYYY7>' + conjunciones + 'Y'                                                      #7
conjunciones = '4-3-7-6-5-11-14-12-16-YYYYYYYY8>' + conjunciones + 'Y'                                                             #8
conjunciones = '1-5-13-6-3-10-11-12-14-YYYYYYYY9>' + conjunciones + 'Y'                                                            #9
conjunciones = '9-11-12-14-6-2-5-7-4-13-15-YYYYYYYYYY10>' + conjunciones + 'Y'                                                     #10
conjunciones = '9-10-12-3-7-15-6-1-8-14-16-YYYYYYYYYY11>' + conjunciones + 'Y'                                                     #11
conjunciones = '8-4-16-9-10-11-15-7-2-YYYYYYYY12>' + conjunciones + 'Y'                                                            #12
conjunciones = '9-5-1-10-7-4-14-15-16-YYYYYYYY13>' + conjunciones + 'Y'                                                            #13
conjunciones = '13-15-16-10-6-2-9-11-8-YYYYYYYY14>' + conjunciones + 'Y'                                                           #14
conjunciones = '13-14-16-10-5-12-11-7-3-YYYYYYYY15>' + conjunciones + 'Y'                                                          #15
conjunciones = '12-8-4-13-14-15-11-6-1-YYYYYYYY16>' + conjunciones + 'Y'                                                           #16


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
