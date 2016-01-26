/* -*- c++ -*- */

#define RTDEX_TESTS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "rtdex_tests_swig_doc.i"

%{
#include "rtdex_tests/resta.h"
%}


%include "rtdex_tests/resta.h"
GR_SWIG_BLOCK_MAGIC2(rtdex_tests, resta);
