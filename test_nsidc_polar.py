from nsidc_polar_lonlat import *
from nsidc_polar_ij import *
import numpy as np
import time

print("Testing Northern hemisphere, 12.5km")
tic = time.clock()
for i in range(1,608):
    jj = np.arange(1, 896)
    ll = nsidc_polar_ij(i, jj, 12.5, 1)
    ij = nsidc_polar_lonlat(ll[0], ll[1], 12.5, 1)
    if np.any(np.not_equal(ij[0], i)) or np.any(np.not_equal(ij[1], jj)):
        print("error: i=" + str(i))
        break
print(" time=" + str(time.clock() - tic))

print("Testing Southern hemisphere, 12.5km")
tic = time.clock()
for i in range(1, 632):
    jj = np.arange(1, 664)
    ll = nsidc_polar_ij(i, jj, 12.5, -1)
    ij = nsidc_polar_lonlat(ll[0], ll[1], 12.5, -1)
    if np.any(np.not_equal(ij[0], i)) or np.any(np.not_equal(ij[1], jj)):
        print("error: i=" + str(i))
        break
print(" time=" + str(time.clock() - tic))
