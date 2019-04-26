print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
import projectile_data as pd

"""This module will analyze the test data provided from projectile_data and eliminate parameters that are determined to not heavily influence the end test result"""
#First, miscellaneous test parameters will be deleted and 
#analysis results will be given to the user

# Build a classification task using 3 informative features
X,y= make_classification(n_samples=len(td.velocity_measured),
                           n_features=len(td.test_parameters),
                           n_informative=3,
                           n_redundant=0,
                           n_repeated=0,
                           n_classes=2,
                           random_state=0,
                           shuffle=False)

# Build a forest and compute the feature importances
