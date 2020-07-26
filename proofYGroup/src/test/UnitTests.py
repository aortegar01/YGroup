# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:54:14 2020

@author: aortegar
"""


import unittest
import os.path
import pandas as pd
from src.test.ConstantsDF import ConstantsDF as Cte
from src.main.ODFiles import ODFiles as OD


class UnitTests(unittest.TestCase):
    
    def test_topNStations(self):
        st_df_2014 = OD.ODFiles('2014').topNStations()
        cteDF = Cte.topNStationsDF
        self.assertEqual(st_df_2014.to_string(), cteDF.to_string())
     
    def test_topNTravels(self):
        st_df_start_end_2014 = OD.ODFiles('2014').topNTravels()
        cteDF = Cte.listStartEndDF
        self.assertEqual(st_df_start_end_2014.to_string(), cteDF.to_string())
    
    def test_rushHours(self):
        st_rush_hours = OD.ODFiles('2014').rushHours()
        cteList = Cte.list_rushHours
        self.assertEqual(st_rush_hours,cteList)
        
    def test_totalSize(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, 'file\stationsCsv.csv')
        with open(path) as df:
            df = pd.read_csv(df)
        df_total_size = OD.ODFiles('2014').totalSize()
        self.assertEqual(df_total_size.to_string(), df.to_string())
    
    def main():
         unittest.main() 
