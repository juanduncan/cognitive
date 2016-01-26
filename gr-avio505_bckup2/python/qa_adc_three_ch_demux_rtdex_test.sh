#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/nutaq/avio505_juan/gr-avio505/python
export PATH=/home/nutaq/avio505_juan/gr-avio505/python:$PATH
export LD_LIBRARY_PATH=/home/nutaq/avio505_juan/gr-avio505/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/nutaq/avio505_juan/gr-avio505/swig:$PYTHONPATH
/usr/bin/python2 /home/nutaq/avio505_juan/gr-avio505/python/qa_adc_three_ch_demux_rtdex.py 
