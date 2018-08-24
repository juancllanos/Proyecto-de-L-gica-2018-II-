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
f = raw_input('Ingrese una cadena: ') or 'rqpO>' # Cadena por defecto

print "Cadena ingresada " + f

cadena = list(f)

print cadena

letrasProposicionales = ['p', 'q', 'r', 's', 't', 'v']
conectivos = ['O', 'Y', '>']

pila = [] # inicializamos la pila

for c in cadena:
    if c in letrasProposicionales:
        pila.append(Tree(c, None, None))
    elif c == '-':
        aux = Tree(c, None, pila[-1])
        del pila[-1]
        pila.append(aux)
    elif c in conectivos:
        aux = Tree(c, pila[-1], pila[-2])
        del pila[-1]
        del pila[-1]
        pila.append(aux)

formula = pila[-1]

print "La formula ",
Inorder(formula)
print " fue creada como un objeto!"

#EJERCICIO 4:
letProp = ['p','q','r']
interps = [] # Creamos la lsita de las posibles interpretaciones
aux = {}     # Creamos la primera intrepretacion

for i in letrasProposicionales:   
	aux[i] = 1
interps.append(aux) 
# En este primer for inicializamos aux como verdadera para toda letra proposicional
for i in letrasProposicionales:
	interps_aux = [j for j in interps]
# Esta lista nos ayuda a tener las interpretaciones que llevemos
	for i in interps_aux:
		aux1 = {}
		for j in range(len(letProp)):
			for b in letProp:
				if letProp[i] == letProp[b]:
					aux1[b] == 1-i[j][b]
# En este paso si estamos comparando letras proposicionales iguales les cambiamos la interpretacion
				else:
					aux1[b] = i[j][b]
# Si no entonces se deja igual la interpretacion
		interps.append(aux1)
# Por ultimo se agrega a la lista de interpretaciones

print "Interpretaciones :"
for i in interps:
	print i


