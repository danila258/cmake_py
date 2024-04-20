#!/bin/sh

BUILD_DIRECTORY=build

if [ ! -d "$BUILD_DIRECTORY" ]; then
  mkdir $BUILD_DIRECTORY
fi

cmake -S ./ -B build
cmake --build build
./build/test
