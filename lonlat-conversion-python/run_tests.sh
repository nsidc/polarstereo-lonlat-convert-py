#!/bin/bash

set -eo pipefail

. activate lonlat

python test.py

flake8 --config .flake8 .
