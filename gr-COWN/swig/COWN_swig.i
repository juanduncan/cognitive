/* -*- c++ -*- */

#define COWN_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "COWN_swig_doc.i"

%{
#include "COWN/tag_generator.h"
#include "COWN/test.h"
#include "COWN/syncher.h"
#include "COWN/syncher2.h"
#include "COWN/resta.h"
%}


%include "COWN/tag_generator.h"
GR_SWIG_BLOCK_MAGIC2(COWN, tag_generator);
%include "COWN/test.h"
GR_SWIG_BLOCK_MAGIC2(COWN, test);

%include "COWN/syncher.h"
GR_SWIG_BLOCK_MAGIC2(COWN, syncher);
%include "COWN/syncher2.h"
GR_SWIG_BLOCK_MAGIC2(COWN, syncher2);


%include "COWN/resta.h"
GR_SWIG_BLOCK_MAGIC2(COWN, resta);
