import numpy as np

inputs = np.loadtxt('training_set.csv', delimiter=',')
x_train = inputs[:,0:100]

print(x_train)