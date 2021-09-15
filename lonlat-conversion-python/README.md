![NSIDC logo](../images/NSIDC_DAAC_2018_smv2.jpg)

# NSIDC Polar Stereographic Projection lon/lat python scripts

Utilities for converting polar stereographic coordinates.

NSIDC's polar stereographic projection specifies a projection plane or grid
tangent to the Earth's surface at 70° northern and southern latitude. While this
increases the distortion at the poles by six percent and decreases the
distortion at the grid boundaries by the same amount, the latitude of 70° was
selected so that little or no distortion would occur in the marginal ice zone.

This directory contains conversion functions between longitude/latitude and generic x,
y (km) coordinates. There are also conversion functions between
longitude/latitude and i, j grid coordinates for specific datasets for AMSR-E
and SSM/I.

See also [Polar Stereo Overview](https://nsidc.org/data/polar-stereo).

## Level of Support

<b>This directory is fully supported by the NSIDC DAAC</b>. If you discover any problems or
bugs, please submit an Issue. If you would like to contribute to this
repository, you may fork the repository and submit a pull request.

See the [LICENSE](../LICENSE) for details on permissions and warranties. Please
contact nsidc@nsidc.org for more information.

## Requirements

* Python 3.6 or higher (tested with 3.6.7 and 3.9.7)
* [`numpy`](https://numpy.org/) (python library)

These requirements are also included in the provided `environment.yml` file,
which can be used with [conda](https://docs.conda.io/en/latest/) to install the
requirements into a `conda` environment.


## Installation

It is reccomended to install the requirements for the included scripts with `conda`:

```
$ conda env create -f environment.yml
$ conda activate lonlat
```

## Usage

See the individual files for details.  The functions defined in these files can
be used in your own projects.

### `polar_convert.py`

Convert from longitude, latitude to Polar Stereographic x, y (km) and vice
versa. This module defines two functions:

* `polar_lonlat_to_xy`: Convert from geodetic longitude and latitude to Polar
  Stereographic (X, Y) coordinates in km. Functional equivilient of
  [`mapll.for`](../locate/mapll.for).
  
* `polar_xy_to_lonlat`: Convert from Polar Stereographic (x, y) coordinates to
  geodetic longitude and latitude. Functional equivilent of
  [`mapxy.for`](../locate/mapxy.for)

### `nsidc_polar_lonlat.py`

This module defines a function `nsidc_polar_lonlat` that transforms from
longitude and latitude to NSIDC Polar Stereographic I, J (grid) coordinates.

### `nsidc_polar_ij.py`

This module defines a function `nsidc_polar_ij` that transforms from NSIDC Polar
Stereographic I, J (grid) coordinates to longitude and latitude.

```
>>> from nsidc_polar_ij import nsidc_polar_ij
>>> i = 10  # `i` is an int representing the x grid coordinate
>>> j = 200  # `j` is an int representing y grid coordinate
>>> grid_size = 12.5  # in km
>>> hemisphere = 1  # 1 is 'north' and anything else is 'south'
>>> nsidc_polar_ij(i, j, grid, hemisphere)
[183.02869857834057, 45.89915728375587]
```


### `test_nsidc_polar.py`

Simple tests for the `nsidc_polar_lonlat` and `nsidc_polar_ij` functions.

```
$ python test_nsidc_polar.py
Testing Northern hemisphere, 6.25km
 time=0.6453779018484056
Testing Northern hemisphere, 12.5km
 time=0.2094833878800273
Testing Northern hemisphere, 25km
 time=0.07760114083066583
Testing Southern hemisphere, 6.25km
 time=0.549166772980243
Testing Southern hemisphere, 12.5km
 time=0.18855400010943413
Testing Southern hemisphere, 25km
 time=0.07395890913903713
```


## License

See [LICENSE](../LICENSE).


## Code of Conduct

See [Code of Conduct](../CODE_OF_CONDUCT.md).


## Credit

This software was developed by the NASA National Snow and Ice Data Center
Distributed Active Archive Center.
