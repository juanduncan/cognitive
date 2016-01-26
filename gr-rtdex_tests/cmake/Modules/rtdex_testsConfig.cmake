INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_RTDEX_TESTS rtdex_tests)

FIND_PATH(
    RTDEX_TESTS_INCLUDE_DIRS
    NAMES rtdex_tests/api.h
    HINTS $ENV{RTDEX_TESTS_DIR}/include
        ${PC_RTDEX_TESTS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RTDEX_TESTS_LIBRARIES
    NAMES gnuradio-rtdex_tests
    HINTS $ENV{RTDEX_TESTS_DIR}/lib
        ${PC_RTDEX_TESTS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RTDEX_TESTS DEFAULT_MSG RTDEX_TESTS_LIBRARIES RTDEX_TESTS_INCLUDE_DIRS)
MARK_AS_ADVANCED(RTDEX_TESTS_LIBRARIES RTDEX_TESTS_INCLUDE_DIRS)

