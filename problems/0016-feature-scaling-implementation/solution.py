import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	min, max = (data.min(axis=0), data.max(axis=0))
	std = data.std(axis=0)
	mean = data.mean(axis=0)
	standardized_data = (data - mean) / std
	normalized_data = (data - min) / (max - min)
	return standardized_data, normalized_data