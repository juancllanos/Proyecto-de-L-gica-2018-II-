#-*-coding: utf-8-*-


print "Importando paquetes..."
from timeit import default_timer as timer
import cnf as T
import DPLL as D
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()


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

# Regla 2: Ningun alfíl debe poder atacar a otro

conjunciones = '9-5-Y1>' + conjunciones + 'Y'
conjunciones = '6-4-Y2>' + conjunciones + 'Y'
conjunciones = '7-5-Y3>' + conjunciones + 'Y'
conjunciones = '8-2-Y4>' + conjunciones + 'Y'
conjunciones = '1-3-7-9-YYY5>' + conjunciones + 'Y'
conjunciones = '8-2-Y6>' + conjunciones + 'Y'
conjunciones = '3-5-Y7>' + conjunciones + 'Y'
conjunciones = '6-4-Y8>' + conjunciones + 'Y'
conjunciones = '1-5-Y9>' + conjunciones + 'Y'

###########################################



A = T.StringtoTree(conjunciones, letrasProposicionales)
print "Formula: ", T.Inorder(A)

A = T.quitarDobleNegacion(A)
print "La fórmula sin dobles negaciones es:\n "
print T.Inorder(A)

A = T.reemplazarImplicacion(A)

print "La fórmula reemplazando implicaciones es:\n "
print T.Inorder(A)

A = T.quitarDobleNegacion(A)

print "La fórmula sin dobles negaciones es:\n " 
print T.Inorder(A)

OK = True
while OK:
    aux1 = T.Inorder(A)
    print "Se analiza: ", aux1
    B = T.deMorgan(A)
    B = T.quitarDobleNegacion(B)
    aux2 = T.Inorder(B)
    print "Se obtuvo : ", aux2
    if  aux1 != aux2:
        print "Se aplicó deMorgan" 
        OK = True
        A = B
    else:
        print "No se aplicó deMorgan"
        OK = False


while OK:
    OK, A = T.aplicaDistributiva(A)

conjuntoClausulas = T.formaClausal(A)

print "Conjunto de disyunciones de literales: "
print conjuntoClausulas

I = {}

print "\n "
print D.DPLL(conjuntoClausulas,I)