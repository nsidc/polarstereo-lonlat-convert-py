#!/bin/bash

set -eo pipefail

flake8 --config .flake8 .

pytest test.py
