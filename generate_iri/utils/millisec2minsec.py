import datetime
def get_min_sec(ms):
    result = datetime.datetime.fromtimestamp(ms/1000.0)
    reformat = str(0)+':'+str(result.minute)+':'+str(result.second)
    return reformat