import numpy as np

def moving_avg(a, window_width):
    denoised = np.convolve(a, np.ones(window_width)/window_width, 'same')
    return denoised

def double_integral(times, accl):
    if len(accl) != len(times):
        raise Exception("accl and times should be numpy arrays of the same length")
        # If times[0] != 0 then there will be unexpected behaviour.
    else:
        inner_integrals = np.empty_like(accl)
        inner_integrals[0] = 0 # We assume that the cyclist is stationary at time 0.
        for i in range(1,len(times)):
            a1 = accl[i-1]
            a2 = accl[i]
            w = times[i] - times[i-1]
            trapezium_area = 0.5*(a1 + a2)*w
            inner_integrals[i] = inner_integrals[i-1] + trapezium_area
        speeds = np.abs(inner_integrals)
        return np.trapz(speeds,times) 
    
def calculate_total_distance(times, s):
    if len(times)==len(s):
        out = np.trapz(s,times)
        return out
    else:
        raise Exception('times have to be the same length as speed data!')
        

def calculate_IRI(times, a, s):#source: https://www.mdpi.com/1424-8220/18/3/914?fbclid=IwAR0kwJiW8Tps4s_Mb6amyYG98ERun2hxBDeN3wKgt91FYnDNpdgE5vTUkKg
    total_distance = calculate_total_distance(times, s)
    return double_integral(times, a)/total_distance


def IRI_sliding_window(times_list, a_list, s_list, width, stride):
    """
    Return IRI index in each time in times_list, the first and the last time frame 
    with index 0:+(width/2) and -(width/2):-1 will have None IRI value 
    """
    out_iri_list = [None for i in range(int(width/2))] 
    out_times_index_list = [None for i in range(int(width/2))]
    
    start=0
    end=width-1

    while end<=len(times_list)-1:
        window_times = np.array(times_list[start:end])
        window_a = np.array(a_list[start:end])
        window_s = np.array(s_list[start:end])
        iri = calculate_IRI(window_times, window_a, window_s)
        out_iri_list.append(iri)
        out_times_index_list.append(int((start+end)/2))
        start+=stride
        end+=stride
    
    for i in range(len(times_list)-len(out_iri_list)):
        out_iri_list.append(None)
        
    for i in range(len(times_list)-len(out_times_index_list)):
        out_times_index_list.append(None)
        
    if len(times_list)==len(out_iri_list)==len(out_times_index_list):
        return out_iri_list, out_times_index_list
    else:
        raise Exception('out_iri_list, out_times_index_list and times_list should have the same length!')