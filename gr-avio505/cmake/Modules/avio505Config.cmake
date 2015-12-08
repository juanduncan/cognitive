INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_AVIO505 avio505)

FIND_PATH(
    AVIO505_INCLUDE_DIRS
    NAMES avio505/api.h
    HINTS $ENV{AVIO505_DIR}/include
        ${PC_AVIO505_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    AVIO505_LIBRARIES
    NAMES gnuradio-avio505
    HINTS $ENV{AVIO505_DIR}/lib
        ${PC_AVIO505_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(AVIO505 DEFAULT_MSG AVIO505_LIBRARIES AVIO505_INCLUDE_DIRS)
MARK_AS_ADVANCED(AVIO505_LIBRARIES AVIO505_INCLUDE_DIRS)

