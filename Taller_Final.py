class Tree(object):
    def __init__(self,l,iz,der):
        self.left = iz
        self.right = der
        self.label = l

def top():
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
	return formula

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


def VI(f):
    if f.right == None:
        return i[f.label]
    elif f.label == '~':
        if VI(f.right) == 1:
            return 0
        else:
            return 1
    elif f.label == 'Y':
        if (VI(f.left) == 1 and VI(f.right) == 1):
            return 1
        else:
            return 0

    elif f.label == 'O':
        if (VI(f.left) == 1 or VI(f.right) == 1):
            return 1
        else:
            return 0
    elif f.label == '>':
        if (VI(f.left) == 0 or VI(f.right) == 1):
            return 1
        else:
            return 0
    elif f.label == '<->':
        if(VI(f.left) == VI(f.right)):
            return 1
        else:
            return 0
#----------------------------------------------------------------------------------------------------
Proposicionales = ['p', 'q', 'r']
pila0 = []
aux ={}

for a in Proposicionales:
    aux[a] = 1

pila0.append(aux)

for a in Proposicionales:
    pila0_aux =  [i for i in pila0]

    for i in pila0_aux:
        aux1 = {}

        for b in Proposicionales:
            if a == b:
                aux1[b] = 1 - i[b]
            else:
                aux1[b] = i[b]

        pila0.append(aux1)

#--------------------------------Ejecucion----------------------------------------
pila2 = []
pila3 = []
formula1 = top()
formula2 = top()

print 'Interpretaciones: '
for i in pila0:
    print i

for i in pila0:
	pila2.append(VI(formula1))


for i in pila0:
	pila3.append(VI(formula2))
#-----------------------Evaluacion-------------------------------------------
Condicional = True

for i in pila2:
	if pila2[i] == pila3[i]:
		i = i + 1
		Condicional = True
	else:
		print "Las formulas NO son equivalentes"
		Condicional = False
		break

if(Condicional == True):
	print "Las formulas son equivalentes"
#----------------FIN--------------------------------
