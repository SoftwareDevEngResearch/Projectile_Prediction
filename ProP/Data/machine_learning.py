#This is comparing the velocity recorded to just the powder load using linear regression
#This is currently how the powder load is determined in the field
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import sys
sys.path.append('C:/Users/beard/Desktop/Python Programs/Class Project/Projectile_Prediction/ProP/Data')
import projectile_data as prod


def mach(threat):
    system,learn,test=prod.collect_data(threat)
    
    def linear_reg():
        """This method is comparing system predictions with one parameter"""
        # Use a predetermined number of features
        system,cube_learn,cube_test=prod.collect_data()
        
        # Split the data into training/testing sets
        cube_X_train = np.reshape(np.array([system[2].parameter[:-10]]),(-1,1))
        cube_X_test = np.reshape(np.array([system[2].parameter[-10:]]),(-1,1))
        
        # Split the targets into training/testing sets
        cube_y_train = np.reshape(np.array([system[0].parameter[:-10]]),(-1,1))
        cube_y_test = np.reshape(np.array([system[0].parameter[-10:]]),(-1,1))
        
        # Create linear regression object
        regr = linear_model.LinearRegression()
        
        # Train the model using the training sets
        regr.fit(cube_X_train, cube_y_train)
        
        # Make predictions using the testing set
        cube_y_pred = regr.predict(cube_X_test)
        
        # The coefficients
        print('Coefficients: \n', regr.coef_)
        # The mean squared error
        print("Mean squared error: %.2f"
              % mean_squared_error(cube_y_test, cube_y_pred))
        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % r2_score(cube_y_test, cube_y_pred))
        
        # Plot outputs
        plt.scatter(cube_X_test, cube_y_test,  color='black')
        plt.plot(cube_X_test, cube_y_pred, color='blue', linewidth=3)
    
    
    
    def lasso():
        system,cube_learn,cube_test=prod.collect_data()
            
        """This is looking at more than one parameter"""
        parameters=len(system)-1
        cube_X_train=np.empty(shape=(parameters,(len(cube_learn))),dtype=int)
        cube_X_test= np.empty(shape=(parameters,(len(cube_test))),dtype=int)
        i=1
        while i<=parameters:
            new_train=np.array([system[i].parameter[:-30]])
            cube_X_train[i-1]=new_train
            new_test=np.array([system[i].parameter[-30:]])
            cube_X_test[i-1]=new_test
            i+=1
            
        cube_X_train=np.reshape(cube_X_train.T,(-1,parameters))
        cube_X_test=np.reshape(cube_X_test.T,(-1,parameters))
        
        # Split the targets into training/testing sets
        cube_y_train = np.reshape(np.array([system[0].parameter[:-30]]),(-1,1))
        cube_y_test = np.reshape(np.array([system[0].parameter[-30:]]),(-1,1))
                     
        alpha = 0.1
        enet = linear_model.ElasticNet(alpha=alpha, l1_ratio=0.7)
        
        y_pred_enets = enet.fit(cube_X_train, cube_y_train).predict(cube_X_test)
        r2_score_enet = r2_score(cube_y_test, y_pred_enets)
##        print("Mean squared error: %.2f" % r2_score_enet)
##        
##        print(enet)
##        plt.scatter(cube_X_test[0:,0], y_pred_enets, color='red', linewidth=3)
##        plt.scatter(cube_X_train[0:,0], cube_y_train,  color='black')
##        plt.xticks(())
##        plt.yticks(())
##        plt.show()
        
##        
##    parameters=len(system)
##    if parameters==2:
##        return linear_reg()
##    elif parameters>2:
##        return lasso()
##    else:
##        print("Error in data recieved, not enough parameters.")
        
    return lasso()
