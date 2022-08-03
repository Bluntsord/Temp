#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "thriftz::thriftz" for configuration "Release"
set_property(TARGET thriftz::thriftz APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(thriftz::thriftz PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libthriftz.0.16.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libthriftz.0.16.0.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS thriftz::thriftz )
list(APPEND _IMPORT_CHECK_FILES_FOR_thriftz::thriftz "${_IMPORT_PREFIX}/lib/libthriftz.0.16.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
