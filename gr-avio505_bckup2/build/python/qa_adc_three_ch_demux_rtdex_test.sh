#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/juan/cognitive/gr-avio505/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/juan/cognitive/gr-avio505/build/python:$PATH
export LD_LIBRARY_PATH=/home/juan/cognitive/gr-avio505/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/juan/cognitive/gr-avio505/build/swig:$PYTHONPATH
/usr/bin/python2 /home/juan/cognitive/gr-avio505/python/qa_adc_three_ch_demux_rtdex.py 
