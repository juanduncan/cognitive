INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_COWN_MISC COWN_misc)

FIND_PATH(
    COWN_MISC_INCLUDE_DIRS
    NAMES COWN_misc/api.h
    HINTS $ENV{COWN_MISC_DIR}/include
        ${PC_COWN_MISC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    COWN_MISC_LIBRARIES
    NAMES gnuradio-COWN_misc
    HINTS $ENV{COWN_MISC_DIR}/lib
        ${PC_COWN_MISC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(COWN_MISC DEFAULT_MSG COWN_MISC_LIBRARIES COWN_MISC_INCLUDE_DIRS)
MARK_AS_ADVANCED(COWN_MISC_LIBRARIES COWN_MISC_INCLUDE_DIRS)

