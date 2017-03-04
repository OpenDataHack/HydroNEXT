import numpy

#CAUTION: this includes 29th february every 4 years

#Reference period: 1971-01-01 to 2000-12-31  ->10958 days -> from 0 (included) to 10958 (not included)
#An empty period from 2001-01-01 to 2010-12-31 ->3652 days
#Future periods: 
#2011-01-01 to 2040-12-31 ->10958 days -> from 14610 (included) to 25568 (not included)
#2041-01-01 to 2070-12-31 ->10957 days -> from 25568 (included) to 36525 (not included)
#2071-01-01 to 2100-12-31 ->10957 days -> from 36525(included) to 47482 (not included)






##Generation of trial list
listaEjemplo=[]
for i in range(10958):
    listaEjemplo.append(1)
for i in range(3652):
    listaEjemplo.append(9)
for i in range(10958):
    listaEjemplo.append(1.2)
for i in range(10957):
    listaEjemplo.append(1.4)
for i in range(10957):
    listaEjemplo.append(1.6)
#print(listaLarga)

def Promedio(plist):
    lista = numpy.array(plist)
    try:
       if len(plist)>0:
           return numpy.mean(lista)
       return 0
    except:	 
      pass	

def GenerarValoresPromedios(listaLarga):
    listaValoresDePromedios=[]    
        
    listaPeriodoInicial=listaLarga[0:10958]
    #print(listaPeriodoInicial)
    mediaPeriodoInicial=Promedio(listaPeriodoInicial)
    #print(mediaPeriodoInicial)
    listaValoresDePromedios.append(mediaPeriodoInicial)

    listaPeriodoFuturo1=listaLarga[14610:25568]
    #print(listaPeriodoFuturo1)
    mediaPeriodoFuturo1=Promedio(listaPeriodoFuturo1)
    #print(mediaPeriodoFuturo1)
    listaValoresDePromedios.append(mediaPeriodoFuturo1)

    listaPeriodoFuturo2=listaLarga[25568:36525]
    #print(listaPeriodoFuturo2)
    mediaPeriodoFuturo2=Promedio(listaPeriodoFuturo2)
    #print(mediaPeriodoFuturo2)
    listaValoresDePromedios.append(mediaPeriodoFuturo2)
	
    listaPeriodoFuturo3=listaLarga[36525:47482]
    #print(listaPeriodoFuturo3)
    mediaPeriodoFuturo3=Promedio(listaPeriodoFuturo3)
    #print(mediaPeriodoFuturo3)
    listaValoresDePromedios.append(mediaPeriodoFuturo3)

    print(listaValoresDePromedios)
    listaValoresDePromediosNormalizada=[]
    for i in range(4):
        valorNormalizado=listaValoresDePromedios[i]/listaValoresDePromedios[0]*100
        listaValoresDePromediosNormalizada.append(valorNormalizado)
    return(listaValoresDePromediosNormalizada)

