#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/nutaq/avio505_juan/gr-avio505/lib
export PATH=/home/nutaq/avio505_juan/gr-avio505/lib:$PATH
export LD_LIBRARY_PATH=/home/nutaq/avio505_juan/gr-avio505/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-avio505 
