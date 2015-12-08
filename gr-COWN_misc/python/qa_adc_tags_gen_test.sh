#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/juan/cognitive/gr-COWN_misc/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/juan/cognitive/gr-COWN_misc/python:$PATH
export LD_LIBRARY_PATH=/home/juan/cognitive/gr-COWN_misc/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/juan/cognitive/gr-COWN_misc/swig:$PYTHONPATH
/usr/bin/python2 /home/juan/cognitive/gr-COWN_misc/python/qa_adc_tags_gen.py 
