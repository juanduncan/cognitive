/* -*- c++ -*- */

#define COWN_MISC_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "COWN_misc_swig_doc.i"

%{
#include "COWN_misc/adc_tags_gen.h"
%}


%include "COWN_misc/adc_tags_gen.h"
GR_SWIG_BLOCK_MAGIC2(COWN_misc, adc_tags_gen);
