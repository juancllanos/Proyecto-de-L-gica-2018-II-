#-*-coding: utf-8-*-

# Juan Camilo LLanos y Edwin Forero, 2018
# Codigo para crear la formula del problema de las damas

print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente ocho damas

# Se crean las letras proposicionales
letrasProposicionales = []
for i in range(1, 65):
    letrasProposicionales.append(str(i))
    
# Regla 1: Debe haber exactamente ocho damas
conjunciones = '' # Para ir guardando las conjunciones de tamaño ocho de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion

for p in letrasProposicionales:
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto p
    for q in aux1:
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        for r in aux2:
            aux3=[x for x in aux2 if x != r]# Todas las letras excepto p, q y r
            for s in aux3:
                aux4 = [x for x in aux3 if x != s] # Todas las letras excepto p,q,r y s
                for t in aux4:
                    aux5 = [x for x in aux4 if x != t] # Todas las letras excepto p,q,r,s y t
                    for u in aux5:
                        aux6 = [x for x in aux5 if x!=u] # Todas las letras excepto p,q,r,s,t y u
                        for v in aux6:
                            aux7 = [x for x in aux6 if x != v] # Todas las letras excepto p,q,r,s,t,u y v
                            for w in aux7:
                                literal = w+v+u+t+s+r+q+p+'Y'+'Y'+'Y'+'Y'+'Y'+'Y'+'Y'
                                aux8 = [x+'-' for x in aux7 if x != w]# Todas las letras excepto p,q,r,s,t,u,v y w
                                for x in aux8:
                                    literal = x + literal + 'Y' # concatena las letras proposicionales restantes agregandoles una negacion y un 'Y'
                                if inicial:
                                    conjunciones = literal
                                    inicial = False
                                else:
                                    conjunciones = literal + conjunciones + 'O' # Concatena las posibles formulas con una 'O'

# Regla 2: Ninguna dama debe poder atacar a otra

conjunciones = '8-6-Y1>' + conjunciones + 'Y'
conjunciones = '9-7-Y2>' + conjunciones + 'Y'
conjunciones = '8-4-Y3>' + conjunciones + 'Y'
conjunciones = '9-3-Y4>' + conjunciones + 'Y'
conjunciones = '7-1-Y6>' + conjunciones + 'Y'
conjunciones = '6-2-Y7>' + conjunciones + 'Y'
conjunciones = '3-1-Y8>' + conjunciones + 'Y'
conjunciones = '4-2-Y9>' + conjunciones + 'Y'

# Creo la formula como objeto

A = T.StringtoTree(conjunciones, letrasProposicionales)
print "Formula: ", T.Inorder(A)

lista_hojas = [[A]] # Inicializa la lista de hojas

OK = '' # El tableau regresa Satisfacible o Insatisfacible
interpretaciones = [] # lista de lista de literales que hacen verdadera lista_hojas

OK, INTS = T.Tableaux(lista_hojas, letrasProposicionales)

print "Tableau terminado!"
# Guardo el tiempo al terminar el procedimiento
end = timer()
print u"El procedimiento demoró: ", end - start

if OK == 'Satisfacible':
    if len(INTS) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'tableros_automatico.csv'
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
