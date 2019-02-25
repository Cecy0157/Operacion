clase  operacion :
    __numerouno =  flotar ( 0 )
    __numerodos=  flotador ( 0 )
    __division=  flotar ( 0 )


while numerodos==0:
	print 'No se puede dividir por 0. Inserte otro numero mayor que 0:'
	numerodos=int(input())
division=(numerouno/numerodos)
modulo=(numerouno%numerodos)
if modulo==0:
	print'La division es exacta. El resultado es : cociente= %s' % str(division)
else:
	print 'La division no es exacta. El resultado es : cociente= %s y el resto= %s' % (str(division),str(modulo))