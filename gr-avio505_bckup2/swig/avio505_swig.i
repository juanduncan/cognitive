/* -*- c++ -*- */

#define AVIO505_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "avio505_swig_doc.i"

%{
#include "avio505/three_ch_multip_rtdex.h"
#include "avio505/adc_three_ch_demux_rtdex.h"
#include "avio505/syncher.h"
#include "avio505/check_flux.h"
#include "avio505/resta.h"
#include "avio505/three_ch_mux_rtdex_v2.h"
%}

%include "avio505/three_ch_multip_rtdex.h"
GR_SWIG_BLOCK_MAGIC2(avio505, three_ch_multip_rtdex);
%include "avio505/adc_three_ch_demux_rtdex.h"
GR_SWIG_BLOCK_MAGIC2(avio505, adc_three_ch_demux_rtdex);

%include "avio505/syncher.h"
GR_SWIG_BLOCK_MAGIC2(avio505, syncher);
%include "avio505/check_flux.h"
GR_SWIG_BLOCK_MAGIC2(avio505, check_flux);
%include "avio505/resta.h"
GR_SWIG_BLOCK_MAGIC2(avio505, resta);
%include "avio505/three_ch_mux_rtdex_v2.h"
GR_SWIG_BLOCK_MAGIC2(avio505, three_ch_mux_rtdex_v2);
