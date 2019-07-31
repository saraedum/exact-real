#!/bin/bash

pushd standardese
~/proj/eskin/standardese/build/tool/standardese -I ../../src -I$CONDA_PREFIX/include `find ../../src/exact-real/ -name "$1"'*.hpp' -not -path '*external*'` --compilation.standard=c++17 --output.format commonmark --
popd
