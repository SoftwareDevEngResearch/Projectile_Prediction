#This is comparing the velocity recorded to just the powder load using linear regression
#This is currently how the powder load is determined in the field
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import projectile_data as prod


"""This method is comparing system predictions with one parameter"""
# Use a predetermined number of features
#cube_X = prod.cube[prod.cube.columns[2:3]]


# Split the data into training/testing sets
cube_X_train = np.reshape(np.array([prod.system[2].parameter[:-10]]),(-1,1))
cube_X_test = np.reshape(np.array([prod.system[2].parameter[-10:]]),(-1,1))

# Split the targets into training/testing sets
cube_y_train = np.reshape(np.array([prod.system[0].parameter[:-10]]),(-1,1))
cube_y_test = np.reshape(np.array([prod.system[0].parameter[-10:]]),(-1,1))

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


#plt.scatter(cube_X_test[cube_X_test.columns[1]], cube_y_test,  color='black')
#plt.plot(cube_X_test[cube_X_test.columns[1]], cube_y_pred, color='blue', linewidth=3)

