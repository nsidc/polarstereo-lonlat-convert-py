import numpy as np


def polar_xy_to_lonlat(x, y, true_scale_lat, re, e, hemisphere):
    """Convert from Polar Stereographic (x, y) coordinates to
    geodetic longitude and latitude.
    
    Args:
        x (float): X coordinate(s) in km
        y (float): Y coordinate(s) in km
        true_scale_lat (float): true-scale latitude in degrees
        hemisphere (1 or -1): 1 for Northern hemisphere, -1 for Southern
        re (float): Earth radius in km
        e (float): Earth eccentricity
    
    Returns:
        If x and y are scalars then the result is a
        two-element list containing [longitude, latitude].
        If x and y are numpy arrays then the result will be a two-element
        list where the first element is a numpy array containing
        the longitudes and the second element is a numpy array containing
        the latitudes.
    """

    e2 = e*e
    slat = true_scale_lat*np.pi/180
    rho = np.sqrt(x**2 + y**2)

    if abs(true_scale_lat-90.) < 1e-5:
        t = rho*np.sqrt((1 + e)**(1 + e)*(1 - e)**(1 - e))/(2*re)
    else:
        cm = np.cos(slat)/np.sqrt(1 - e2*(np.sin(slat)**2))
        t = np.tan((np.pi/4) - (slat/2))/((1 - e*np.sin(slat)) /
                                          (1 + e*np.sin(slat)))**(e/2)
        t = rho*t/(re*cm)

    chi = (np.pi/2) - 2*np.arctan(t)
    lat = chi + ((e2/2) + (5*e2**2/24) + (e2**3/12))*np.sin(2*chi) + \
        ((7*e2**2/48) + (29*e2**3/240))*np.sin(4*chi) + \
        (7*e2**3/120)*np.sin(6*chi)
    lat = hemisphere*lat*180/np.pi
    lon = np.arctan2(hemisphere*x, -hemisphere*y)
    lon = hemisphere*lon*180/np.pi
    lon = lon + np.less(lon, 0)*360
    return [lon, lat]


def polar_lonlat_to_xy(longitude, latitude, true_scale_lat, re, e, hemisphere):
    """Convert from geodetic longitude and latitude to Polar Stereographic
    (X, Y) coordinates in km.

    Args:
        longitude (float): longitude or longitude array in degrees
        latitude (float): latitude or latitude array in degrees (positive)
        true_scale_lat (float): true-scale latitude in degrees
        re (float): Earth radius in km
        e (float): Earth eccentricity
        hemisphere (1 or -1): Northern or Southern hemisphere
    
    Returns:
        If longitude and latitude are scalars then the result is a
        two-element list containing [X, Y] in km.
        If longitude and latitude are numpy arrays then the result will be a
        two-element list where the first element is a numpy array containing
        the X coordinates and the second element is a numpy array containing
        the Y coordinates.
    """

    lat = abs(latitude)*np.pi/180
    lon = longitude*np.pi/180
    slat = true_scale_lat*np.pi/180

    e2 = e*e

    # Snyder (1987) p. 161 Eqn 15-9
    t = np.tan(np.pi/4 - lat/2) / \
        ((1 - e*np.sin(lat))/(1 + e*np.sin(lat)))**(e/2)

    if abs(90 - true_scale_lat) < 1e-5:
        # Snyder (1987) p. 161 Eqn 21-33
        rho = 2*re*t/np.sqrt((1 + e)**(1 + e)*(1 - e)**(1 - e))
    else:
        # Snyder (1987) p. 161 Eqn 21-34
        tc = np.tan(np.pi/4 - slat/2) / \
            ((1 - e*np.sin(slat))/(1 + e*np.sin(slat)))**(e/2)
        mc = np.cos(slat)/np.sqrt(1 - e2*(np.sin(slat)**2))
        rho = re*mc*t/tc

    x = rho*hemisphere*np.sin(hemisphere*lon)
    y = -rho*hemisphere*np.cos(hemisphere*lon)
    return [x, y]
