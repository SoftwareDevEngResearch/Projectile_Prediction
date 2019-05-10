"""The data will be loaded from an Excel file with the left most column being the velocity measured"""
import pandas as pd
import numpy as np
import sys
sys.path.append('C:/Users/beard/Desktop/Python Programs/Class Project/Projectile_Prediction/ProP/Data')

#The following is test data imported if the correct file was chosen    
# collected_data.py
def collect_data():
    cube=pd.read_excel("Cube_data.xlsx","Real") 
    
    class collected_data(object):
        """This will classify the test data"""
        def __init__(self,data,column):
            self.title=cube[cube.columns[column]].name
            self.parameter=np.array(list(cube.values[0:,column]))
    
    def datapar(cube):
        data_parameters=cube.columns[0:]
        i=0
        system=[]
        for each in data_parameters:
            name=data_parameters[i]
            name=collected_data(cube,i)
            i+=1
            system.append(name)
        return system
    
    def learn_test(tpe):
        """This function will return the data of the imported file to teach the machine and test the prediction system"""
        nor=cube.shape[0]
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
    
    datapar=datapar(cube)
    cube_learn=learn_test("learn")
    cube_test=learn_test("test")
    return datapar,cube_learn,cube_test