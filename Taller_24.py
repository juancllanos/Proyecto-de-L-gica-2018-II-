print "Funcion que pasa de una formula como cadena a un objeto Tree\n\
Recuerde que la formula debe estar escrita en notacion polaca invertida\n \
Las unicas letras proposicionales permitidas son p, q, r, s, t, v\n \
Claves de escritura para los conectivos:\n \
La negacion se escribe -\n \
La Or se escribe O\n \
El AND se escribe Y\n \
La implicacion se escribe >"

# Definimos la clase de objetos Tree para las formulas
class Tree(object):
    def __init__(self,l,iz,der):
        self.left = iz
        self.right = der
        self.label = l

# Define la funcion de imprimir rotulos Inorder(f)
def Inorder(f):
    # Determina si F es una hoja
    if f.right == None:
#        print "Es una hoja!"
        print f.label,
    elif f.label == '-':
        print f.label,
        Inorder(f.right)
    else:
        print "(",
        Inorder(f.left)
        print f.label,
        Inorder(f.right)
        print ")",

# Solicitamos una cadena
#f = raw_input('Ingrese una cadena: ') or 'rqpO>' # Cadena por defecto

#print "Cadena ingresada " + f

#cadena = list(f)

#print cadena

letrasProposicionales = ['p', 'q', 'r', 's', 't', 'v']
conectivos = ['O', 'Y', '>']

pila = [] # inicializamos la pila

#for c in cadena:
#    if c in letrasProposicionales:
#        pila.append(Tree(c, None, None))
#    elif c == '-':
#        aux = Tree(c, None, pila[-1])
#        del pila[-1]
#        pila.append(aux)
#    elif c in conectivos:
#        aux = Tree(c, pila[-1], pila[-2])
#        del pila[-1]
#        del pila[-1]
#        pila.append(aux)

#formula = pila[-1]

#print "La formula ",
#Inorder(formula)
#print " fue creada como un objeto!"

#EJERCICIO 4:
letProp = ['p','q','r']
interps = [] # Creamos la lsita de las posibles interpretaciones
aux = {}     # Creamos la primera intrepretacion

for i in letrasProposicionales:   
	aux[i] = 1         #1era interpretacion, verdadera para toda letra
interps.append(aux)

for i in letProp:
    interps_aux = {for x in interps}   #Esta lista nos ayuda a saber las interpretraciones que se llevan
    for j in interps_aux:
        aux1 = {}                      #Se crea un diccionario auxiliar
        for k in letProp:
            if i == k:                 #Se comparan las letras para cambiarles su valor de verdad
                aux1[b] = 1-j[b]       #Si son iguales se les cambia el valor en el diccionario auxiliar
            else:                      #Si no entonces se deja el mismo valor de verdad
                aux1[b] = i[b]
            


print "Interpretaciones :"
for i in interps:
	print i


