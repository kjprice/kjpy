#!/bin/bash

cd "$(dirname "$0")"
cd ..

pypath="$(which python)"

nodemon -e py -x "$pypath -m unittest"
