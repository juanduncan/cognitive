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
list(APPEND COWN_sources
    tag_generator_impl.cc
    test_impl.cc
    syncher_impl.cc
    syncher2_impl.cc
    resta_impl.cc
    tx_valve_impl.cc
    tx_valve2_impl.cc
    tx_valve3_impl.cc )

set(COWN_sources "${COWN_sources}" PARENT_SCOPE)
if(NOT COWN_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT COWN_sources)
add_library(gnuradio-COWN SHARED ${COWN_sources}
    )
target_link_libraries(gnuradio-COWN ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-COWN PROPERTIES DEFINE_SYMBOL "gnuradio_COWN_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-COWN PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-COWN
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_COWN_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_COWN.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_COWN.cc
)

add_executable(test-COWN ${test_COWN_sources})

target_link_libraries(
  test-COWN
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-COWN
)

GR_ADD_TEST(test_COWN test-COWN)
