class Tree(object):
    def __init__(self,l,iz,der):
        self.left = iz
        self.right = der
        self.label = l

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

#Pedir un valor de verdad
def I(cadena):
	letrasProposicionales = ['p', 'q', 'r', 's', 't', 'u']
	conectivos = ['O', 'Y', '>','<>']

	for c in cadena:
		if c in letrasProposicionales:
			j = raw_input('Ingrese un valor de verdad: ' )
			pila2.append(Tree(None,c,c))
	for c in cadena:	
		if c in conectivos:	
			pila2.append(Tree(c,None,None))

	formula2 = pila2[-1]
	return formula2

def V1(f):
	
	if f.right==None:
		return I(f.label)
	elif f.label== '-':
		if V1(f.right)== "V":
			return "F"
		else:
			return "V"
	elif f.label=='&':
		if(V1(f.left)=="V" and V1(f.right)=="V"):
			return "V"
		else:
			return "F"
	elif f.label == "v" :
		if (V1(f.left)=="V" or V1(f.right)=="V"):
			return "V"
		else:
			return "F"
	elif f.label == "->":
		if (V1(f.left)=="F" or V1(f.right)=="V"):
			return "V"
		else:
			return "F"
	elif f.label == "<->":
		if (V1(f.left) == V1(f.right)):
			return "V"
		else:
			return "F"
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
letrasProposicionales = ['p', 'q', 'r', 's', 't', 'u']
conectivos = ['O', 'Y', '>','<>']
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
f = raw_input('Ingrese una cadena: ') or 'rqpO->' # Cadena por defecto

print "Cadena ingresada " + f

cadena = list(f)


pila = []
pila2 = []

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
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I(cadena)
V1(I(cadena))

