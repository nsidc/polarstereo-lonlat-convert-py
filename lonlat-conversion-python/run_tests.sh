#!/bin/bash

set -eo pipefail

. activate lonlat

python test_nsidc_polar.py

flake8 --config .flake8 .
