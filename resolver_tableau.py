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
for i in range(1, 65):
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
                                    # print "Conjunciones: ", conjunciones

# Regla 2: Ninguna reina debe poder atacar a otra

conjunciones = '2-3-4-5-6-7-8-9-10-17-19-25-28-33-37-41-46-49-55-57-64-YYYYYYYYYYYYYYYYYYYY1>' + conjunciones + 'Y'#1
conjunciones = '1-3-4-5-6-7-8-9-10-11-18-20-26-29-34-38-42-47-50-56-58-YYYYYYYYYYYYYYYYYYYY2>' + conjunciones + 'Y'
conjunciones = '1-2-4-5-6-7-8-10-11-12-17-19-21-27-30-35-39-43-48-51-59-YYYYYYYYYYYYYYYYYYYY3>' + conjunciones + 'Y'
conjunciones = '1-2-3-5-6-7-8-11-12-13-18-20-22-15-28-31-36-40-44-52-60-YYYYYYYYYYYYYYYYYYYY4>' + conjunciones + 'Y'
conjunciones = '1-2-3-4-6-7-8-12-13-14-19-21-23-26-29-32-33-37-45-53-61-YYYYYYYYYYYYYYYYYYYY5>' + conjunciones + 'Y'
conjunciones = '1-2-3-4-5-7-8-13-14-15-20-22-24-27-30-34-38-41-46-54-62-YYYYYYYYYYYYYYYYYYYY6>' + conjunciones + 'Y'
conjunciones = '1-2-3-4-5-6-8-14-15-16-21-23-28-31-25-39-42-47-49-55-63-YYYYYYYYYYYYYYYYYYYY7>' + conjunciones + 'Y'
conjunciones = '1-2-3-4-5-6-7-15-16-22-24-29-32-36-40-43-48-50-56-57-64-YYYYYYYYYYYYYYYYYYYY8>' + conjunciones + 'Y'

conjunciones = '1-2-10-11-12-13-14-15-16-17-25-33-41-49-57-18-27-36-45-54-63-YYYYYYYYYYYYYYYYYYYY9>' + conjunciones + 'Y'#9
conjunciones = '1-2-3-9-11-12-13-14-15-16-17-18-19-26-28-34-37-42-46-50-55-58-64-YYYYYYYYYYYYYYYYYYYYYY10>' + conjunciones + 'Y'
conjunciones = '2-3-4-9-10-12-13-14-15-16-18-19-20-25-27-29-35-38-43-47-51-56-59-YYYYYYYYYYYYYYYYYYYYYY11>' + conjunciones + 'Y'
conjunciones = '3-4-5-9-10-11-13-14-15-16-19-20-21-26-28-30-33-36-39-44-48-52-60-YYYYYYYYYYYYYYYYYYYYYY12>' + conjunciones + 'Y'
conjunciones = '4-5-6-9-10-11-12-14-15-16-20-21-22-27-29-31-34-37-40-41-45-53-61-YYYYYYYYYYYYYYYYYYYYYY13>' + conjunciones + 'Y'
conjunciones = '5-6-7-9-10-11-12-13-15-16-21-22-23-28-30-32-35-38-42-46-49-54-62-YYYYYYYYYYYYYYYYYYYYYY14>' + conjunciones + 'Y'
conjunciones = '6-7-8-9-10-11-12-13-14-16-22-23-24-29-31-36-39-43-47-50-55-57-63-YYYYYYYYYYYYYYYYYYYYYY15>' + conjunciones + 'Y'
conjunciones = '7-8-9-10-11-12-13-14-15-23-24-30-32-37-40-44-48-51-56-58-64-YYYYYYYYYYYYYYYYYYY16>' + conjunciones + 'Y'

conjunciones = '1-3-9-10-18-19-20-21-22-23-24-25-26-33-35-41-44-49-53-57-62-YYYYYYYYYYYYYYYYYYYY17>' + conjunciones + 'Y'#17
conjunciones = '2-4-9-10-11-17-19-20-21-22-23-24-25-26-27-34-36-42-45-50-54-58-63-YYYYYYYYYYYYYYYYYYYYYY18>' + conjunciones + 'Y'
conjunciones = '1-3-5-10-11-12-17-18-20-21-22-23-24-26-27-28-35-37-43-46-51-55-59-64-YYYYYYYYYYYYYYYYYYYYYYY19>' + conjunciones + 'Y'
conjunciones = '2-4-6-11-12-13-17-18-19-21-22-23-24-27-28-29-34-36-38-41-44-47-52-56-60-YYYYYYYYYYYYYYYYYYYYYYYY20>' + conjunciones + 'Y'
conjunciones = '3-5-7-12-13-14-17-18-19-20-22-23-24-28-29-30-35-37-39-42-45-48-49-53-61-YYYYYYYYYYYYYYYYYYYYYYYY21>' + conjunciones + 'Y'
conjunciones = '4-6-8-13-14-15-17-18-19-20-21-23-24-29-30-31-36-38-40-43-46-50-54-57-62-YYYYYYYYYYYYYYYYYYYYYYYY22>' + conjunciones + 'Y'
conjunciones = '5-7-14-15-16-17-18-19-20-21-22-24-30-31-32-37-39-44-47-51-55-58-63-YYYYYYYYYYYYYYYYYYYYY23>' + conjunciones + 'Y'
conjunciones = '8-15-16-17-18-19-20-21-22-23-31-32-38-40-45-48-52-56-59-64-6-YYYYYYYYYYYYYYYYYYYY24>' + conjunciones + 'Y'

conjunciones = '1-4-9-11-17-18-26-27-28-29-30-31-32-33-34-41-43-49-52-57-61-YYYYYYYYYYYYYYYYYYY25>' + conjunciones + 'Y'#25
conjunciones = '2-5-10-12-17-18-19-25-27-28-29-30-31-32-33-34-35-42-44-50-53-58-62-YYYYYYYYYYYYYYYYYYYYYY26>' + conjunciones + 'Y'
conjunciones = '3-6-9-11-13-18-19-20-25-26-28-29-30-31-32-34-35-36-41-43-45-51-54-59-63-YYYYYYYYYYYYYYYYYYYYYYY27>' + conjunciones + 'Y'
conjunciones = '1-4-7-10-12-14-19-20-21-25-26-27-29-30-31-32-35-36-37-42-44-46-49-52-55-60-64-YYYYYYYYYYYYYYYYYYYYYYYYY28>' + conjunciones + 'Y'
conjunciones = '2-5-8-11-13-15-20-21-22-25-26-27-28-30-31-32-36-37-38-43-45-47-50-53-56-57-61-YYYYYYYYYYYYYYYYYYYYYYYYY29>' + conjunciones + 'Y'
conjunciones = '3-6-12-14-16-21-22-23-25-26-27-28-29-31-32-37-38-39-44-46-48-51-54-58-62-YYYYYYYYYYYYYYYYYYYY30>' + conjunciones + 'Y'
conjunciones = '4-7-13-15-22-23-24-25-26-27-28-29-30-32-38-39-40-45-47-52-55-60-63-YYYYYYYYYYYYYYYYYYYYYY31>' + conjunciones + 'Y'
conjunciones = '5-8-14-16-23-24-25-26-27-28-29-30-31-39-40-46-48-53-56-60-64-YYYYYYYYYYYYYYYYYYYY32>' + conjunciones + 'Y'

conjunciones = '1-5-9-12-17-19-25-26-34-35-36-37-38-39-40-41-42-49-51-57-60-YYYYYYYYYYYYYYYYYYYY33>' + conjunciones + 'Y'#33
conjunciones = '2-6-10-13-18-20-25-26-27-33-35-36-37-38-39-40-41-42-43-50-52-58-61-YYYYYYYYYYYYYYYYYYYYYY34>' + conjunciones + 'Y'
conjunciones = '3-7-11-14-17-19-21-26-27-28-33-34-36-37-38-39-40-42-43-44-49-51-53-62-YYYYYYYYYYYYYYYYYYYYYYY35>' + conjunciones + 'Y'
conjunciones = '4-8-9-12-15-18-20-22-27-28-29-43-44-45-50-52-54-57-60-63-33-34-35-37-38-39-40-YYYYYYYYYYYYYYYYYYYYYYYYY36>' + conjunciones + 'Y'
conjunciones = '1-5-10-13-16-19-21-23-28-29-30-44-45-46-33-34-35-36-38-39-40-51-53-55-58-61-64-YYYYYYYYYYYYYYYYYYYYYYYYY37>' + conjunciones + 'Y'
conjunciones = '2-6-11-14-20-22-24-29-30-31-33-34-35-36-37-39-45-46-47-52-54-56-59-62-YYYYYYYYYYYYYYYYYYYYYYY38>' + conjunciones + 'Y'
conjunciones = '3-7-12-15-21-23-30-31-32-33-34-35-36-37-38-40-46-47-48-53-55-60-63-YYYYYYYYYYYYYYYYYYYYYY39>' + conjunciones + 'Y'
conjunciones = '4-8-13-16-22-24-31-32-33-34-35-36-37-38-39-47-48-54-56-61-64-YYYYYYYYYYYYYYYYYYYY40>' + conjunciones + 'Y'

conjunciones = '1-6-9-13-17-20-25-27-33-34-42-43-44-45-46-47-48-49-50-57-59-YYYYYYYYYYYYYYYYYYYY41>' + conjunciones + 'Y'#41
conjunciones = '2-7-10-14-18-21-26-28-33-34-35-41-43-44-45-46-47-48-49-50-51-58-60-YYYYYYYYYYYYYYYYYYYYYY42>' + conjunciones + 'Y'
conjunciones = '3-8-11-15-19-22-25-27-29-34-35-36-41-42-44-45-46-47-48-50-51-52-57-59-61-YYYYYYYYYYYYYYYYYYYYYYY43>' + conjunciones + 'Y'
conjunciones = '4-12-16-17-20-23-26-28-30-35-36-37-41-42-43-45-46-47-48-51-52-53-58-60-62-YYYYYYYYYYYYYYYYYYYYYYYY44>' + conjunciones + 'Y'
conjunciones = '5--9-13-18-21-24-27-29-31-36-37-38-41-42-43-44-46-47-48-52-53-54-58-61-63-YYYYYYYYYYYYYYYYYYYYYYYY45>' + conjunciones + 'Y'
conjunciones = '1-6-10-14-19-22-28-30-32-37-38-39-41-42-43-44-45-47-48-53-54-55-60-62-64-YYYYYYYYYYYYYYYYYYYY46>' + conjunciones + 'Y'
conjunciones = '2-7-11-15-20-23-29-31-38-39-40-41-42-43-44-45-46-48-54-55-56-61-63-YYYYYYYYYYYYYYYYYYYYYY47>' + conjunciones + 'Y'
conjunciones = '3-8-12-16-21-24-30-32-39-40-41-42-43-44-45-46-47-55-56-62-64-YYYYYYYYYYYYYYYYYYYY48>' + conjunciones + 'Y'

conjunciones = '1-7-9-14-17-21-25-28-33-35-41-42-50-51-52-53-54-55-56-57-58-YYYYYYYYYYYYYYYYYYYY49>' + conjunciones + 'Y'#49
conjunciones = '2-8-10-15-18-22-26-29-24-36-41-42-43-49-51-52-53-54-55-56-57-58-59-YYYYYYYYYYYYYYYYYYYYYY50>' + conjunciones + 'Y'
conjunciones = '3-11-16-19-23-27-30-33-35-37-42-43-44-49-50-52-53-54-55-56-58-59-60-YYYYYYYYYYYYYYYYYYYYYY51>' + conjunciones + 'Y'
conjunciones = '4-12-20-24-25-28-31-34-36-38-43-44-45-49-50-51-53-54-55-56-59-60-61-YYYYYYYYYYYYYYYYYYYYYY52>' + conjunciones + 'Y'
conjunciones = '5-13-17-21-26-29-32-35-37-39-44-45-46-49-50-51-52-54-55-56-60-61-62-YYYYYYYYYYYYYYYYYYYYYY53>' + conjunciones + 'Y'
conjunciones = '6-9-14-18-22-27-30-36-38-40-45-46-47-49-50-51-52-53-55-56-61-62-63-YYYYYYYYYYYYYYYYYYYYYY54>' + conjunciones + 'Y'
conjunciones = '1-7-10-15-19-23-28-31-37-39-46-47-48-49-50-51-52-53-54-56-62-63-64-YYYYYYYYYYYYYYYYYYYYYY55>' + conjunciones + 'Y'
conjunciones = '2-8-11-16-20-24-29-32-30-40-47-48-49-50-51-52-53-54-55-63-64-YYYYYYYYYYYYYYYYYYYY56>' + conjunciones + 'Y'

conjunciones = '1-8-9-15-17-22-25-29-33-36-41-43-49-50-58-59-60-61-62-63-64-YYYYYYYYYYYYYYYYYYYY57>' + conjunciones + 'Y'#57
conjunciones = '2-10-16-18-23-26-30-34-37-42-44-49-50-51-57-59-60-61-62-63-64-YYYYYYYYYYYYYYYYYYYYY58>' + conjunciones + 'Y'
conjunciones = '3-11-19-24-27-31-35-38-41-43-45-50-51-52-57-58-60-61-62-63-64-YYYYYYYYYYYYYYYYYYYYY59>' + conjunciones + 'Y'
conjunciones = '4-12-20-28-32-33-36-39-42-44-46-51-52-53-57-58-59-61-62-63-64-YYYYYYYYYYYYYYYYYYYYY60>' + conjunciones + 'Y'
conjunciones = '5-13-21-25-29-34-37-40-43-45-47-52-53-54-57-58-59-60-62-63-64-YYYYYYYYYYYYYYYYYYYYY61>' + conjunciones + 'Y'
conjunciones = '6-14-17-22-26-30-35-38-44-46-48-53-54-55-57-58-59-60-61-63-64-YYYYYYYYYYYYYYYYYYYYY62>' + conjunciones + 'Y'
conjunciones = '7-9-15-18-23-27-31-36-39-45-47-54-55-56-57-58-59-60-61-62-64-YYYYYYYYYYYYYYYYYYYY63>' + conjunciones + 'Y'
conjunciones = '1-8-10-16-19-24-28-32-37-40-46-48-55-56-57-58-59-60-61-62-63-YYYYYYYYYYYYYYYYYYYY64>' + conjunciones + 'Y'

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
