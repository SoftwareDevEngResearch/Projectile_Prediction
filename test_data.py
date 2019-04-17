### The data will be loaded from an Excel file with the left most column being the velocity measured
import pandas as pd
#from pandas import ExcelWriter
#from pandas import ExcelFile
import numpy as np

cube=pd.read_excel('cube_data.xlsx', sheet_name='Sheet1')
velocity_measured=cube[cube.columns[0]]
test_parameters=cube.columns[2:]

test_conditions=np.empty([len(test_parameters),len(velocity_measured)])

i=2    
while i<cube.columns.size:
    test_conditions[i-2]=np.array(cube.values[:,i])
    i=i+1

#number of rows
nor=cube.shape[0]
cube_learn={}
cube_test={}

for i in range(nor-5):
    cube_learn[i]=np.array(list(cube.values[i]))
for i in range(nor-5,nor):
    cube_test[i]=np.array(list(cube.values[i]))


### This is the end of importing the test data

