# -*- coding: utf8 -*-
from xlrd import open_workbook, xldate
import urllib.request
from . import FlowToEnergy
from . import LongListToPeriod
''' La funcion callForData(longitud,latitud)

devuelve para la longitud y latitud un diccionario llamado modelo donde
modelo["dates"] contiene una lista de fechas
modelo[nombreModeloDelExcel] contiene la lista de valores para esas fechas (si existen)

'''
from . import DataparametersClasss

def data(dls):
	##	wb = open_workbook('C:/Users/sera/Documents/python34/ccclimate/options/River flow (Catchments).xlsx')
	##dls ="http://swicca.smhi.se/swicca/catchment/daily/flow?lat=42.1435546875&lon=13.3154296875"
	data = urllib.request.urlretrieve(dls, "River flow (Catchments).xlsx")
	##wb = open_workbook('C:/Users/sera/Documents/python34/ccclimate/options/River flow (Catchments).xlsx')
	wb = open_workbook("River flow (Catchments).xlsx")
	sheet=wb.sheet_by_index(1)

	number_of_rows = sheet.nrows
	number_of_columns = sheet.ncols

	modelos = {}

	values = []

	name="dates"
	for row in range(1, number_of_rows):
		value  = (sheet.cell(row,0).value)
		try:
			value = xldate.xldate_as_datetime(value, wb.datemode)
			value= value.strftime("%Y-%m-%d")

		except ValueError:
			pass
		finally:
			values.append(value)
	modelos[name]=values

	for col in range(1, number_of_columns):
		values = []
		name=sheet.cell(0,col).value
		for row in range(1,number_of_rows):
			value  = (sheet.cell(row,col).value)
			try:
				value = (float(value))
			except ValueError:
				pass
			finally:
				values.append(value)
		modelos[name]=values

	##for modelo in modelos:
	##   print (modelo+" "+ "[	" + ", ".join( str(x) for x in modelos[modelo]) + "]")

	return (modelos)
def callForData(longitud,latitud):
	##latitud="42.1435546875"
	##longitud="13.3154296875"
	dls ="http://swicca.smhi.se/swicca/catchment/daily/flow?lat="+str(latitud)+"&lon="+str(longitud)
	print(dls)
	return(data(dls))

##callForData("42.1435546875","13.3154296875")
from django.http import HttpResponse
from django.shortcuts import render

def calculaCaudal(request,longitud, latitud, lugar):
	print(" latituod y longitud %f %f", latitud,longitud)
	modelos=callForData(latitud,longitud)
	valores95pr = []
	namemodeloslist=[]
	namemodelos=[]
	anios = []
	modelos.pop('SMHI_RCA4_HadGEM2-ES_rcp45', None)
	modelos.pop('SMHI_RCA4_HadGEM2-ES_rcp85', None)
	for modelo in modelos:
	   if modelo=="dates":
	      continue
	   namemodeloslist.append(modelo.replace("&#39;",""))
	   valores95pr.append(modelos[modelo][0:10])
	anios.append(modelos["dates"])
	
	return render(request, 'options/mapa.html', {'namemodelos':namemodeloslist,'valores':valores95pr, 'anios':anios, 'lugar':lugar,'variable':""})

def calculaEnergia(request,longitud, latitud, lugar,dataparameters):
	print(dataparameters)

	print(" latituod y longitud %f %f", latitud,longitud)
	modelos=callForData(latitud,longitud)
	valores95pr = []
	namemodeloslist=[]
	namemodelos=[]
	anios = []
	modelos.pop('SMHI_RCA4_HadGEM2-ES_rcp45', None)
	modelos.pop('SMHI_RCA4_HadGEM2-ES_rcp85', None)
	for modelo in modelos:
	   if modelo=="dates":
	      continue
	   namemodeloslist.append(modelo.replace("&#39;",""))
	   energyResult=FlowToEnergy.obtainEnergyList(modelos[modelo][0:60],dataparameters)
	   print(energyResult)
	   valores95pr.append(energyResult)
	anios.append(modelos["dates"])
	return render(request, 'options/mapa.html', {'namemodelos':namemodeloslist,'valores':valores95pr, 'anios':anios, 'lugar':lugar,'dataparametersSt':dataparameters})

def calculaPeriodo(request,longitud, latitud, lugar,dataparameters):
	print(dataparameters)

	print(" latituod y longitud %f %f", latitud,longitud)
	modelos=callForData(latitud,longitud)
	valores95pr = []
	namemodeloslist=[]
	namemodelos=[]
    
	lista=[1,2,3,4] 
	anios = []
	modelos.pop('SMHI_RCA4_HadGEM2-ES_rcp45', None)
	modelos.pop('SMHI_RCA4_HadGEM2-ES_rcp85', None)

	
	for modelo in modelos:
	   if modelo=="dates":
	      continue
	   namemodeloslist.append(modelo.replace("&#39;",""))
	   energyResult=FlowToEnergy.obtainEnergyList(modelos[modelo][0:len(modelos[modelo])],dataparameters)
	   print(modelo)
	   periodoResult=LongListToPeriod.GenerarValoresPromedios(energyResult)
	   valores95pr.append(periodoResult)
	anios.append(lista)
	namemodelos.append(namemodeloslist)
	return render(request, 'options/mapaResumen.html', {'namemodelos':namemodeloslist,'valores':valores95pr, 'anios':anios, 'lugar':lugar,'dataparametersSt':dataparameters})
