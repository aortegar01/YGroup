# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:47:20 2020

@author: aortegar
"""

import pandas as pd
import os.path
import json

class ODFiles:

    
    def __init__(self, year):
        self.year = year    
        
        my_path = os.path.abspath(os.path.dirname(__file__))
        pathTravels = os.path.join(my_path, 'files\OD_' + self.year + '.csv')
        pathStations = os.path.join(my_path, 'files\Stations_' + self.year + '.csv')
        pathJson = os.path.join(my_path,'files\stations.json')
        with open(pathTravels) as dfT:
            self.dfTravels  = pd.read_csv(dfT, index_col=0)
        with open(pathStations) as dfS:
            self.dfStations  =  pd.read_csv(dfS)
        with open(pathJson) as data_stations_json:    
            data = json.load(data_stations_json)  
            self.StationsJson = pd.json_normalize(data, 'stations', record_prefix='')
        
    def hist(self):
        hist_plot = self.dfTravels["duration_sec"].hist(range=[0, 3000],bins=150)
        hist_plot.set_title('Travel times of ' + self.year)
        hist_plot.set_xlabel('Duration Sec')
        hist_plot.set_ylabel('Frecuency')

    def topNStations(self):
        # N = 10
        startDF = pd.DataFrame(self.dfTravels['start_station_code'].value_counts()[:10].index.tolist(),columns = 'start_station_code'.split())
        startResult = pd.merge(startDF,self.dfStations,how='inner',left_on=['start_station_code'],right_on=['code'])['name']
         
        endDF = pd.DataFrame(self.dfTravels['end_station_code'].value_counts()[:10].index.tolist(),columns = 'end_station_code'.split())
        endResult = pd.merge(endDF,self.dfStations,how='inner',left_on=['end_station_code'],right_on=['code'])['name']

        totalDF = pd.DataFrame(pd.concat([self.dfTravels["start_station_code"],self.dfTravels["end_station_code"]]).value_counts()[:10].index.tolist(),columns='Total_Station_Names'.split())
        totalResult = pd.merge(totalDF,self.dfStations,how='inner',left_on=['Total_Station_Names'],right_on=['code'])['name']
        
    
        return pd.DataFrame(list(zip(startResult, endResult, totalResult)), 
               columns =['TOP_start', 'TOP_end','TOP_total'])
   
    def topNTravels(self):
        df = self.dfTravels[['start_station_code','end_station_code']]
        df['start-end'] = self.dfTravels['start_station_code'].astype(str) + '-' + self.dfTravels['end_station_code'].astype(str)
        topTravelsDF = pd.DataFrame(df['start-end'].value_counts()[:10].index.tolist(),columns = 'start-end'.split())
        topTravelsDF['start'] = topTravelsDF['start-end'].str[0:4]
        topTravelsDF['end'] = topTravelsDF['start-end'].str[5:]
        mergeStart = pd.merge(topTravelsDF, self.dfStations[['name','code']].astype(str),how='inner',left_on=['start'],right_on=['code'])
        mergeEnd = pd.merge(topTravelsDF, self.dfStations[['name','code']].astype(str),how='inner',left_on=['end'],right_on=['code'])
        result = pd.DataFrame(mergeStart['name'] + ' --> ' + mergeEnd['name'],columns = ['name'])
        
        return result
        
    def rushHours(self):
        self.dfTravels['hour'] = self.dfTravels['start_date'].str.slice(11, 13) 
        self.dfTravels['hour+1'] = self.dfTravels['start_date'].str.slice(11, 13).astype(int) + 1
        listHours = [1,2,3,4,5,6,7,8,9]
        self.dfTravels['hour+1'] = self.dfTravels['hour+1'].apply(lambda x: '0' + str(x) if x in listHours else x)
        self.dfTravels['Rush_hours'] =  self.dfTravels['hour'] + '-' + self.dfTravels['hour+1'].astype(str)
        
        return self.dfTravels['Rush_hours'].value_counts()[:10].index.tolist()
        
    def totalSize(self):
        df = self.StationsJson[['n','s','ba','bx']]
        df['totalSize'] = df['ba'] + df['bx']
        
        return df[['n','s','totalSize']]

    