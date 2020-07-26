# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:51:59 2020

@author: aortegar
"""

from src.test.UnitTests import UnitTests
from ODFiles import ODFiles as OD

class Main:
    def main():
        od2014 = OD.ODFiles('2014')
        od2015 = OD.ODFiles('2015')
        od2016 = OD.ODFiles('2016')
        od2017 = OD.ODFiles('2017')
        print('##########################################')
        print('##########################################')
        print('##########################################')
        print('##########################################')
        print('############### Report ###############')
        print('######## Histograma de tiempos de viaje para un año dado #######')
        print('Año 2014')
        od2014.hist()
        print('Año 2015')
        od2015.hist()
        print('Año 2016')
        od2016.hist()
        print('Año 2017')
        od2017.hist()
        print('#######Listado del Top N de estaciones más utilizadas para un año dado.#######')
        print('Año 2014')
        print(od2014.topNStations())
        print('Año 2015')
        print(od2015.topNStations())
        print('Año 2016')
        print(od2016.topNStations())
        print('Año 2017')
        print(od2017.topNStations())
        print('######Listado del Top N de viajes más comunes para un año dado. Donde un viaje se define por su estación de salida y de llegada.#######')
        print('Año 2014')
        print(od2014.topNTravels())
        print('Año 2015')
        print(od2015.topNTravels())
        print('Año 2016')
        print(od2016.topNTravels())
        print('Año 2017')
        print(od2017.topNTravels())
        print('######Identificación de horas punta para un año determinado sin tener en cuenta el día.#########')
        print('Año 2014')
        print(od2014.rushHours())
        print('Año 2015')
        print(od2015.rushHours())
        print('Año 2016')
        print(od2016.rushHours())
        print('Año 2017')
        print(od2017.rushHours())
        print('############Cantidad de viajes totales. Comparativa 2014-2015#############')
        print('############Número de viajes año 2014: ' + str(od2014.dfTravels.index.size) + '. Número de viajes año 2015: ' + str(od2015.dfTravels.index.size)+'############')
        print('############Capacidad instalada total############')                
        print('Año 2014')
        print(od2014.totalSize())
        print('Año 2015')
        print(od2015.totalSize())
        print('Año 2016')
        print(od2016.totalSize())
        print('Año 2017')
        print(od2017.totalSize())
        print('##########################################')
        print('##########################################')
        print('##########################################')
        print('##########################################')        
        
if __name__ == "__main__":
    Main.main()
    print('############# Unitary Tests ##############')
    UnitTests.main()