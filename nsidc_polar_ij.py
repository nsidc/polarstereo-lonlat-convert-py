import doctest
from polar_convert import polar_xy_to_lonlat
import numpy as np

def nsidc_polar_ij(i, j, grid, hemisphere):
    """Transform from NSIDC Polar Stereographic I, J coordinates
    to longitude and latitude coordinates
    
    Args:
        i (int): an integer or integer array giving the x grid coordinate(s)
        j (int): an integer or integer array giving the y grid coordinate(s)
        grid (float): 6.25, 12.5 or 25; the grid cell dimensions in km
        hemisphere (1 or -1): Northern or Southern hemisphere
    
    Returns:
        If i and j are scalars then the result is a
        two-element list containing [longitude, latitude].
        If i and j are numpy arrays then the result will
        be a two-element list where the first element is a numpy array containing
        the longitudes and the second element is a numpy array containing
        the latitudes.

    Examples:
        print(nsidc_polar_ij(608, 896, 12.5, 1))
            [350.01450147320855, 34.40871032516291]
    """

    true_scale_lat = 70
    re = 6378.273
    e = 0.081816153

    if grid != 6.25 and grid != 12.5 and grid != 25:
        raise ValueError("Illegal grid value: Possible values are 6.25, 12.5, or 25")
    
    if hemisphere != 1 and hemisphere != -1:
        raise ValueError("Illegal hemisphere value: Possible values are 1 or -1")

    if hemisphere == 1:
        delta = 45
        imax = 1216
        jmax = 1792
        xmin = -3850 + grid/2
        ymin = -5350 + grid/2
    else:
        delta = 0
        imax = 1264
        jmax = 1328
        xmin = -3950 + grid/2
        ymin = -3950 + grid/2

    if grid == 12.5:
        imax = imax//2
        jmax = jmax//2
    elif grid == 25:
        imax = imax//4
        jmax = jmax//4

    if np.any(np.less(i, 1)) or np.any(np.greater(i, imax)):
        raise ValueError("'i' value is out of range: [1, " +
            str(imax) + "]")
    if np.any(np.less(j, 1)) or np.any(np.greater(j, jmax)):
        raise ValueError("'j' value is out of range: [1, " +
            str(jmax) + "]")

    # Convert I, J pairs to x and y distances from origin.
    x = ((i - 1)*grid) + xmin
    y = ((jmax - j)*grid) + ymin
    lonlat = polar_xy_to_lonlat(x, y, true_scale_lat, re, e, hemisphere)
    lon = lonlat[0] - delta #lonlat.lon - delta
    lon = lon + np.less(lon, 0)*360
    return [lon, lonlat[1]] #PolarLonLat(lon, lonlat.lat)

def _doctests():
    """
    >>> nsidc_polar_ij(1, 1, 12.5, 1)
    [168.33507963020855, 31.041601496464544]
    >>> nsidc_polar_ij(608, 1, 12.5, 1)
    [102.35468099709325, 31.426360396715474]
    >>> nsidc_polar_ij(1, 896, 12.5, 1)
    [279.2726017772003, 33.98819310110948]
    >>> nsidc_polar_ij(608, 896, 12.5, 1)
    [350.01450147320855, 34.40871032516291]

    >>> nsidc_polar_ij(1, 1, 12.5, -1)
    [317.7632627634601, -39.29786078224397]
    >>> nsidc_polar_ij(632, 1, 12.5, -1)
    [42.236737236539895, -39.29786078224397]
    >>> nsidc_polar_ij(1, 664, 12.5, -1)
    [225.0, -41.51518413616323]
    >>> nsidc_polar_ij(632, 664, 12.5, -1)
    [135.0, -41.51518413616323]
    """

if __name__ == "__main__":
    doctest.testmod(optionflags=doctest.ELLIPSIS)
