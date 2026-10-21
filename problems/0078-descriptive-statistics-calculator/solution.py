import numpy as np

def interpol(data, i):
    k = int(i)
    d = i - k

    if k == len(data) - 1:
        return float(data[k])

    return data[k] + d * (data[k+1] - data[k])

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    arr = np.asarray(data)
    mean = np.sum(arr)/len(arr)
    variance = np.sum((arr - mean) ** 2) / len(arr)
    p25 = interpol(arr.tolist(), (25/100) * (len(arr) - 1))
    p50 = interpol(arr.tolist(), (50/100) * (len(arr) - 1))
    p75 = interpol(arr.tolist(), (75/100) * (len(arr) - 1))

    vals, cons = np.unique(arr, return_counts=True)

    return {
        'mean': mean,
        'median': np.median(arr),
        'mode': vals[cons.argmax()],
        'variance': variance,
        'standard_deviation': variance ** 0.5,
        '25th_percentile': p25,
        '50th_percentile': p50,
        '75th_percentile': p75,
        'interquartile_range': p75 - p25
    }