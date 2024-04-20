# cmake_py
Pass variables and arrays from cmake to python and vice versa.

## Function Description
Function `run_python` executes a Python script located at `scriptPath` and returns the values of the variables listed in `OUTPUT_VARIABLES_NAMES`.

## Input:
- `scriptPath`: The path to the Python script.
- `OUTPUT_VARIABLES_NAMES`: A list of variable names that are expected to be in the output of the Python script.

## Return:
- All variables from `OUTPUT_VARIABLES_NAMES` with their corresponding values.
