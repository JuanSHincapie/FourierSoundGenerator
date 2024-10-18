import numpy as np

def calculate_mse(signal1, signal2) :
    min_len = min(len(signal1), len(signal2))
    return np.mean((signal1[:min_len] - signal2[min_len]) ** 2)
