#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Loopback
# Generated: Mon Sep 28 13:17:12 2015
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from wifi_phy_hier import wifi_phy_hier
import foo
import ieee802_11
import math
import ofdm_80211
import pmt
import sip

from distutils.version import StrictVersion
class wifi_loopback(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Wifi Loopback")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wifi Loopback")
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

        self.settings = Qt.QSettings("GNU Radio", "wifi_loopback")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.window_size = window_size = 48
        self.sync_length = sync_length = 320
        self.snr = snr = 36
        self.samp_rate = samp_rate = 1e6
        self.pdu_length = pdu_length = 500
        self.out_buf_size = out_buf_size = 96000
        self.noise_var = noise_var = -150
        self.interval = interval = 100
        self.freq_offset = freq_offset = 0
        self.encoding = encoding = 0
        self.chan_est = chan_est = 0

        ##################################################
        # Blocks
        ##################################################
        self._snr_range = Range(-15, 50, 1, 36, 200)
        self._snr_win = RangeWidget(self._snr_range, self.set_snr, "snr", "counter_slider")
        self.top_layout.addWidget(self._snr_win)
        self._noise_var_range = Range(-180, -40, 5, -150, 200)
        self._noise_var_win = RangeWidget(self._noise_var_range, self.set_noise_var, "noise_var", "counter_slider")
        self.top_layout.addWidget(self._noise_var_win)
        self._encoding_options = [0,1,2,3,4,5,6,7]
        self._encoding_labels = ["BPSK 1/2", "BPSK 3/4", "QPSK 1/2", "QPSK 3/4", "16QAM 1/2", "16QAM 3/4", "64QAM 2/3", "64QAM 3/4"]
        self._encoding_group_box = Qt.QGroupBox("encoding")
        self._encoding_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._encoding_button_group = variable_chooser_button_group()
        self._encoding_group_box.setLayout(self._encoding_box)
        for i, label in enumerate(self._encoding_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._encoding_box.addWidget(radio_button)
        	self._encoding_button_group.addButton(radio_button, i)
        self._encoding_callback = lambda i: Qt.QMetaObject.invokeMethod(self._encoding_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._encoding_options.index(i)))
        self._encoding_callback(self.encoding)
        self._encoding_button_group.buttonClicked[int].connect(
        	lambda i: self.set_encoding(self._encoding_options[i]))
        self.top_layout.addWidget(self._encoding_group_box)
        self._chan_est_options = [0, 1]
        self._chan_est_labels = ["LMS", "Linear Comb"]
        self._chan_est_group_box = Qt.QGroupBox("chan_est")
        self._chan_est_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._chan_est_button_group = variable_chooser_button_group()
        self._chan_est_group_box.setLayout(self._chan_est_box)
        for i, label in enumerate(self._chan_est_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._chan_est_box.addWidget(radio_button)
        	self._chan_est_button_group.addButton(radio_button, i)
        self._chan_est_callback = lambda i: Qt.QMetaObject.invokeMethod(self._chan_est_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._chan_est_options.index(i)))
        self._chan_est_callback(self.chan_est)
        self._chan_est_button_group.buttonClicked[int].connect(
        	lambda i: self.set_chan_est(self._chan_est_options[i]))
        self.top_layout.addWidget(self._chan_est_group_box)
        self.wifi_phy_hier_0 = wifi_phy_hier(
            encoding=encoding,
            chan_est=chan_est,
        )
        self.sync_long = ieee802_11.ofdm_sync_long(sync_length, False, False)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	2**14, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1.set_y_label("My own sycn short", "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.05, 0, 0, "ofdm_start")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
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
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	2**15, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-0.01, 0.4)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.15, 2e-3, 2, "FISTOR")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["samples", "corr", "correlation_big", "", "",
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
        
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
                gr.sizeof_float,
                0,
                qtgui.NUM_GRAPH_HORIZ,
        	1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("nuber sync")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self._pdu_length_range = Range(0, 1500, 1, 500, 200)
        self._pdu_length_win = RangeWidget(self._pdu_length_range, self.set_pdu_length, "pdu_length", "counter_slider")
        self.top_layout.addWidget(self._pdu_length_win)
        self.marica = ofdm_80211.short_match_filter(160, 16)
        self._interval_range = Range(10, 10000, 1, 100, 200)
        self._interval_win = RangeWidget(self._interval_range, self.set_interval, "interval", "counter_slider")
        self.top_layout.addWidget(self._interval_win)
        self.ieee802_11_ofdm_parse_mac_0_0 = ieee802_11.ofdm_parse_mac(False, True)
        self.ieee802_11_ofdm_parse_mac_0 = ieee802_11.ofdm_parse_mac(False, False)
        self.ieee802_11_ofdm_mac_0 = ieee802_11.ofdm_mac(([0x23, 0x23, 0x23, 0x23, 0x23, 0x23]), ([0x42, 0x42, 0x42, 0x42, 0x42, 0x42]), ([0xff, 0xff, 0xff, 0xff, 0xff, 0xff]))
        self.ieee802_11_ofdm_equalize_symbols_0 = ieee802_11.ofdm_equalize_symbols(chan_est, False)
        self.ieee802_11_ofdm_decode_signal_0 = ieee802_11.ofdm_decode_signal(False, False)
        self.ieee802_11_ofdm_decode_mac_0 = ieee802_11.ofdm_decode_mac(False, False)
        self._freq_offset_range = Range(-0.10, 0.1, 0.0001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, "freq_offset", "slider")
        self.top_layout.addWidget(self._freq_offset_win)
        self.foo_packet_pad2_0 = foo.packet_pad2(False, False, 0.001, 500, 0)
        (self.foo_packet_pad2_0).set_min_output_buffer(96000)
        self.fft_vxx_0_1 = fft.fft_vcc(64, True, (window.rectangular(64)), True, 1)
        self.carajito = ofdm_80211.ofdm_sync_short(0.05, 2, False, False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate/2,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 64)
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.float_t, "packet_len")
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_1_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_1_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((4e9*10**(      (36-snr)   /10.0), ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((9e9, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((10**(      (snr+noise_var)   /20.0) + 1, ))
        self.blocks_message_strobe_1_0 = blocks.message_strobe(pmt.intern("HOLAabcd123456aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1234"), 1000)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_gr_complex*1, sync_length)
        self.blocks_complex_to_mag_squared_0_1_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1 = blocks.complex_to_mag_squared(1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_1_0, 'strobe'), (self.ieee802_11_ofdm_mac_0, 'app in'))    
        self.msg_connect((self.ieee802_11_ofdm_decode_mac_0, 'out'), (self.ieee802_11_ofdm_parse_mac_0_0, 'in'))    
        self.msg_connect((self.ieee802_11_ofdm_mac_0, 'phy out'), (self.wifi_phy_hier_0, 'mac_in'))    
        self.msg_connect((self.ieee802_11_ofdm_parse_mac_0_0, 'fer'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))    
        self.msg_connect((self.wifi_phy_hier_0, 'mac_out'), (self.ieee802_11_ofdm_parse_mac_0, 'in'))    
        self.connect((self.blocks_complex_to_mag_squared_0_1, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_1_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_delay_0_1, 0), (self.sync_long, 1))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.marica, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_null_source_0, 0), (self.wifi_phy_hier_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.carajito, 0), (self.blocks_delay_0_1, 0))    
        self.connect((self.carajito, 0), (self.blocks_null_sink_0_1_0_0, 0))    
        self.connect((self.carajito, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.carajito, 0), (self.sync_long, 0))    
        self.connect((self.fft_vxx_0_1, 0), (self.ieee802_11_ofdm_equalize_symbols_0, 0))    
        self.connect((self.foo_packet_pad2_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.ieee802_11_ofdm_decode_signal_0, 0), (self.ieee802_11_ofdm_decode_mac_0, 0))    
        self.connect((self.ieee802_11_ofdm_equalize_symbols_0, 0), (self.ieee802_11_ofdm_decode_signal_0, 0))    
        self.connect((self.marica, 1), (self.blocks_complex_to_mag_squared_0_1, 0))    
        self.connect((self.marica, 0), (self.blocks_complex_to_mag_squared_0_1_0, 0))    
        self.connect((self.marica, 2), (self.blocks_null_sink_0_1_0, 0))    
        self.connect((self.marica, 1), (self.carajito, 1))    
        self.connect((self.marica, 3), (self.carajito, 2))    
        self.connect((self.marica, 0), (self.carajito, 0))    
        self.connect((self.marica, 3), (self.qtgui_time_sink_x_0, 2))    
        self.connect((self.sync_long, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.wifi_phy_hier_0, 1), (self.blocks_null_sink_0_0, 0))    
        self.connect((self.wifi_phy_hier_0, 0), (self.foo_packet_pad2_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wifi_loopback")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_window_size(self):
        return self.window_size

    def set_window_size(self, window_size):
        self.window_size = window_size

    def get_sync_length(self):
        return self.sync_length

    def set_sync_length(self, sync_length):
        self.sync_length = sync_length
        self.blocks_delay_0_1.set_dly(self.sync_length)

    def get_snr(self):
        return self.snr

    def set_snr(self, snr):
        self.snr = snr
        self.blocks_multiply_const_vxx_0_0_0.set_k((4e9*10**(      (36-self.snr)   /10.0), ))
        self.blocks_multiply_const_vxx_0.set_k((10**(      (self.snr+self.noise_var)   /20.0) + 1, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/2)

    def get_pdu_length(self):
        return self.pdu_length

    def set_pdu_length(self, pdu_length):
        self.pdu_length = pdu_length

    def get_out_buf_size(self):
        return self.out_buf_size

    def set_out_buf_size(self, out_buf_size):
        self.out_buf_size = out_buf_size

    def get_noise_var(self):
        return self.noise_var

    def set_noise_var(self, noise_var):
        self.noise_var = noise_var
        self.blocks_multiply_const_vxx_0.set_k((10**(      (self.snr+self.noise_var)   /20.0) + 1, ))

    def get_interval(self):
        return self.interval

    def set_interval(self, interval):
        self.interval = interval

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_encoding(self):
        return self.encoding

    def set_encoding(self, encoding):
        self.encoding = encoding
        self._encoding_callback(self.encoding)
        self.wifi_phy_hier_0.set_encoding(self.encoding)

    def get_chan_est(self):
        return self.chan_est

    def set_chan_est(self, chan_est):
        self.chan_est = chan_est
        self._chan_est_callback(self.chan_est)
        self.wifi_phy_hier_0.set_chan_est(self.chan_est)
        self.ieee802_11_ofdm_equalize_symbols_0.set_algorithm(self.chan_est)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = wifi_loopback()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
