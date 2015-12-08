#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/juan/cognitive/gr-avio505/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/juan/cognitive/gr-avio505/lib:$PATH
export LD_LIBRARY_PATH=/home/juan/cognitive/gr-avio505/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-avio505 
