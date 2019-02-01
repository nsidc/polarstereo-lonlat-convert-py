# NSIDC Polar Stereographic Projection

https://nsidc.org/data/polar-stereo

NSIDC's polar stereographic projection specifies a projection plane or grid tangent to the Earth's surface at 70° northern and southern latitude. While this increases the distortion at the poles by six percent and decreases the distortion at the grid boundaries by the same amount, the latitude of 70° was selected so that little or no distortion would occur in the marginal ice zone.

This repo contains conversion routines between longitude/latitude and generic x, y (km) coordinates. There are also conversion routines between longitude/latitude and i, j grid coordinates for specific datasets for AMSR-E and SSM/I.

## Python Code

**polar_convert.py**:
Convert from longitude, latitude to Polar Stereographic x, y (km) and vice versa.  
`polar_lonlat_to_xy` replaces Fortran `mapll.for`  
`polar_xy_to_lonlat` replaces Fortran `mapxy.for`  

**nsidc_polar_lonlat.py**:
Transform from longitude and latitude
    to NSIDC Polar Stereographic I, J (grid) coordinates.

**nsidc_polar_ij.py**:
Transform from NSIDC Polar Stereographic I, J (grid) coordinates to longitude and latitude.

**read_mask**: Read in a Polar Stereographic mask file and return the data.

**read_mask_hdf**: Read in an HDF4 Polar Stereographic mask file and return the data.

**display_mask**: Read in and display a Polar Stereographic mask file.

## FORTRAN Code

**mapll.for** (_obsolete_): Convert from latitude and longitude to Polar Stereographic x, y (km).

**mapxy.for** (_obsolete_): Convert from Polar Stereographic x, y (km) to latitude and longitude.

**locate.for** (_obsolete_): Transform I,J coordinates of an SSM/I grid cell to latitude and longitude and vice versa.

## IDL Code

**extract_ice.pro** (_obsolete_): Extract sea ice concentrations from Polar Stereographic grid files.

**disp_ssmi_ice_xa.pro** (_obsolete_): Create animations of sea ice concentrations from SSM/I Polar Grids.
