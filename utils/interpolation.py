import numpy as np
import pandas as pd
from bisect import bisect_left

def linearly_interpolate(t, data_times, data_values):
    """
    Given a list of times data_times and the corresponding list of values data_values,
    returns the value at time t by linearly interpolating data_values.
    """
    if t > max(data_times) or t < min(data_times):
        raise Exception(f'The time {t} is outside the data range (from {min(data_times)} to {max(data_times)})')
    i = bisect_left(data_times,t) # The smallest i such that t <= data_times[i]
    if i == 0:
        return data_values[0]
    else:
        t_after = data_times[i]
        t_before= data_times[i-1]
        v_after = data_values[i]
        v_before= data_values[i-1]
        
        t_width = t_after - t_before
        p = ( t_after - t ) / t_width
        return p * v_before + (1-p)*v_after
    
def iterate_interpolation(data, accl_data, imputed_column):
    tlist = data['Milliseconds'].tolist()
    vlist = data[imputed_column].tolist()

    target_times = accl_data['Milliseconds'].tolist()

    interpolated_list = [None] * len(target_times)

    for i,t in enumerate(target_times):
        try:
            interpolated_list[i] = linearly_interpolate(t,tlist,vlist)
        except:
            interpolated_list[i] = np.NaN
    
    accl_data[imputed_column] = interpolated_list
    return accl_data
