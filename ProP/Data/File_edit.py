import tables as tb
import numpy as np
#import sys
#sys.path.append('C:/Users/beard/Desktop/Python Programs/Class Project/Projectile_Prediction/ProP/Data')
import projectile_data as proj

f=tb.open_file('C:/Users/beard/Desktop/Python Programs/Class Project/Projectile_Prediction/ProP/Data/Test_data.txt','a')
#f.create_group(h5file.root,'test_data','cube')
cube=f.create_array('/','Cube_Parameters',proj.collected_data,proj.system[:])
f.root.test_data.cube.append(cube)
