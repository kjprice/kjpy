#!/bin/bash

cd "$(dirname "$0")"
cd ..

nodemon -e py -x 'python -m unittest'
