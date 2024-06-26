project(cmake_to_python)
cmake_minimum_required(VERSION 3.20)

# Function for easy use python script from cmake
# Input:
#   scriptPath - path to the python script
#   OUTPUT_VARIABLES_NAMES - variables that must be in the output of the python script
# Return:
#   All variables from OUTPUT_VARIABLES_NAMES
function(run_python scriptPath)

    cmake_parse_arguments(PARSE_ARGV 1 arg "" "" "OUTPUT_VARIABLES_NAMES")

    find_package(Python REQUIRED COMPONENTS Interpreter)
    
    set(VARIABLES_LIST)
    set(ARGV_SEPARATOR "\;")
    set(SCRIPT_OUTPUT_PATH "script_output.json")

    get_cmake_property(ALL_VARIABLES VARIABLES)

    # Store all global variables and their values in VARIABLES_LIST
    foreach(VARIABLE_NAME IN LISTS ALL_VARIABLES)
        set(VARIABLE_VALUE ${${VARIABLE_NAME}})

        foreach(VALUE IN LISTS VARIABLE_VALUE)
            if(VALUE MATCHES ";")
                message(FATAL_ERROR "${VARIABLE_NAME} consists ';'")
            endif()
        endforeach()

        list(APPEND VARIABLES_LIST "${VARIABLE_NAME};${${VARIABLE_NAME}}")
        list(APPEND VARIABLES_LIST "${ARGV_SEPARATOR}")
    endforeach()

    # Run script
    execute_process(COMMAND ${Python_EXECUTABLE} ${scriptPath} ${VARIABLES_LIST}
                    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                    COMMAND_ERROR_IS_FATAL ANY)

    # Read script output JSON
    file(READ ${SCRIPT_OUTPUT_PATH} OUTPUT_JSON)
    message(STATUS "Output JSON file: ${OUTPUT_JSON}")

    # Read all needed variables from JSON and define their in PARENT_SCOPE
    foreach(VARIABLE_NAME IN LISTS arg_OUTPUT_VARIABLES_NAMES)
        string(JSON VARIABLE_VALUE GET ${OUTPUT_JSON} ${VARIABLE_NAME})
        string(REPLACE "," ";" VARIABLE_VALUE ${VARIABLE_VALUE})

        set(${VARIABLE_NAME} ${VARIABLE_VALUE} PARENT_SCOPE)
        message(STATUS "${VARIABLE_NAME} = ${VARIABLE_VALUE}")
    endforeach()
endfunction()

# Start of build logic
run_python(script.py
           OUTPUT_VARIABLES_NAMES test_variable test_arr)

message(STATUS "Result: '${test_variable}' and '${test_arr}'")

add_executable(test main.c)
