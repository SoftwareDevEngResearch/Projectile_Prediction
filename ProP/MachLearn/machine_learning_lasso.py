#This is comparing the velocity recorded to just the powder load using lasso
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import projectile_data as prod



"""This is looking at 3 parameters"""
# Split the data into training/testing sets
cube_X_train =np.reshape(np.array([[prod.system[2].parameter[:-30]], [prod.system[3].parameter[:-30]], [prod.system[4].parameter[:-30]]]).T,(-1,3))
cube_X_test = np.reshape(np.array([[prod.system[2].parameter[-30:]], [prod.system[3].parameter[-30:]], [prod.system[4].parameter[-30:]]]).T,(-1,3))

# Split the targets into training/testing sets
cube_y_train = np.reshape(np.array([prod.system[0].parameter[:-30]]),(-1,1))
cube_y_test = np.reshape(np.array([prod.system[0].parameter[-30:]]),(-1,1))



alpha = 0.1
enet = linear_model.ElasticNet(alpha=alpha, l1_ratio=0.7)

y_pred_enets = enet.fit(cube_X_train, cube_y_train).predict(cube_X_test)
r2_score_enet = r2_score(cube_y_test, y_pred_enets)
print(enet)
plt.plot(cube_X_test[0:,0], y_pred_enets, color='red', linewidth=3)
plt.scatter(cube_X_train[0:,0], cube_y_train,  color='black')


plt.xticks(())
plt.yticks(())

plt.show()
