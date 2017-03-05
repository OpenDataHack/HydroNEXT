import numpy as np
import requests
from django.shortcuts import render
from . import generateListOfDates
#for retrieving the step time number 3 (the second day before 2008-04-08)
#url = 'http://earthserver.ecmwf.int/rasdaman/ows?service=WCS&version=2.0.11&request=ProcessCoverages&query=for c in (river_discharge_forecast_opt2) return encode (c[ansi("2008-04-08T00:00"),Lat(41.32),Long(-89.0),forecast(2)],"csv")'

def obtainValues():
    url = 'http://earthserver.ecmwf.int/rasdaman/ows?service=WCS&version=2.0.11&request=ProcessCoverages&query=for c in (river_discharge_forecast_opt2) return encode (c[ansi("2008-04-08T00:00"),Lat(41.32),Long(-89.0)],"csv")'

    print(" hardcoded value for url "+ url)
    r = requests.get(url,
                    proxies={'http':None}
                    )
    r.raise_for_status()
    x = np.array(eval(r.text.replace('{','[').replace('}',']')))

    listOfMedian=[]

    for i in range(30):
        listOfEnsambles=x[i]
       ## print(listOfEnsambles)
        listOfEnsambles_masked = np.ma.masked_where(listOfEnsambles == 0, listOfEnsambles)
       ## print(listOfEnsambles_masked)
        medianValue=np.nanmedian(listOfEnsambles_masked)
       ## print(medianValue)
        listOfMedian.append(medianValue)

    return(listOfMedian)    
    
def calculaCaudal(request):
    caudales= obtainValues()
    valores95pr = []
    anios = []
    for idx, caudal in enumerate(caudales):
       anios.append(idx)
       valores95pr.append(caudal)

    return render(request, 'options/forecastflow.html', {'valores':valores95pr, 'anios':generateListOfDates.ListOf30DaysAhead()})
