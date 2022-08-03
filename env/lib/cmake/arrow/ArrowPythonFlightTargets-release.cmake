#----------------------------------------------------------------
# Generated CMake target import file for configuration "RELEASE".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "arrow_python_flight_shared" for configuration "RELEASE"
set_property(TARGET arrow_python_flight_shared APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(arrow_python_flight_shared PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libarrow_python_flight.700.0.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libarrow_python_flight.700.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS arrow_python_flight_shared )
list(APPEND _IMPORT_CHECK_FILES_FOR_arrow_python_flight_shared "${_IMPORT_PREFIX}/lib/libarrow_python_flight.700.0.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
