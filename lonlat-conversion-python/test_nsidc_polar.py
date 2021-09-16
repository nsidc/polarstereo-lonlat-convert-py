# Automated testing for nsidc_polar_* routines.
# Run through all grid sizes for both hemispheres,
# convert from all grid_size locations to lon/lat and back again,
# verify that the output is identical.
#
# To run, from a command prompt:
#   python test_nsidc_polar.py
#
# CT, NSIDC, Jan 2019.
#
import time

import numpy as np

from constants import NORTH, SOUTH
from nsidc_polar_ij import nsidc_polar_ij
from nsidc_polar_lonlat import nsidc_polar_lonlat

if __name__ == '__main__':
    grid_size = [6.25, 12.5, 25]
    imax = [1216, 608, 304]
    jmax = [1792, 896, 448]
    for g in [0, 1, 2]:
        print("Testing Northern hemisphere, " + str(grid_size[g]) + "km")
        tic = time.perf_counter()
        for i in range(1, imax[g]):
            jj = np.arange(1, jmax[g])
            lonlat = nsidc_polar_ij(i, jj, grid_size[g], NORTH)
            ij = nsidc_polar_lonlat(lonlat[0], lonlat[1], grid_size[g], NORTH)
            if np.any(np.not_equal(ij[0], i)) or np.any(np.not_equal(ij[1], jj)):
                raise RuntimeError("error: i=" + str(i))
        print(" time=" + str(time.perf_counter() - tic))

    imax = [1264, 632, 316]
    jmax = [1328, 664, 332]
    for g in [0, 1, 2]:
        print("Testing Southern hemisphere, " + str(grid_size[g]) + "km")
        tic = time.perf_counter()
        for i in range(1, imax[g]):
            jj = np.arange(1, jmax[g])
            lonlat = nsidc_polar_ij(i, jj, grid_size[g], SOUTH)
            ij = nsidc_polar_lonlat(lonlat[0], lonlat[1], grid_size[g], SOUTH)
            if np.any(np.not_equal(ij[0], i)) or np.any(np.not_equal(ij[1], jj)):
                raise RuntimeError("error: i=" + str(i))
        print(" time=" + str(time.perf_counter() - tic))
