import geopy.distance

def twoGPSpoints_distance(coords_1, coords_2):
    """
    format: decimal minute
    
    ex, 
        coords_1 = (52.2296756, 21.0122287)
        coords_2 = (52.406374, 16.9251681)
    """
    return geopy.distance.geodesic(coords_1, coords_2).km