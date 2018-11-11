#-*-coding: utf-8-*-



#Código para solucionar el problema de # Alfíles en un tablero de Ajedréz en un tablero de 3x3 por método de Tableau




print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente tres alfíles

# Creo las letras proposicionales
letrasProposicionales = []
for i in range(1, 10):
    letrasProposicionales.append(str(i))

# print "Letras proposicionales: ", letrasProposicionales

# Regla 1: Debe haber exactamente tres alfíles
conjunciones = '' # Para ir guardando las conjunciones de trios de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion

for p in letrasProposicionales:
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto
    # print "aux1: ", aux1
    for q in aux1:
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        # print "aux2", aux2
        for r in aux2:
            literal = r + q + p + 'Y' + 'Y'
            aux3 = [x + '-' for x in aux2 if x != r]
            for k in aux3:
                literal = k + literal + 'Y'
            # print "Literal: ", literal
            if inicial: # Inicializar la primera conjuncion
                conjunciones = literal
                inicial = False
            else:
                conjunciones = literal + conjunciones + 'O'

        # print "Conjunciones: ", conjunciones

# Regla 2: Ningun alfíi debe poder atacar a otro

conjunciones = '9-5-Y1>' + conjunciones + 'Y'
conjunciones = '6-4-Y2>' + conjunciones + 'Y'
conjunciones = '7-5-Y3>' + conjunciones + 'Y'
conjunciones = '8-2-Y4>' + conjunciones + 'Y'
conjunciones = '1-3-7-9-Y5>' + conjunciones + 'Y'
conjunciones = '8-2-Y6>' + conjunciones + 'Y'
conjunciones = '3-5-Y7>' + conjunciones + 'Y'
conjunciones = '6-4-Y8>' + conjunciones + 'Y'
conjunciones = '1-5-Y9>' + conjunciones + 'Y'


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
        archivo = 'alfil_sol.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print "Interpretaciones guardadas  en " + archivo

        import visualizacion_alfil as V
        contador = 1
        for i in INTS:
            print "Trabajando con literales: ", i
            V.dibujar_tablero(i,contador)
            contador += 1

print "FIN"