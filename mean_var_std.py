import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        
    new_array = np.array([list[0:3], list[3:6], list[6:]])

    means = [
        np.mean(new_array, axis=0).tolist(),
        np.mean(new_array, axis=1).tolist(),
        np.mean(new_array)
    ]

    variances = [
        np.var(new_array, axis=0).tolist(),
        np.var(new_array, axis=1).tolist(),
        np.var(new_array)
    ]

    std_devs = [
        np.std(new_array, axis=0).tolist(),
        np.std(new_array, axis=1).tolist(),
        np.std(new_array)
    ]

    maxs = [
        np.max(new_array, axis=0).tolist(),
        np.max(new_array, axis=1).tolist(),
        np.max(new_array)
    ]

    mins = [
        np.min(new_array, axis=0).tolist(),
        np.min(new_array, axis=1).tolist(),
        np.min(new_array)
    ]

    sums = [
        np.sum(new_array, axis=0).tolist(),
        np.sum(new_array, axis=1).tolist(),
        np.sum(new_array)
    ]

    calculations = {
        'mean': means,
        'variance': variances,
        'standard deviation': std_devs,
        'min': mins,
        'max': maxs,
        'sum': sums
    }

    return calculations