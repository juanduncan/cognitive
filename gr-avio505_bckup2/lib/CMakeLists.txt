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
list(APPEND avio505_sources
    three_ch_multip_rtdex_impl.cc
    adc_three_ch_demux_rtdex_impl.cc
    syncher_impl.cc
    check_flux_impl.cc
    resta_impl.cc
    three_ch_mux_rtdex_v2_impl.cc )

set(avio505_sources "${avio505_sources}" PARENT_SCOPE)
if(NOT avio505_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT avio505_sources)

add_library(gnuradio-avio505 SHARED ${avio505_sources})
target_link_libraries(gnuradio-avio505 ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-avio505 PROPERTIES DEFINE_SYMBOL "gnuradio_avio505_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-avio505 PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-avio505
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_avio505_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_avio505.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_avio505.cc
)

add_executable(test-avio505 ${test_avio505_sources})

target_link_libraries(
  test-avio505
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-avio505
)

GR_ADD_TEST(test_avio505 test-avio505)
