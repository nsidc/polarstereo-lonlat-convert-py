import time

import numpy as np
import pytest

from polar_convert import polar_ij_to_lonlat, polar_lonlat_to_ij
from polar_convert.constants import NORTH, SOUTH, VALID_GRID_SIZES
from polar_convert.validators import validate_hemisphere, validate_grid_size


def _test_hemisphere(hemisphere, imax_list, jmax_list):
    """Test nsidc_polar_* functions.

    Run through all grid sizes for the given hemisphere, convert from all
    grid_size locations to lon/lat and back again, verify that the output is
    identical.
    """
    for idx, grid_size in enumerate(VALID_GRID_SIZES):
        print(f'Testing {hemisphere} hemisphere, {grid_size}km')
        tic = time.perf_counter()
        for i in range(1, imax_list[idx]):
            jj = np.arange(1, jmax_list[idx])
            lonlat = polar_ij_to_lonlat(i, jj, grid_size, hemisphere)
            ij = polar_lonlat_to_ij(lonlat[0], lonlat[1], grid_size, hemisphere)
            if np.any(np.not_equal(ij[0], i)) or np.any(np.not_equal(ij[1], jj)):
                raise RuntimeError("error: i=" + str(i))
        print(" time=" + str(time.perf_counter() - tic))


def test_northern_hemisphere():
    _test_hemisphere(
        NORTH,
        [1216, 608, 304],
        [1792, 896, 448],
    )


def test_southern_hemisphere():
    _test_hemisphere(
        SOUTH,
        [1264, 632, 316],
        [1328, 664, 332],
    )


def test_validate_hemisphere():
    assert 'north' == validate_hemisphere('NORTH')
    assert 'south' == validate_hemisphere('SOUTH')

    # Assert that a `ValueError` is raised when invalid input is given
    for invalid_hemi in ('n', 's', 'noth', 'soth', 1, -1):
        with pytest.raises(ValueError):
            validate_hemisphere(invalid_hemi)


def test_validate_grid_size():
    for grid_size in VALID_GRID_SIZES:
        assert grid_size == validate_grid_size(grid_size)

    for invalid_grid_size in ('foo', 1, 400, -1):
        with pytest.raises(ValueError):
            validate_grid_size(invalid_grid_size)
