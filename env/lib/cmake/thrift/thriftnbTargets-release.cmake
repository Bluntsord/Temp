#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "thriftnb::thriftnb" for configuration "Release"
set_property(TARGET thriftnb::thriftnb APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(thriftnb::thriftnb PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libthriftnb.0.16.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libthriftnb.0.16.0.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS thriftnb::thriftnb )
list(APPEND _IMPORT_CHECK_FILES_FOR_thriftnb::thriftnb "${_IMPORT_PREFIX}/lib/libthriftnb.0.16.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
