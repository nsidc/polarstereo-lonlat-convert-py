![NSIDC logo](../images/NSIDC_DAAC_2018_smv2.jpg)

# locate.for

This program transforms I,J coordinates of an SSM/I grid cell to latitude and
longitude coordinates. This program provides the inverse functions as
well. LOCATE interfaces to the revised forms of the subroutines, MAPXY and
MAPLL.

## Level of Support

<b>This directory is fully supported by the NSIDC DAAC</b>. If you discover any problems or
bugs, please submit an Issue. If you would like to contribute to this
repository, you may fork the repository and submit a pull request.

See the [LICENSE](../LICENSE) for details on permissions and warranties. Please
contact nsidc@nsidc.org for more information.


## Requirements

`locate.for` requries [`gfortran`](https://gcc.gnu.org/wiki/GFortran).


## Installation

Install `gfortran` and then compile the `locatefor` executable with the
following command:

```
gfortran locate.for mapll.for mapxy.for -o locatefor
```

### With Docker

[`Docker`](https://www.docker.com/) can be used to run `locate.for`.

A `Dockerfile` has been included in this directory and can be used to create a
Docker image runs `locatefor`.

To build the `locatefor` Docker image:

```
docker build . -t locatefor
```

## Usage

To use `locate.for`, simply run the compiled `locatefor` and follow the prompts.

For example, to use the `locatefor` docker image to convert northern hemisphere
I,J coordinates to latitude,longitude coordinates:

```
$ docker run -it locatefor
 Enter the grid cell dimension:
  1. 12.5 Km
  2. 25.0 Km
1
 Enter the hemisphere of interest:
  1. North
  2. South
1
 Enter one of the following transform functions:
  1. Convert I,J to Latitude, Longitude
  2. Convert Latitude, Longitude to I,J
1
 Enter the column number
 the valid range is (1-608)
200
 Enter the row number
 the valid range is (1-896)
300
   67.1696243       167.778168
```

## License

See [LICENSE](../LICENSE).


## Code of Conduct

See [Code of Conduct](../CODE_OF_CONDUCT.md).


## Credit

This software was developed by the NASA National Snow and Ice Data Center
Distributed Active Archive Center.
