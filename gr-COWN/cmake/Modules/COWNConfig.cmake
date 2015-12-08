INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_COWN COWN)

FIND_PATH(
    COWN_INCLUDE_DIRS
    NAMES COWN/api.h
    HINTS $ENV{COWN_DIR}/include
        ${PC_COWN_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    COWN_LIBRARIES
    NAMES gnuradio-COWN
    HINTS $ENV{COWN_DIR}/lib
        ${PC_COWN_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(COWN DEFAULT_MSG COWN_LIBRARIES COWN_INCLUDE_DIRS)
MARK_AS_ADVANCED(COWN_LIBRARIES COWN_INCLUDE_DIRS)

