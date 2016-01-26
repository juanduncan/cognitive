# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND rtdex_tests_sources
    resta_impl.cc
)

set(rtdex_tests_sources "${rtdex_tests_sources}" PARENT_SCOPE)
if(NOT rtdex_tests_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT rtdex_tests_sources)

add_library(gnuradio-rtdex_tests SHARED ${rtdex_tests_sources})
target_link_libraries(gnuradio-rtdex_tests ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-rtdex_tests PROPERTIES DEFINE_SYMBOL "gnuradio_rtdex_tests_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-rtdex_tests PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-rtdex_tests
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_rtdex_tests_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_rtdex_tests.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_rtdex_tests.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_resta.cc
)

add_executable(test-rtdex_tests ${test_rtdex_tests_sources})

target_link_libraries(
  test-rtdex_tests
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-rtdex_tests
)

GR_ADD_TEST(test_rtdex_tests test-rtdex_tests)
