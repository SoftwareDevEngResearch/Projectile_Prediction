"""The data will be loaded from an Excel file with the left most column being the velocity measured"""
import pandas as pd
import numpy as np
import sys

#The following is test data imported if the correct file was chosen
def collect_data(threat,det):
    """
    Takes the imported excel data and forms it into usable objects for machine learning.

    Args:
        threat: imported data of known system
        det: imported data of predicted system

    Returns:
        datapar_threat: collection of classes that define the system information to be used for machine learning
        datapar_det: collection of classes that define the system that needs to be predicted with machine learning
        threat_learn:learn_test("threat")
        threat_pred: learn_test("prediction")

    Raises:
        KeyError: Raises an exception.
    """
    class collected_data(object):
        """This will classify the test data"""
        def __init__(self,data,column):
            self.title=threat[threat.columns[column]].name
            self.parameter=np.array(list(threat.values[0:,column]))
    class predic_data(object):
        """This will classify the prediction data"""
        def __init__(self,data,column):
            self.title=det[det.columns[column]].name
            self.parameter=np.array(list(det.values[0:,column]))

    def datapar(sys):
        """
        This system is used to create an array of objects defining the known data results.

        Args:
            sys: a numpy array of the data that will be used to train the machine.

        Returns:
            an object list of the parameters observed in the test.

        Raises:
            KeyError: Raises an exception.
        """
        data_parameters=sys.columns[0:]
        i=0
        system=[]
        for each in data_parameters:
            name=data_parameters[i]
            name=collected_data(sys,i)
            i+=1
            system.append(name)
        return system
    def predpar(sys):
        """
        Creates an array of objects defining the known parameters of the instreated
        environment with unknown gun powder loads.

        Args:
            sys: a numpy array of the data that will be used to predict gunpowder loads.

        Returns:
            an object list of the parameters comprising the test environment.

        Raises:
            KeyError: Raises an exception.
        """
        data_parameters=sys.columns[0:]
        i=0
        system=[]
        for each in data_parameters:
            name=data_parameters[i]
            name=predic_data(sys,i)
            i+=1
            system.append(name)
        return system

    def learn_test(tpe):
        """
        Breaks up the data into arrays for machine learning

        Args:
            tpe: state is the data required is "threat" data or "prediction" data

        Returns:
            Single array of gunpowder loads.

        Raises:
            KeyError: Raises an exception.
        """
        """This function will return the data of the imported file to teach the machine and test the prediction system"""
        if tpe=="threat":
            nor=threat.shape[0]
            learn={}
            learn=np.array(list(threat.values))
            return learn
        if tpe=="prediction":
            pred={}
            pred=np.array(list(det.values))
            return pred

    datapar_threat=datapar(threat)
    datapar_det=predpar(det)
    threat_learn=learn_test("threat")
    threat_pred=learn_test("prediction")
#    cube_learn=learn_test("learn")
#    cube_test=learn_test("test")
    return datapar_threat,datapar_det,threat_learn,threat_pred
