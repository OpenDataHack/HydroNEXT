class DataparametersClasss:
    opcionesEcoRiverFlow=5.0
    opcionesMaximumFlow=5.0
    opcionesReservoirCapacity=10.0
    opcionesNetFalling=201.51
    opcionesNumberOfTurbines=2.0
    opcionesTypeOfTurbine="Pelton"
    def __str__(self):
       return ("Ecological River Flow: "+str(self.opcionesEcoRiverFlow)+"\n"+ "Maximum Flow: "+str(self.opcionesMaximumFlow)+"\n"+"Reservoir Capacity: "+str(self.opcionesReservoirCapacity)+"\n"+ "Net Falling: "+str(self.opcionesNetFalling)+"\n"+ "Number Of Turbines: "+str(self.opcionesNumberOfTurbines)+"\n"+ "Type Of Turbine: "+self.opcionesTypeOfTurbine)