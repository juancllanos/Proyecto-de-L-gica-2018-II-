# -*- coding: utf-8 -*-
def complemento(l):
	if '-' in l:
		return l[1:]
	else:
		return '-' + l

def RE(S,I,p):
        #print "RE"
        #print "|",S,"|",I
        q = []
        if '-' in p:
                I[p.replace('-','')]= "F"
        else:
                I[p] = "V"
        #Aca vemos si la letra es una negacion o no y agregamos su interpretacion como verdadera
                
        #print " Letra = ",p
        for i in S:
                for j in i:
                        if j == complemento(p):
         #                       print "Complemento de letra :",complemento(p)
                                a = list(i)
                                a.remove(j)
                                q.append(a)
                                
                                #Revisamos si  el complemento de la letra proposicional
                                #esta en la clausula, si esta entonces removemos ese elemento
                                # de la clausula y se lo agregamos a la lista q.
                                
                if not(p in i) and not(complemento(p) in i):
          #              print " Ni letra ni complemento"
                        q.append(i)
                        #Si no esta ni la letra ni su complemento entonces agregamos la clausula completa
        #S  = q
        #print "Retorno : ", q,I
        #print "S : ", S
        #print "FIN RE"
        #print "----------------------------------------------------------------------------"
        
        # Aqui retornamos la lista y la interpretacion dada la letra proposicional p

        return q,I
              
def DPLL1(S,I):
        #print "DPLL"
        #print "INICIO ",S,"|",I
        if len(S) == 0:
                #print "Conjunto vacio"
                #print "S :",S
                #print "RETORNA ",True,"Satisfacible",I

                #Aca se revisa si el tamaño de la lista que ingresamos es 0, eso quiere
                #decir por definicion que es satisfacible
                return True,"Satisfacible",I
        
        elif [] in S:
                #print "[] en conjunto"
                #print "S: ",S
                #print "RETORNA ",False,"Insatisfacible",[]

                #Aca se revisa si la clausula vacia esta en el conjunto de las clausulas
                return False,"Insatisfacible",[]
        
        else:

                #print "Buscando I :"
                #print "S :",S
                if len(S[0][0]) == 0:
                        c = S[1][0]
                else :
                        c = S[0][0]
                #Se mira si el primer elemento es vacio, si es vacio
                # entonces se toma el siguiente, no se necesita recorrer la lista
                # ya que si la clausula vacia esta de primera o de segunda en la
                # siguiente recursion se mira eso y retorna el paso anterior.
                I1 = dict(I)
                I2 = dict(I)
                #Creamos copias del diccionario para no modificarlo
                a = RE(S,I1,c)
                b = RE(S,I2,complemento(c))
                #Utilizamos la funcion RE que funciona como un UnitPropagate solo que
                #para clausulas que no son unitarias tambien
                if (DPLL1(a[0],a[1])[0] or DPLL1(b[0],b[1])[0]):
                        #Revisamos si el primer elemento que retorna la funcion en p
                        # es verdadero o si la funcion con p complemento es verdadero
                        if DPLL1(a[0],a[1])[0] == True:
                                return DPLL1(a[0],a[1])
                        elif DPLL1(b[0],b[1])[0] == True:
                                #print "Esta en B"
                                #print "FIN DPLL"
                                return DPLL1(b[0],b[1])
                        #Aca revisamos de donde salio, si de la letra o de su complemento y esto
                        # es lo que retorna
                else:
                        return False,"Insatisfacible",[]
                #Si ninguna hoja da verdadero entonces se retorna que es insatisfacible
                
def DPLL(S,I):
        print "S :", S
        a = DPLL1(S,I)
        return a[1],a[2]

        #Esta funcion llama a DPLL1 que es la que hace todo el proceso y luego
        # solo retornamos la lista y la interpretacion, es decir quitamos el valor
        # booleano de la funcion DPLL1

              
S1 = []
S2 = [['-p','-q'],['p','q'],['-p','q']]
S3 = [['p','q'],['-p','q'],['-q','-r'],['r','-q']]
S4 = [['p','q','r'],['-p','-q','-r'],['-p','q','r'],['-q','r'],['q','-r']]
S5 =  [['p','-q'],['-p','-q'],['q','r'],['-q','-r'],['-p','-r'],['p','-r']]
S6 = [['-p'],['q']]
S7 = [['-q', '-p'], ['q', 'p'], ['q', '-p']]
I = {}

print DPLL(S7,I)

"""
print"---------------------------------------------------------------"
print DPLL(S1,I)
print"---------------------------------------------------------------"
print DPLL(S2,I)
print"---------------------------------------------------------------"
print DPLL(S3,I)
print"---------------------------------------------------------------"
print DPLL(S4,I)
print"---------------------------------------------------------------"
print DPLL(S5,I)
print"---------------------------------------------------------------"
print DPLL(S6,I)
print"---------------------------------------------------------------"

"""

        





            
            

        
        
                        
        
            

                
                
















"""
def stringToList(a):
    v = []
    cont = 0
    while(cont != len(a)):
        print cont
        if (a[cont] == "-"):
            c = a[cont]+a[cont+1]
            print 'c = ',c
            v.append(c)
            cont = cont +2
        else:
            v.append(a[cont])
            cont = cont +1
    return v

s = "pqrs-p-q-r-s-q-q"
print stringToList(s)
"""




            
            
            










        
            
        
        

