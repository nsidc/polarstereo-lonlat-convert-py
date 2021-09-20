![NSIDC logo](/images/NSIDC_logo_2018_poster-1.png)

# NSIDC Polar Stereographic Projection lon/lat conversion: polar_convert

Python functions for converting polar stereographic coordinates.

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

<b>This repository is fully supported by NSIDC.</b> If you discover any problems or
bugs, please submit an Issue. If you would like to contribute to this
repository, you may fork the repository and submit a pull request.

See the [LICENSE](LICENSE) for details on permissions and warranties. Please
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

See the docstrings for individual functions in
[`polar_convert.py`](./polar_convert/polar_convert.py) for details.  The
functions defined in this file can be used in your own projects.

### `polar_lonlat_to_xy`

Convert from geodetic longitude and latitude to Polar Stereographic (X, Y)
coordinates in km. Functional equivilient of
[`mapll.for`](https://github.com/nsidc/polarstereo-latlon-convert-fortran/blob/main/locate/mapll.for).

```
>>> from polar_convert.constants import NORTH
>>> from polar_convert import polar_lonlat_to_xy
>>> longitude = 20  # longitude in degrees
>>> latitude = 80  # latitude in degrees
>>> true_scale_lat = 70  # true-scale latitude in degrees
>>> re = 6378.137  # earth radius in km
>>> e = 0.01671 # earth eccentricity
>>> hemisphere = NORTH
>>> polar_lonlat_to_xy(longitude, latitude, true_scale_lat, re, e, hemisphere)
[370.2450347527368, -1017.2398726483362]
```

### `polar_xy_to_lonlat`

Convert from Polar Stereographic (x, y) coordinates to geodetic longitude and
latitude. Functional equivilent of
[`mapxy.for`](https://github.com/nsidc/polarstereo-latlon-convert-fortran/blob/main/locate/mapxy.for).

```
>>> from polar_convert.constants import NORTH
>>> from polar_convert import polar_xy_to_lonlat
>>> x = 370.25  # x coordinate in km
>>> y = -1017.24  # y coordinate in km
>>> true_scale_lat = 70  # true-scale latitude in degrees 
>>> re = 6378.137  # earth radius in km
>>> e = 0.01671 # earth eccentricity
>>> hemisphere = NORTH
>>> polar_xy_to_lonlat(x, y, true_scale_lat, re, e, hemisphere)
[20.000244645773623, 79.99998329186566]
```

### `polar_lonlat_to_ij`

Convert from longitude and latitude to NSIDC Polar Stereographic I, J (grid)
coordinates.

```
>>> from polar_convert.constants import NORTH
>>> from polar_convert import polar_lonlat_to_ij
>>> longitude = 45  # longitude in degrees
>>> latitude = 85  # latitude in degrees
>>> grid_size = 6.25  # in km
>>> hemisphere = NORTH
>>> polar_lonlat_to_ij(longitude, latitude, grid, hemisphere)
[703, 936]
```

### `polar_ij_to_lonlat`

Convert from NSIDC Polar Stereographic I, J (grid) coordinates to longitude and
latitude.

```
>>> from polar_convert.constants import NORTH
>>> from polar_convert import polar_ij_to_lonlat
>>> i = 10  # `i` is an int representing the x grid coordinate
>>> j = 200  # `j` is an int representing y grid coordinate
>>> grid_size = 12.5  # in km
>>> hemisphere = NORTH
>>> polar_ij_to_lonlat(i, j, grid, hemisphere)
[183.02869857834057, 45.89915728375587]
```

## Development

See [DEVELOPMENT.md](./DEVELOPMENT.md) for information on how to contribute to
this python code.


## License

See [LICENSE](LICENSE), unless otherwise stated in the README file with each subdirectory.

## Code of Conduct

See [Code of Conduct](CODE_OF_CONDUCT.md).

## Credit

Credit is provided in the README file within each subdirectory.
