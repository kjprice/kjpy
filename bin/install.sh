#!/bin/bash

cd "$(dirname "$0")"
cd ..

pypath="$(which python)"

$pypath -m pip install --no-build-isolation --editable .
