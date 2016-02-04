#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Oct  8 11:22:52 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import avio505
import sip
import sys

from distutils.version import StrictVersion
class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10000
        self.Nsamples_Qtime = Nsamples_Qtime = 128

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0_2 = qtgui.time_sink_c(
        	Nsamples_Qtime, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_2.set_y_axis(-1,  1)
        
        self.qtgui_time_sink_x_0_0_2.set_y_label("Amplitude DME 2", "")
        
        self.qtgui_time_sink_x_0_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_2.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 1, 0, 1, "")
        self.qtgui_time_sink_x_0_0_2.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_2.enable_grid(True)
        self.qtgui_time_sink_x_0_0_2.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_2.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_2_win)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_c(
        	Nsamples_Qtime, #size
        	samp_rate*4, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-1,  1)
        
        self.qtgui_time_sink_x_0_0_1.set_y_label("Amplitude ADSB", "")
        
        self.qtgui_time_sink_x_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 1, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_1.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_1_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	Nsamples_Qtime, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1,  1)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude DME1", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 1, 0, 1, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_short*1, samp_rate*12,True)
        self.blocks_short_to_float_0_2 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_interleave_0_0 = blocks.interleave(gr.sizeof_short*1, 1)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        self.blocks_float_to_complex_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_short*1, 1)
        self.avio505_three_ch_multip_rtdex_0 = avio505.three_ch_multip_rtdex()
        self.analog_sig_source_x_0_1_0 = analog.sig_source_c(samp_rate*4, analog.GR_SIN_WAVE, 1000, 1, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 400, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 400, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.avio505_three_ch_multip_rtdex_0, 0))    
        self.connect((self.analog_sig_source_x_0_1, 0), (self.avio505_three_ch_multip_rtdex_0, 1))    
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.avio505_three_ch_multip_rtdex_0, 2))    
        self.connect((self.avio505_three_ch_multip_rtdex_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_deinterleave_0, 4), (self.blocks_interleave_0, 0))    
        self.connect((self.blocks_deinterleave_0, 6), (self.blocks_interleave_0, 1))    
        self.connect((self.blocks_deinterleave_0, 8), (self.blocks_interleave_0, 2))    
        self.connect((self.blocks_deinterleave_0, 10), (self.blocks_interleave_0, 3))    
        self.connect((self.blocks_deinterleave_0, 5), (self.blocks_interleave_0_0, 0))    
        self.connect((self.blocks_deinterleave_0, 7), (self.blocks_interleave_0_0, 1))    
        self.connect((self.blocks_deinterleave_0, 9), (self.blocks_interleave_0_0, 2))    
        self.connect((self.blocks_deinterleave_0, 11), (self.blocks_interleave_0_0, 3))    
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_short_to_float_0, 0))    
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_short_to_float_0_0, 0))    
        self.connect((self.blocks_deinterleave_0, 3), (self.blocks_short_to_float_0_0_0, 0))    
        self.connect((self.blocks_deinterleave_0, 2), (self.blocks_short_to_float_0_1, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.qtgui_time_sink_x_0_0_2, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.qtgui_time_sink_x_0_0_1, 0))    
        self.connect((self.blocks_interleave_0, 0), (self.blocks_short_to_float_0_2, 0))    
        self.connect((self.blocks_interleave_0_0, 0), (self.blocks_short_to_float_0_0_1, 0))    
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_short_to_float_0_0_0, 0), (self.blocks_float_to_complex_0_0, 1))    
        self.connect((self.blocks_short_to_float_0_0_1, 0), (self.blocks_float_to_complex_0_0_0, 1))    
        self.connect((self.blocks_short_to_float_0_1, 0), (self.blocks_float_to_complex_0_0, 0))    
        self.connect((self.blocks_short_to_float_0_2, 0), (self.blocks_float_to_complex_0_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_deinterleave_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.samp_rate*4)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate*4)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*12)

    def get_Nsamples_Qtime(self):
        return self.Nsamples_Qtime

    def set_Nsamples_Qtime(self, Nsamples_Qtime):
        self.Nsamples_Qtime = Nsamples_Qtime


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
