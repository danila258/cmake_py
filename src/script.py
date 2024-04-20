import sys
import json

# Common functions
def parseArgv() -> dict:
    argv = {}
    cur_key = ""

    for arg in sys.argv:
        if arg == ';':
            cur_key = ""
        elif not cur_key:
            cur_key = arg
            argv[cur_key] = []
        else:
            argv[cur_key].append(arg)

    for key in argv:
        value = argv[key]
        if len(value) == 1:
            argv[key] = value[0]
        elif len(value) == 0:
            argv[key] = ""
    
    return argv

def saveResult(file_path : str, **kwargs) -> None:
    result = {}
    separator = ','

    for key, value in kwargs.items():
        line = ""
        if isinstance(value, str):
            line = value
        else:
            for i in value:
                line += str(i) + separator

        if line.endswith(separator):
            line = line[:-1]

        result[key] = line

    with open(file_path, 'w') as file:
        json.dump(result, file)
 
# Script start
args = parseArgv()
saveResult(args["SCRIPT_OUTPUT_PATH"], test_variable="Some value", test_arr=[1, 2, 3, 4])
