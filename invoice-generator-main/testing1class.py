# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:38:59 2023

@author: User
"""
#The creation of TestData class based on testing1  

import pandas as pd

class TestData:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def get_test_data(self, ID):
        test = self.df[self.df["ZP_ID"] == ID]
        test.to_csv('test_data.csv', index=False)

test_data = TestData('Performance_data.csv')
ID = input("enter the ID: ")
test_data.get_test_data(ID)
