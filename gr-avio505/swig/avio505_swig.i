/* -*- c++ -*- */

#define AVIO505_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "avio505_swig_doc.i"

%{
#include "avio505/three_ch_multip_rtdex.h"
#include "avio505/adc_three_ch_demux_rtdex.h"
#include "avio505/sink_test.h"
#include "avio505/resta.h"
%}


%include "avio505/three_ch_multip_rtdex.h"
GR_SWIG_BLOCK_MAGIC2(avio505, three_ch_multip_rtdex);
%include "avio505/adc_three_ch_demux_rtdex.h"
GR_SWIG_BLOCK_MAGIC2(avio505, adc_three_ch_demux_rtdex);
%include "avio505/sink_test.h"
GR_SWIG_BLOCK_MAGIC2(avio505, sink_test);
%include "avio505/resta.h"
GR_SWIG_BLOCK_MAGIC2(avio505, resta);
