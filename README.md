# HidroNext: A web application for assisting hydroelectric sector in acquiring and using climate information in decision making processes.  


## Team name & members
HidroNext Team:

- Olga María Serrano Ramos
- Jorge Paz Jimenez

## Description
Hydroelectricity is the most important renewable source in Europe (and worldwide) but, currently climate services for this activity are focusing on wind, solar, etc.   (at least in the R&D programs as Copernicus, H2020,etc.). This sector is currently using climate records for decision making processes as planning of maintenance, evaluation of investment operations, design of the plants (power, etc.), planning of the sector, etc. They are not using seasonal forecasts and long term climate change projections (valuable for this long live assets). The main reason for that it this sector requires river flow as the most important Essential climate Variable, and this variable should be generated with hydrological models, that requires a lot of information (land uses, digital elevation model, etc.) However, two projects are providing this information (in demo mode). SWICCA (Service for Water Indicators in Climate Change Adaptation) offers readily available climate-impact data to speed up the workflow in climate-change adaptation of water management across Europe. ECMWF Web Coverage Service (WCS) is delivering 30 day projections. HydroNext will run in a free web portal. It will allow users to enter the location of the plant they wish to study and some basic parameters (power, reservoir capacity, etc.). Combining this information with river flow data adquired online  from SWICCA and WCS it will generate the next information: 

-	River flow  series for the entire 21st century considering the ouputs of different models and RCPs from SWICCA
-	Energy generation for the entire 21st century computed 
-	Energy generation evolution in four periods
-	River flow evolution for the next 30 days 
-	Energy generation for the next 30 days
Currently, an demand of studies about climate information is emerging but in other parts of the globe (SouthAmerica, etc.) These studies are funded by public institutions, and don´t offer an interactive layer. 

HydroNext will boost the demand of climate information in Europa, focusing on private sector and actors that don´t make use of climate change projections and seasonal forecast. 

The business model will be FREEMIUM. A free web portal will allow to generate the consultations indicated previously. Premium services will include computation of hydro cascade systems , study of the sediments, etc. 

The portal is running. It has been developed using Dwango. Visualizations make use of C3.js. All data from SWICCA and WCS are adquired trhougth web services. Algorithms for computing energy generation and other indicators are python functions.

Everything is in https://github.com/OpenDataHack/HydroNEXT



## Lessons learnt
What have you accomplished during the OpenDataHack? 
-	Development of a running web application can be achieved in a weekend!!!!
-	Access to SWICCA and WCS is complicated to integrate into applications, but can be automated, and in a reasonable time this data will be available through the Copernicus Climate Data Store (SWICCA) and will include additional information (WCS).
What would you do differently if you had to start all over again?
-	User experience could be improved. Templates, forms, etc. should came ready to the next Hackathom

## Future developments
-	As soon as the data from SWICCA is available through the Copernicus Climate Data Store (SWICCA) our application has to point there.
-	WCS under development.
-	Presentations could be improved as well: maps, new graphs, 
-	Downloadable data can be provided to users (txt files, etc.)
