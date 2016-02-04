# Install script for directory: /home/nutaq/cognitive/gr-COWN/grc

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
<<<<<<< HEAD
    "/home/juan/cognitive/gr-COWN/grc/COWN_tag_generator.xml"
    "/home/juan/cognitive/gr-COWN/grc/COWN_test.xml"
    "/home/juan/cognitive/gr-COWN/grc/COWN_syncher.xml"
    "/home/juan/cognitive/gr-COWN/grc/COWN_syncher2.xml"
    "/home/juan/cognitive/gr-COWN/grc/COWN_resta.xml"
    "/home/juan/cognitive/gr-COWN/grc/COWN_tx_valve.xml"
    "/home/juan/cognitive/gr-COWN/grc/COWN_tx_valve2.xml"
    "/home/juan/cognitive/gr-COWN/grc/COWN_tx_valve3.xml"
=======
    "/home/nutaq/cognitive/gr-COWN/grc/COWN_tag_generator.xml"
    "/home/nutaq/cognitive/gr-COWN/grc/COWN_test.xml"
    "/home/nutaq/cognitive/gr-COWN/grc/COWN_syncher.xml"
    "/home/nutaq/cognitive/gr-COWN/grc/COWN_syncher2.xml"
    "/home/nutaq/cognitive/gr-COWN/grc/COWN_resta.xml"
>>>>>>> e993df33b66c0d5f0e4079bc7eda6af8a5ee6fbf
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

