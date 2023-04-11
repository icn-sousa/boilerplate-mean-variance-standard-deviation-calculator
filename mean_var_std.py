import numpy as np

def calculate(list):
    # ValueError raised if a list contain less than 9 elements 
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    # convert the list with 9 digits into a 3 x 3 Numpy array (matrix)
    matrix = np.array((list)).reshape(3,3)
    
    # mean along both axes and for the flattened matrix
    mean = [matrix.mean(axis = 0), 
            matrix.mean(axis = 1), 
            matrix.flatten().mean()]
    # convert to list
    mean_lst = [i.tolist() for i in mean]
    
    # variance along both axes and for the flattened matrix
    var = [matrix.var(axis = 0), 
           matrix.var(axis = 1), 
           matrix.flatten().var()]
    # convert to list
    var_lst = [j.tolist() for j in var]
    
    # standard deviation along both axes and for the flattened matrix
    std = [matrix.std(axis = 0), 
           matrix.std(axis = 1), 
           matrix.flatten().std()]
    # convert to list
    std_lst = [k.tolist() for k in std]
    
    # max along both axes and for the flattened matrix
    max = [matrix.max(axis = 0), 
           matrix.max(axis = 1), 
           matrix.flatten().max()]
    # convert to list
    max_lst = [l.tolist() for l in max]
    
    # min along both axes and for the flattened matrix
    min = [matrix.min(axis = 0), 
           matrix.min(axis = 1), 
           matrix.flatten().min()]
    # convert to list
    min_lst = [m.tolist() for m in min]
    
    # sum along both axes and for the flattened matrix
    sum = [matrix.sum(axis = 0), 
           matrix.sum(axis = 1), 
           matrix.flatten().sum()]
    # convert to list
    sum_lst = [n.tolist() for n in sum]
    
    # dictionay keys and values
    keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    values = [mean_lst, var_lst, std_lst, max_lst, min_lst, sum_lst]
    # create dictionary
    calculations = {keys[i]: values[i] for i in range(len(keys))}
    # return dictionary
    return calculations
