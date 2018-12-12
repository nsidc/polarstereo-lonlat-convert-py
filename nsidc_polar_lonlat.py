import doctest
from polar_convert import *

def nsidc_polar_lonlat(longitude, latitude, grid, hemisphere):
    """Transform from geodetic longitude and latitude coordinates
    to NSIDC Polar Stereographic I, J coordinates
    
    Args:
        longitude (float): longitude or longitude array in degrees
        latitude (float): latitude or latitude array in degrees (always positive)
        grid (float): 6.25, 12.5 or 25; the grid cell dimensions in km
        hemisphere (1 or -1): Northern or Southern hemisphere
    
    Returns:
        If longitude and latitude are scalars then the result is a
        two-element list containing [I, J].
        If longitude and latitude are numpy arrays then the result will
        be a two-element list where the first element is a numpy array containing
        the I coordinates and the second element is a numpy array containing
        the J coordinates.

    Examples:
        print(nsidc_polar_lonlat(608, 896, 12.5, 1))
            [lon=350.01450147320855, lat=34.40871032516291)
    """

    true_scale_lat = 70
    re = 6378.273
    e = 0.081816153

    if grid != 6.25 and grid != 12.5 and grid != 25:
        raise ValueError("Illegal grid value: Possible values are 6.25, 12.5, or 25")
    
    if hemisphere >= 0:
        delta = 45
        imax = 1216
        jmax = 1792
        xmin = -3850 + grid/2
        ymin = -5350 + grid/2
    else:
        delta = 0
        imax = 1263
        jmax = 1327
        xmin = -3950 + grid/2
        ymin = -3950 + grid/2

    if grid == 12.5:
        imax = (imax + 1)//2
        jmax = (jmax + 1)//2
    elif grid == 25:
        imax = (imax + 1)//4
        jmax = (jmax + 1)//4

    xy = polar_lonlat_to_xy(longitude + delta, np.abs(latitude),
        true_scale_lat, re, e, hemisphere)
    i = (np.round((xy[0] - xmin)/grid)).astype(int) + 1
    j = (np.round((xy[1] - ymin)/grid)).astype(int) + 1
    # Flip grid orientation in the 'y' direction
    j = jmax - j + 1
    return [i, j] #[i, j)

def _doctests():
    """
    >>> nsidc_polar_lonlat(168.3, 31.04, 12.5, 1)
    [1, 1]
    >>> nsidc_polar_lonlat(102.4, 31.4, 12.5, 1)
    [608, 1]
    >>> nsidc_polar_lonlat(279.3, 33.99, 12.5, 1)
    [1, 896]
    >>> nsidc_polar_lonlat(350.0, 34.41, 12.5, 1)
    [608, 896]

    >>> nsidc_polar_lonlat(317.8, 39.30, 12.5, -1)
    [1, 1]
    >>> nsidc_polar_lonlat(42.24, 39.29, 12.5, -1)
    [632, 1]
    >>> nsidc_polar_lonlat(225.0, 41.5, 12.5, -1)
    [1, 664]
    >>> nsidc_polar_lonlat(135.0, 41.5, 12.5, -1)
    [632, 664]
    """

if __name__ == "__main__":
    doctest.testmod(optionflags=doctest.ELLIPSIS)
