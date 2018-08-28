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

# PUNTO 3

def Vi(A, I):

	if A.right == NULL:
		return I(A.label)
	if A.label == '-':
		if(Vi(A.right)) == 1:
			return 0
		else:
			return 1
	if A.label == 'Y':
		if(Vi(A.left) == 1) and (Vi(A.right) == 1):
			return 1
		else:
			return 0
	if A.label == 'O':
		if(Vi(A.left) == 1) or (Vi(A.right) == 1):
			return 1
		else:
			return 0
	if A.label == '>':
		if(Vi(A.left) == 0) or (Vi(A.right) == 1):
			return 1
		else:
			return 0
	if A.label == '<>':
		if (Vi(A.left)) == (Vi(A.right)):
			return 1
		else:
			return 0

#EJERCICIO 4:

letProp = ['p','q','r'] #Creamos la lista de letras proposicionales
interps = [] # Creamos la lista de todas las interpretaciones posibles 
aux = {}     # Creamos la primera intrepretacion

for i in letProp:   
	aux[i] = 1 # En este primer for inicializamos aux como verdadera para toda letra proposicional
interps.append(aux) #Incluimos esta interpretación en la lista de interpretaciones

for a in letProp:
	
	interps_aux = [j for j in interps] # Esta lista auxiliar contiene las interpretaciones que ya hemos guardado

	for i in interps_aux:
		aux1 = {} #Se crea un diccionario auxiliar que va a guardar la interpretación que se va a crear

		for b in letProp:
			if a== b: #Se comparan las letras para cambiarles su valor de verdad 
				aux1[b] = 1 - i[b]  #Si son iguales, cambia el valor de verdad de la letra en el diccionario auxiliar
			else:
				aux1[b] = i[b] #Si no son, se deja el mismo valor de verdad (se deja el mismo valor de verdad para todas las letras distintas)
		
		interps.append(aux1) #Se incluye esta nueva interpretación en la lista original de interpretaciones

#Así se obtienen todas las interpretaciones posibles

print "Interpretaciones:"
for i in interps:
	print i

# PUNTO 5

def equiv(f1, f2):
	for i in interps:
		if Vi(f1, i) != Vi(f2, i):
			print "las formulas no son equivalentes"
		else:
			print "las formulas son equivalentes"


