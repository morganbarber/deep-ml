import numpy as np

def make_diagonal(x):
	# Your code here
	result = np.zeros((x.shape[0], x.shape[0]))

	for i in range(x.shape[0]):
		result[i, i] = x[i]

	return result