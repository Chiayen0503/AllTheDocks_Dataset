import pandas as pd

def add_vertical_speed(df):
    speedx_list = []
    for i in range(len(df)):
        speedx = ((df['Speed3D'].iloc[i])**2 - (df['Speed'].iloc[i])**2)**(1/2)
        speedx_list.append(speedx)
    df['SpeedX'] = speedx_list
    return df


def add_accl3d(df, exclude_X=False):
    vect_len_list = []
    if not exclude_X:
        for i in range(len(df)):
            sum_square = (df['AcclX'].iloc[i])**2+df['AcclY'].iloc[i]**2+df['AcclZ'].iloc[i]**2
            out = sum_square**(1/2)
            vect_len_list.append(out)
    else:
        for i in range(len(df)):
            sum_square =df['AcclY'].iloc[i]**2+df['AcclZ'].iloc[i]**2
            out = sum_square**(1/2)
            vect_len_list.append(out)        

    df['Accl3D']=vect_len_list
    return df