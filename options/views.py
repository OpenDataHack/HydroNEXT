from django.http import HttpResponse
from .models import Localizacion
from .models import Coordenadas
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response

from .models import Option
from .models import Localizacion
from .models import Coordenadas
from . import readExcel
from . import DataparametersClasss
from . import ECMWF_dataRecover01

import math
import json
import urllib.request, urllib.parse, urllib.error
import re

class GoogleCoords():
    def __init__(self, lat, lon, ds):
        self.lat = lat
        self.lon = lon
        self.ds = ds

    def __str__(self):
        return self.ds
		
##Función BuscarCoordenadas -------------------
def BuscarCoordenadas(direccion):
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
    # serviceurl = 'http://python-data.dr-chuck.net/geojson?'
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': direccion})
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url) 
    data = (uh.read().decode(uh.info().get_param('charset') or 'utf-8'))
    print ('Retrieved',len(data),'characters from GoogleMaps')
    try: js = json.loads(str(data))
    except: js = None
    print("js: ",js)
    if ('status' not in js) or (js['status'] != 'OK'):
        print ('==== Failure To Retrieve ====')
        print (data)
    print (json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    formatted_address = js["results"][0]["formatted_address"]
    print ('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print (location)
    place_id = js['results'][0]['place_id']
    print (place_id)
    return(GoogleCoords(lat,lng,formatted_address))
# Create your views here.
def index(request):
    location=0
    if request.method == 'POST':
       existsLocalization = Localizacion.objects.filter(lugar_id = request.POST['lugar'] )
       if existsLocalization.count()==0:
         location= Localizacion.objects.create(lugar_id=request.POST['lugar']  , lugar_ds=request.POST['lugar']  )
         localizacion_id=location.id
         if location!=0:
            coordenadas = BuscarCoordenadas(location.lugar_ds)
            try:
                  coordenadasl = Coordenadas.objects.filter(local_ref = location.id)
                  coordenadasl.delete()
            except:
                  pass
            location.coordenadas_set.create(latitud=coordenadas.lat, longitud=coordenadas.lon, descripcion=coordenadas.ds)
            opcion= Option.objects.create(option_code=location.id ,option_type="lugares", option_text=coordenadas.ds )

    opcionesTemperatura = Option.objects.filter(option_type = "temperaturas")
    opcionesEcoRiverFlow = Option.objects.filter(option_type = "ecological river flow")
    opcionesMaximumFlow = Option.objects.filter(option_type = "Maximun flow")
    opcionesReservoirCapacity = Option.objects.filter(option_type = "Reservoir capacity")
    opcionesLugares = Option.objects.filter(option_type = "lugares")
    opcionesNetFalling = Option.objects.filter(option_type = "net falling height or head")
    opcionesNumberOfTurbines = Option.objects.filter(option_type = "Number of turbines")
    opcionesTypeOfTurbine = Option.objects.filter(option_type = "Type of turbines")
    anios = Option.objects.filter(option_type = "year")
    context = {
	   'opcionesTemperatura': opcionesTemperatura,
	   'opcionesEcoRiverFlow': opcionesEcoRiverFlow,
	   'opcionesMaximumFlow': opcionesMaximumFlow,
	   'opcionesReservoirCapacity': opcionesReservoirCapacity,
	   'opcionesNetFalling': opcionesNetFalling,
	   'opcionesNumberOfTurbines': opcionesNumberOfTurbines,
	   'opcionesTypeOfTurbine': opcionesTypeOfTurbine,
	   'opcionesLugares': opcionesLugares,
	   'anios': anios,
    }
    return render(request, 'options/index.html', context)


def mapa(request):
    type=""
    if '_caudal' in request.POST:
     type="_caudal"
    if '_energia' in request.POST:
     type="_energia"
    if '_periodos' in request.POST:
     type="_periodos"
    if '_forecast' in request.POST:
     type="_forecast"
    if type=="_forecast":
        return(ECMWF_dataRecover01.calculaCaudal(request))

    elif 'localizacion_id' in request.POST:
        localizacion_id=request.POST['localizacion_id']
        opcionesEcoRiverFlow=request.POST['opcionesEcoRiverFlow']
        opcionesMaximumFlow=request.POST['opcionesMaximumFlow']
        opcionesReservoirCapacity=request.POST['opcionesReservoirCapacity']
        opcionesNetFalling=request.POST['opcionesNetFalling']
        opcionesNumberOfTurbines=request.POST['opcionesNumberOfTurbines']
        opcionesTypeOfTurbine=request.POST['opcionesTypeOfTurbine']
        location = get_object_or_404(Localizacion, pk=localizacion_id)
        try:
            coordenadas = Coordenadas.objects.filter(local_ref = location.id)
            if type=="_caudal":
                return(readExcel.calculaCaudal(request, coordenadas[0].latitud, coordenadas[0].longitud,coordenadas[0].descripcion))
            if type=="_energia":
                dataparameters =DataparametersClasss.DataparametersClasss ()

                dataparameters.opcionesEcoRiverFlow=opcionesEcoRiverFlow
                dataparameters.opcionesMaximumFlow=opcionesMaximumFlow
                dataparameters.opcionesReservoirCapacity=opcionesReservoirCapacity
                dataparameters.opcionesNetFalling=opcionesNetFalling
                dataparameters.opcionesNumberOfTurbines=opcionesNumberOfTurbines
                dataparameters.opcionesTypeOfTurbine=opcionesTypeOfTurbine
                return(readExcel.calculaEnergia(request, coordenadas[0].latitud, coordenadas[0].longitud,coordenadas[0].descripcion,dataparameters))
            if type=="_periodos":
                dataparameters =DataparametersClasss.DataparametersClasss ()

                dataparameters.opcionesEcoRiverFlow=opcionesEcoRiverFlow
                dataparameters.opcionesMaximumFlow=opcionesMaximumFlow
                dataparameters.opcionesReservoirCapacity=opcionesReservoirCapacity
                dataparameters.opcionesNetFalling=opcionesNetFalling
                dataparameters.opcionesNumberOfTurbines=opcionesNumberOfTurbines
                dataparameters.opcionesTypeOfTurbine=opcionesTypeOfTurbine
                return(readExcel.calculaPeriodo(request, coordenadas[0].latitud, coordenadas[0].longitud,coordenadas[0].descripcion,dataparameters))
        except:
            print("****errir**")


