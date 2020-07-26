# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:58:04 2020

@author: aortegar
"""


import pandas as pd

class ConstantsDF:
    
    top_start_sta_2014 = ["MÃ©tro Mont-Royal (Rivard / du Mont-Royal)","de Maisonneuve / de Bleury",
                    "de Maisonneuve / Stanley","Square St-Louis","Mackay /de Maisonneuve (Sud)",
                    "du Mont-Royal / Clark","MÃ©tro St-Laurent (de Maisonneuve / St-Laurent)",
                    "St-Dominique / Rachel","St-AndrÃ© / Laurier","Marquette / du Mont-Royal"]
    
    top_end_sta_2014 = ["MÃ©tro Mont-Royal (Rivard / du Mont-Royal)","de Maisonneuve / de Bleury",
                    "de Maisonneuve / Stanley","MÃ©tro St-Laurent (de Maisonneuve / St-Laurent)",
                    "Berri / de Maisonneuve","St-Urbain / RenÃ©-LÃ©vesque","Mackay /de Maisonneuve (Sud)",
                    "Square Victoria","MÃ©tro Place-d'Armes (Viger / St-Urbain)","Ste-Catherine / St-Hubert"]
    
    top_total_sta_2014 = ["MÃ©tro Mont-Royal (Rivard / du Mont-Royal)","de Maisonneuve / de Bleury",
                    "de Maisonneuve / Stanley","MÃ©tro St-Laurent (de Maisonneuve / St-Laurent)",
                    "Mackay /de Maisonneuve (Sud)","Berri / de Maisonneuve","Square St-Louis",
                    "St-Urbain / RenÃ©-LÃ©vesque","du Mont-Royal / Clark","Roy / St-Laurent"]
    
    colNames = "TOP_start", "TOP_end", "TOP_total"
    
    topNStationsDF = pd.DataFrame(list(zip(top_start_sta_2014,top_end_sta_2014,top_total_sta_2014)), columns = colNames)
    
    
    list_start_end = ['MÃ©tro Jean-Drapeau --> MÃ©tro Jean-Drapeau', 
                      'de la Commune / Place Jacques-Cartier --> de la Commune / Place Jacques-Cartier',
                      'Garnier / du Mont-Royal --> MÃ©tro Mont-Royal (Rivard / du Mont-Royal)',
                      'Marquette / du Mont-Royal --> MÃ©tro Mont-Royal (Rivard / du Mont-Royal)',
                      'de Maisonneuve / Stanley --> Mackay /de Maisonneuve (Sud)',
                      'de Maisonneuve / Stanley --> Desjardins / Ontario',
                      'MÃ©tro Pie-IX (Pierre-de-Coubertin / Pie-IX) --> Garnier / du Mont-Royal',
                      'MÃ©tro Mont-Royal (Rivard / du Mont-Royal) --> Marquette / du Mont-Royal',
                      'MÃ©tro Mont-Royal (Rivard / du Mont-Royal) --> Tupper / Atwater',
                      'Mackay /de Maisonneuve (Sud) --> de Maisonneuve / Stanley']
    
    listStartEndDF = pd.DataFrame(list(list_start_end), columns = ['name'])

    list_rushHours = ['17-18','16-17','18-19','08-09','15-16','19-20','13-14','14-15','12-13','09-10']