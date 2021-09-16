#!/bin/bash

set -eo pipefail

. activate lonlat

flake8 --config .flake8 .

pytest test.py
