#!/bin/bash

cd "$(dirname "$0")"
cd ..

pypath="$(which python3)"

rm -r dist/*

# Make sure to change version number

$pypath -m build
$pypath -m twine upload dist/*
