#This is comparing the velocity recorded to just the powder load using linear regression
#This is currently how the powder load is determined in the field
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import sys
import projectile_data as prod


def mach(threat,det):
    """
    This function produces results from machine learning
    Args:
        threat: Collected data on the system that needs to be analyzed.
        det: A collection of data points, with the same number of variables in "threat" that will
             be used to predict the recommended gun powder load.

    Returns:
        An array of predicted gun powder loads.

    Raises:
        KeyError: Raises an exception.
    """
    sys_threat,sys_det,threat_learn,threat_pred=prod.collect_data(threat,det)

    def linear_reg():
        """
        CURRENTLY NOT BEING USED
        Looks at linear regression machine learning with provided data.
        Args:
            None

        Returns:
            An array of predicted gun powder loads using linear regression.

        Raises:
            KeyError: Raises an exception.
        """
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
        """
        Looks at lasso with elastic net machine learning with provided data.
        Args:
            None

        Returns:
            An array of predicted gun powder loads using lasso with elastic net.

        Raises:
            KeyError: Raises an exception.
        """
        """This is looking at more than one parameter"""
        parameters=len(sys_threat)-1
        cube_X_train=np.empty(shape=(parameters,(len(threat_learn))),dtype=int)
        cube_X_pred= np.empty(shape=(parameters,(len(threat_pred))) ,dtype=int)
        i=1
        while i<parameters:
            print(i)
            new_train=np.array([sys_threat[i].parameter[0:]])
            cube_X_train[i-1]=new_train
            new_test=np.array([sys_det[i].parameter[0:]])
            cube_X_pred[i-1]=new_test
            i+=1

        cube_X_train=np.reshape(cube_X_train.T,(-1,parameters))
        cube_X_pred= np.reshape(cube_X_pred.T, (-1,parameters))

        """Split the targets into training/testing sets"""
        cube_y_train= np.reshape(np.array([sys_threat[0].parameter[0:]]),(-1,1))
        #cube_y_test = np.reshape(np.array([sys_det[0].parameter[0:]]),(-1,1))

        alpha = 0.1
        enet = linear_model.ElasticNet(alpha=alpha, l1_ratio=0.7)

        y_pred = enet.fit(cube_X_train, cube_y_train).predict(cube_X_pred)
        return y_pred


#    parameters=len(system)
#    if parameters==2:
#        return linear_reg()
#    elif parameters>2:
#        return lasso()
#    else:
#        print("Error in data recieved, not enough parameters.")

    return lasso()
