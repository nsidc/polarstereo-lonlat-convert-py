import numpy as np

from constants import (
    EARTH_ECCENTRICITY,
    EARTH_RADIUS_KM,
    NORTH,
    TRUE_SCALE_LATITUDE,
)
from polar_convert import polar_lonlat_to_xy
from validators import validate_hemisphere, validate_grid_size


def nsidc_polar_lonlat(longitude, latitude, grid_size, hemisphere):
    """Transform from geodetic longitude and latitude coordinates
    to NSIDC Polar Stereographic I, J coordinates

    Args:
        longitude (float): longitude or longitude array in degrees
        latitude (float): latitude or latitude array in degrees (positive)
        grid_size (float): 6.25, 12.5 or 25; the grid_size cell dimensions in km
        hemisphere ('north' or 'south'): Northern or Southern hemisphere

    Returns:
        If longitude and latitude are scalars then the result is a
        two-element list containing [I, J].
        If longitude and latitude are numpy arrays then the result will
        be a two-element list where the first element is a numpy array for
        the I coordinates and the second element is a numpy array for
        the J coordinates.

    Examples:
        print(nsidc_polar_lonlat(350.0, 34.41, 12.5, 1))
            [608, 896]
    """

    validate_grid_size(grid_size)
    hemisphere = validate_hemisphere(hemisphere)

    if hemisphere == NORTH:
        delta = 45
        imax = 1216
        jmax = 1792
        xmin = -3850 + grid_size / 2
        ymin = -5350 + grid_size / 2
    else:
        delta = 0
        imax = 1264
        jmax = 1328
        xmin = -3950 + grid_size / 2
        ymin = -3950 + grid_size / 2

    if grid_size == 12.5:
        imax = imax // 2
        jmax = jmax // 2
    elif grid_size == 25:
        imax = imax // 4
        jmax = jmax // 4

    x, y = polar_lonlat_to_xy(
        longitude + delta,
        np.abs(latitude),
        TRUE_SCALE_LATITUDE,
        EARTH_RADIUS_KM,
        EARTH_ECCENTRICITY,
        hemisphere
    )
    i = (np.round((x - xmin) / grid_size)).astype(int) + 1
    j = (np.round((y - ymin) / grid_size)).astype(int) + 1
    # Flip grid_size orientation in the 'y' direction
    j = jmax - j + 1
    return [i, j]
