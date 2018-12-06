def calculate_variance(values):
    '''
    Function to calculate variance of a list of numbers.

    Arguments
    ---------
    values : list of floats
        The measurements.

    Returns
    -------
    v : float
        The sample variance of the input values.
    '''
    mean = calculate_mean(values)
    
    sum_diffsq = 0
    for val in values:
        diff = val - mean
        diffsq = diff ** 2
        sum_diffsq = sum_diffsq + diffsq

    return sum_diffsq/(len(values) - 1)

def calculate_mean(values):
    '''Calculate mean of values.'''
    total = 0

    for val in values:
        total = total + val

    return total / len(values)
