#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Perseus MIMO
# Generated: Tue Oct 13 14:45:41 2015
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
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import adsb
import avio505
import nutaq
import sip
import sys

from distutils.version import StrictVersion
class perseus_mimo(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Perseus MIMO")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Perseus MIMO")
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

        self.settings = Qt.QSettings("GNU Radio", "perseus_mimo")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 20e6
        self.freq3 = freq3 = samp_rate/2/5/25
        self.freq2 = freq2 = samp_rate/20/2/20
        self.freq1 = freq1 = samp_rate/20/50
        self.decim = decim = 4
        self.Nsamples_Qtime = Nsamples_Qtime = 128

        ##################################################
        # Blocks
        ##################################################
        self._freq3_range = Range(-samp_rate/2/5, samp_rate/2/5, 100, samp_rate/2/5/25, 200)
        self._freq3_win = RangeWidget(self._freq3_range, self.set_freq3, "freq3", "counter_slider")
        self.top_layout.addWidget(self._freq3_win)
        self._freq2_range = Range(-samp_rate/20/2, samp_rate/20/2, 100, samp_rate/20/2/20, 200)
        self._freq2_win = RangeWidget(self._freq2_range, self.set_freq2, "freq2", "counter_slider")
        self.top_grid_layout.addWidget(self._freq2_win, 3,3,3,1)
        self._freq1_range = Range(-samp_rate/20/2, samp_rate/20/2, 100, samp_rate/20/50, 200)
        self._freq1_win = RangeWidget(self._freq1_range, self.set_freq1, "freq1", "counter_slider")
        self.top_grid_layout.addWidget(self._freq1_win, 3,1,3,1)
        self.qtgui_time_sink_x_0_0_2_0_0 = qtgui.time_sink_c(
        	Nsamples_Qtime, #size
        	samp_rate/5, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_2_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_2_0_0.set_y_axis(-1,  1)
        
        self.qtgui_time_sink_x_0_0_2_0_0.set_y_label("Amplitude ADSB", "")
        
        self.qtgui_time_sink_x_0_0_2_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_2_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 1, 0, 1, "")
        self.qtgui_time_sink_x_0_0_2_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_2_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_2_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_2_0_0.disable_legend()
        
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
                    self.qtgui_time_sink_x_0_0_2_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_2_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_2_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_2_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_2_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_2_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_2_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_2_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_2_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_2_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_2_0_0_win)
        self.qtgui_time_sink_x_0_0_0_0_1 = qtgui.time_sink_c(
        	Nsamples_Qtime, #size
        	samp_rate/20, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_1.set_y_axis(-1,  1)
        
        self.qtgui_time_sink_x_0_0_0_0_1.set_y_label("Amplitude DME2", "")
        
        self.qtgui_time_sink_x_0_0_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 1, 0, 1, "")
        self.qtgui_time_sink_x_0_0_0_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_0_1.disable_legend()
        
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
                    self.qtgui_time_sink_x_0_0_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_1_win)
        self.qtgui_time_sink_x_0_0_0_0_0_0_0 = qtgui.time_sink_f(
        	Nsamples_Qtime, #size
        	samp_rate/20, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_y_axis(-0.001,  0.001)
        
        self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_y_label("Amplitude DME1", "")
        
        self.qtgui_time_sink_x_0_0_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 1, 0, 1, "")
        self.qtgui_time_sink_x_0_0_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_0_0_0_0.disable_legend()
        
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
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_0_0_win)
        self.qtgui_time_sink_x_0_0_0_0_0_0 = qtgui.time_sink_c(
        	Nsamples_Qtime, #size
        	samp_rate/20, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_y_axis(-0.001,  0.001)
        
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_y_label("Amplitude DME1", "")
        
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 1, 0, 1, "")
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_0_0_0.disable_legend()
        
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
                    self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_0_win)
        self.nutaq_rtdex_source_0_0 = nutaq.rtdex_source("nutaq_carrier_perseus_0",gr.sizeof_short,1,7)
        self.nutaq_rtdex_source_0_0.set_type(0)
        self.nutaq_rtdex_source_0_0.set_packet_size(8192)
        self.nutaq_rtdex_source_0_0.set_channels("0")
        (self.nutaq_rtdex_source_0_0).set_min_output_buffer(8192)
        self.nutaq_rtdex_sink_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_0",gr.sizeof_short,1,8)
        self.nutaq_rtdex_sink_0.set_type(0)
        self.nutaq_rtdex_sink_0.set_packet_size(8192)
        self.nutaq_rtdex_sink_0.set_channels("0")
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 2, 2)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(1200e6)
        self.nutaq_radio420_tx_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_tx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0_0.set_default_band(0)
        self.nutaq_radio420_tx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-17)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(5)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain3(-4)
        self.nutaq_radio420_tx_0_0.set_default_tx_lpf_bandwidth(6)
        self.nutaq_radio420_tx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_tx_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 1, 0)
        self.nutaq_radio420_tx_0.set_default_enable(1)
        self.nutaq_radio420_tx_0.set_default_tx_freq(1e9)
        self.nutaq_radio420_tx_0.set_default_reference(0)
        self.nutaq_radio420_tx_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_tx_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0.set_default_band(0)
        self.nutaq_radio420_tx_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0.set_default_tx_vga1_gain(-17)
        self.nutaq_radio420_tx_0.set_default_tx_vga2_gain(5)
        self.nutaq_radio420_tx_0.set_default_tx_gain3(-4)
        self.nutaq_radio420_tx_0.set_default_tx_lpf_bandwidth(6)
        self.nutaq_radio420_tx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 2, 3)
        self.nutaq_radio420_rx_0_0.set_default_enable(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_freq(1200e6)
        self.nutaq_radio420_rx_0_0.set_default_reference(0)
        self.nutaq_radio420_rx_0_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_rx_0_0.set_default_band(0)
        self.nutaq_radio420_rx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_lna_gain(3)
        self.nutaq_radio420_rx_0_0.set_default_rx_vga1_gain(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain3(+18)
        self.nutaq_radio420_rx_0_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_lpf_bandwidth(6)
        self.nutaq_radio420_rx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 1, 1)
        self.nutaq_radio420_rx_0.set_default_enable(1)
        self.nutaq_radio420_rx_0.set_default_rx_freq(1e9)
        self.nutaq_radio420_rx_0.set_default_reference(0)
        self.nutaq_radio420_rx_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_0.set_default_calibrate(0)
        self.nutaq_radio420_rx_0.set_default_band(0)
        self.nutaq_radio420_rx_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0.set_default_rx_lna_gain(3)
        self.nutaq_radio420_rx_0.set_default_rx_vga1_gain(1)
        self.nutaq_radio420_rx_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain3(18)
        self.nutaq_radio420_rx_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0.set_default_rx_lpf_bandwidth(6)
        self.nutaq_radio420_rx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_custom_register_0_1_0 = nutaq.custom_register("nutaq_carrier_perseus_0",6)
        self.nutaq_custom_register_0_1_0.set_index(2)
        self.nutaq_custom_register_0_1_0.set_default_value(int((7.5e4)/samp_rate*(2**32)))
        self.nutaq_custom_register_0_1_0.set_update_rate(1)
          
        self.nutaq_custom_register_0_1 = nutaq.custom_register("nutaq_carrier_perseus_0",6)
        self.nutaq_custom_register_0_1.set_index(0)
        self.nutaq_custom_register_0_1.set_default_value(int((2e5)/samp_rate*(2**32)))
        self.nutaq_custom_register_0_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_0_0_0_3 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0_0_0_3.set_index(16)
        self.nutaq_custom_register_0_0_0_0_3.set_default_value(2500000)
        self.nutaq_custom_register_0_0_0_0_3.set_update_rate(10)
          
        self.nutaq_custom_register_0_0_0_0_2 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0_0_0_2.set_index(18)
        self.nutaq_custom_register_0_0_0_0_2.set_default_value(1)
        self.nutaq_custom_register_0_0_0_0_2.set_update_rate(10)
          
        self.nutaq_custom_register_0_0_0_0_1 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0_0_0_1.set_index(19)
        self.nutaq_custom_register_0_0_0_0_1.set_default_value(1000000)
        self.nutaq_custom_register_0_0_0_0_1.set_update_rate(10)
          
        self.nutaq_custom_register_0_0_0_0_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0_0_0_0_0.set_index(31)
        self.nutaq_custom_register_0_0_0_0_0_0.set_default_value(10000)
        self.nutaq_custom_register_0_0_0_0_0_0.set_update_rate(10)
          
        self.nutaq_custom_register_0_0_0_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0_0_0_0.set_index(30)
        self.nutaq_custom_register_0_0_0_0_0.set_default_value(10000)
        self.nutaq_custom_register_0_0_0_0_0.set_update_rate(10)
          
        self.nutaq_custom_register_0_0_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0_0_0.set_index(3)
        self.nutaq_custom_register_0_0_0_0.set_update_rate(10)
          
        self.nutaq_custom_register_0_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0_0.set_index(28)
        self.nutaq_custom_register_0_0_0.set_default_value(232)
        self.nutaq_custom_register_0_0_0.set_update_rate(10)
          
        self.nutaq_custom_register_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0.set_index(4)
        self.nutaq_custom_register_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0 = nutaq.custom_register("nutaq_carrier_perseus_0",0)
        self.nutaq_custom_register_0.set_index(1)
        self.nutaq_custom_register_0.set_default_value(6)
        self.nutaq_custom_register_0.set_update_rate(1)
          
        self.nutaq_carrier_perseus_0 = nutaq.carrier(0,"nutaq_carrier_perseus_0", "192.168.0.175")
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_int*1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.avio505_three_ch_multip_rtdex_0 = avio505.three_ch_multip_rtdex()
        self.avio505_adc_three_ch_demux_rtdex_0 = avio505.adc_three_ch_demux_rtdex()
        self.analog_sig_source_x_0_1_0 = analog.sig_source_c(samp_rate/5, analog.GR_SIN_WAVE, freq3, 0.25, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate/20, analog.GR_SIN_WAVE, freq2, 0.8, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate/20, analog.GR_SIN_WAVE, freq1, 1, 0)
        self.adsb_out_0 = adsb.out()

        ##################################################
        # Connections
        ##################################################
        self.connect((self.adsb_out_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.avio505_three_ch_multip_rtdex_0, 0))    
        self.connect((self.analog_sig_source_x_0_1, 0), (self.avio505_three_ch_multip_rtdex_0, 1))    
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.avio505_three_ch_multip_rtdex_0, 2))    
        self.connect((self.avio505_adc_three_ch_demux_rtdex_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_0, 0))    
        self.connect((self.avio505_adc_three_ch_demux_rtdex_0, 1), (self.qtgui_time_sink_x_0_0_0_0_1, 0))    
        self.connect((self.avio505_adc_three_ch_demux_rtdex_0, 2), (self.qtgui_time_sink_x_0_0_2_0_0, 0))    
        self.connect((self.avio505_three_ch_multip_rtdex_0, 0), (self.nutaq_rtdex_sink_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_0_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.adsb_out_0, 0))    
        self.connect((self.nutaq_rtdex_source_0_0, 0), (self.avio505_adc_three_ch_demux_rtdex_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "perseus_mimo")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.nutaq_custom_register_0_1_0.set_value(int((7.5e4)/self.samp_rate*(2**32)))
        self.nutaq_custom_register_0_1.set_value(int((2e5)/self.samp_rate*(2**32)))
        self.set_freq1(self.samp_rate/20/50)
        self.set_freq2(self.samp_rate/20/2/20)
        self.set_freq3(self.samp_rate/2/5/25)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate/5)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate/20)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/20)
        self.qtgui_time_sink_x_0_0_0_0_0_0_0.set_samp_rate(self.samp_rate/20)
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_samp_rate(self.samp_rate/20)
        self.qtgui_time_sink_x_0_0_2_0_0.set_samp_rate(self.samp_rate/5)
        self.qtgui_time_sink_x_0_0_0_0_1.set_samp_rate(self.samp_rate/20)

    def get_freq3(self):
        return self.freq3

    def set_freq3(self, freq3):
        self.freq3 = freq3
        self.analog_sig_source_x_0_1_0.set_frequency(self.freq3)

    def get_freq2(self):
        return self.freq2

    def set_freq2(self, freq2):
        self.freq2 = freq2
        self.analog_sig_source_x_0_1.set_frequency(self.freq2)

    def get_freq1(self):
        return self.freq1

    def set_freq1(self, freq1):
        self.freq1 = freq1
        self.analog_sig_source_x_0.set_frequency(self.freq1)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim

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
    tb = perseus_mimo()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
