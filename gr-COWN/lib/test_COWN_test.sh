#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/nutaq/cognitive/gr-COWN/lib
export PATH=/home/nutaq/cognitive/gr-COWN/lib:$PATH
export LD_LIBRARY_PATH=/home/nutaq/cognitive/gr-COWN/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-COWN 
