#!/bin/bash

cd "$(dirname "$0")"
cd ..

# pypath="$(which python)"

# $pypath -m pip install --no-build-isolation --editable .
/Users/kjprice/anaconda3/envs/py3.10/bin/python -m pip install --editable .
/Users/kjprice/anaconda3/envs/ml/bin/python -m pip install --editable .
/Users/kjprice/anaconda3/bin/python -m pip install --editable .

# OOPS - should probably reset this
/Users/kjprice/anaconda3/envs/kjpy/bin/python -m pip install --editable .

# /Users/kjprice/anaconda3/envs/py3.10/bin/python -m pip uninstall kjpy
