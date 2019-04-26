"""The data will be loaded from an Excel file with the left most column being the velocity measured"""
import pandas as pd
import numpy as np
import sys as sys

#file_name=input("File name in folder: ")
#sheet=input("Sheet name data is on: ")


cube=pd.read_excel("cube_data.xlsx","Real")    
#The following is test data imported if the correct file was chosen    
# collected_data.py
class collected_data(object):
    """This will classify the test data"""
    def __init__(self,data,column):
        self.title=cube[cube.columns[column]].name
        self.parameter=np.array(list(cube.values[0:,column]))
        
data_parameters=cube.columns[0:]
i=0
system=[]
for each in data_parameters:
    name=data_parameters[i]
    name=collected_data(cube,i)
    i+=1
    system.append(name)

"""Need to change the imported data into a class organized object.
This could be used to identify the variety of parameters, how the tests were
conducted and any other factors worth noting/differences observed"""

#number of rows
#This needs to be changed so that it does not analyze a test number of tests but allocates a percentage of the
#provided data to test and learn    
nor=cube.shape[0]


def learn_test(tpe):
    if tpe=="test":
        cube_test={}
        for i in range(nor-90,nor):
            cube_test[i]=np.array(list(cube.values[i]))
        return cube_test
    if tpe=="learn":
        cube_learn={}
        for i in range(nor-90):
            cube_learn[i]=np.array(list(cube.values[i]))
        return cube_learn
cube_test=learn_test("test")
cube_learn=learn_test("learn")


### This is the end of importing the test data

