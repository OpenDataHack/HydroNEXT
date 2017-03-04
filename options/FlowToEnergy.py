from . import DataparametersClasss

##Parametros definidos por usuario
caudalEcologico=5.0
caudalMaximoTurbinable=5.0
capacidadEmbalse=10.0
saltoNeto=201.51
numeroTurbinas=2.0
tipoTurbina="Pelton"

##Variables por defecto
aguaIncialEmbalse=10
eficienciaGeneradorAlternador=0.95*0.99
gravedad=9.81
densidadAgua=1000
peltonEficiency=[0.86,0.86,0.86,0.86,0.86,0.87,0.88,0.85,0.82,0.6,0]
francisHighSpeedEficiency=[0.86,0.9,0.91,0.91,0.85,0.76,0.62,0.44,0.18,0,0]
francisLowSpeedEficiency=[0.9,0.9,0.9,0.9,0.88,0.86,0.8,0.7,0.5,0.1,0]
kaplanEficiency=[0.9,0.9,0.9,0.9,0.89,0.87,0.85,0.82,0.7,0.3,0]
diccionarioEficienciasTurbina={"Pelton":peltonEficiency,"FrancisHighSpeed":francisHighSpeedEficiency,"FrancisLowSpeed":francisLowSpeedEficiency,"Kaplan":kaplanEficiency}
eficienciaTurbina=diccionarioEficienciasTurbina[tipoTurbina]


##lista de caudales a procesar
def obtainEnergyList(listaCaudales,dataparameters):
	##listaCaudales=[10,7,16,7,12,0,6]
	
	
	
	caudalEcologico=float(dataparameters.opcionesEcoRiverFlow)
	caudalMaximoTurbinable=float(dataparameters.opcionesMaximumFlow)
	capacidadEmbalse=float(dataparameters.opcionesReservoirCapacity)
	saltoNeto=float(dataparameters.opcionesNetFalling)
	numeroTurbinas=float(dataparameters.opcionesNumberOfTurbines)
	tipoTurbina=dataparameters.opcionesTypeOfTurbine

	longitudLista=len(listaCaudales)

	caudalAprovechable=aguaEnEmbalseAntesTurbinar=aguaEnEmbalseTrasTurbinar=caudalTurbinado=numeroTurbinasOperando=CaudalTurbinadoPlenaCarga=CaudalTurbinadoCargaParcial=0.0

	listaEnergia=[]

	for i in range(0,longitudLista):
		#Calculos caudales
		##print("---------Iteraccion: ", i)
		##print("Caudal que llega a embalse o central: ",listaCaudales[i])
		caudalAprovechable=listaCaudales[i]-caudalEcologico
		##print("Caudal Aprovechable: ",caudalAprovechable)
		if i==0:
			aguaEnEmbalseAntesTurbinar=aguaIncialEmbalse+caudalAprovechable
		else:
			aguaEnEmbalseAntesTurbinar=aguaEnEmbalseTrasTurbinar+caudalAprovechable
		##print("Agua En Embalse Antes de Turbinar: ",aguaEnEmbalseAntesTurbinar)
		if aguaEnEmbalseAntesTurbinar>caudalMaximoTurbinable:
			caudalTurbinado=caudalMaximoTurbinable
		else:
			caudalTurbinado=aguaEnEmbalseAntesTurbinar
		if caudalTurbinado<0:
			caudalTurbinado=0
		##print ("Caudal Turbinado: ",caudalTurbinado)
		aguaEnEmbalseTrasTurbinar=min(capacidadEmbalse,max(0,(aguaEnEmbalseAntesTurbinar-caudalTurbinado)))
		##print("Agua en embalse tras turbinar: ",aguaEnEmbalseTrasTurbinar)
		##print()    
		#Calculo numero turbinas y caudales en cada una
		numeroTurbinasOperando=caudalTurbinado/(caudalMaximoTurbinable/numeroTurbinas)
		##print("Numero Turbinas Operando: ",numeroTurbinasOperando)
		numeroTurbinasPlenaCarga=float(int(numeroTurbinasOperando))
		##print("numeroTurbinasPlenaCarga: ",numeroTurbinasPlenaCarga)
		numeroTurbinasCargaParcial=float(numeroTurbinasOperando-int(numeroTurbinasOperando))
		##print("numeroTurbinasCargaParcial: ",numeroTurbinasCargaParcial)    
		CaudalTurbinadoPlenaCarga=numeroTurbinasPlenaCarga*(caudalMaximoTurbinable/numeroTurbinas)
		##print("Caudal Turbinado Plena Carga: ",CaudalTurbinadoPlenaCarga)
		CaudalTurbinadoCargaParcial=numeroTurbinasCargaParcial*(caudalMaximoTurbinable/numeroTurbinas)
		##print("Caudal Turbinado Carga Parcial: ",CaudalTurbinadoCargaParcial)
		##print()    
		#Calculo eficiencias
		eficienciaTurbinaPlenaCarga=eficienciaTurbina[0]
		##print(eficienciaTurbinaPlenaCarga)
		intervaloTurbinasCargaParcial=int(10-round(numeroTurbinasCargaParcial/0.1))
		##print(intervaloTurbinasCargaParcial)
		eficienciaTurbinaCargaParcial=eficienciaTurbina[intervaloTurbinasCargaParcial]
		##print(eficienciaTurbinaCargaParcial)
		#Calculo energias
		energiaTurbinasPlenaCarga=numeroTurbinasPlenaCarga*caudalMaximoTurbinable/numeroTurbinas*eficienciaGeneradorAlternador*eficienciaTurbinaPlenaCarga*gravedad*saltoNeto*densidadAgua*24/1000000
		##print("Energia Turbinas Plena Carga",energiaTurbinasPlenaCarga)
		energiaTurbinasCargaParcial=numeroTurbinasCargaParcial*caudalMaximoTurbinable/numeroTurbinas*eficienciaGeneradorAlternador*eficienciaTurbinaCargaParcial*gravedad*saltoNeto*densidadAgua*24/1000000
		##print("Energia Turbinas Carga Parcial",energiaTurbinasCargaParcial)
		energiaTotal=energiaTurbinasPlenaCarga+energiaTurbinasCargaParcial
		##print("Energia TOTAL",energiaTotal)
		##print()
		listaEnergia.append(energiaTotal)
##	print(listaEnergia)
	return(listaEnergia)

