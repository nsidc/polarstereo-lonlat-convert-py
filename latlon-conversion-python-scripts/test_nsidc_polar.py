# Automated testing for nsidc_polar_* routines.
# Run through all grid sizes for both hemispheres,
# convert from all grid locations to lon/lat and back again,
# verify that the output is identical.
#
# To run, from a command prompt:
#   python test_nsidc_polar.py
#
# CT, NSIDC, Jan 2019.
#
from nsidc_polar_lonlat import nsidc_polar_lonlat
from nsidc_polar_ij import nsidc_polar_ij
import numpy as np
import time
    
grid = [6.25, 12.5, 25]
imax = [1216, 608, 304]
jmax = [1792, 896, 448]
for g in [0, 1, 2]:
    print("Testing Northern hemisphere, " + str(grid[g]) + "km")
    tic = time.perf_counter()
    for i in range(1, imax[g]):
        jj = np.arange(1, jmax[g])
        lonlat = nsidc_polar_ij(i, jj, grid[g], 1)
        ij = nsidc_polar_lonlat(lonlat[0], lonlat[1], grid[g], 1)
        if np.any(np.not_equal(ij[0], i)) or np.any(np.not_equal(ij[1], jj)):
            print("error: i=" + str(i))
            break
    print(" time=" + str(time.perf_counter() - tic))

imax = [1264, 632, 316]
jmax = [1328, 664, 332]
for g in [0, 1, 2]:
    print("Testing Southern hemisphere, " + str(grid[g]) + "km")
    tic = time.perf_counter()
    for i in range(1, imax[g]):
        jj = np.arange(1, jmax[g])
        lonlat = nsidc_polar_ij(i, jj, grid[g], -1)
        ij = nsidc_polar_lonlat(lonlat[0], lonlat[1], grid[g], -1)
        if np.any(np.not_equal(ij[0], i)) or np.any(np.not_equal(ij[1], jj)):
            print("error: i=" + str(i))
            break
    print(" time=" + str(time.perf_counter() - tic))
