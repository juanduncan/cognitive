#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Tx Rx
<<<<<<< HEAD
# Generated: Thu Jan 28 15:50:03 2016
=======
# Generated: Thu Jan 28 17:14:43 2016
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
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
<<<<<<< HEAD
=======
from PyQt4.QtCore import QObject, pyqtSlot
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
<<<<<<< HEAD
import ieee802_11
import ofdm_80211
=======
import COWN
import foo
import ieee802_11
import nutaq
import pmt
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
import sip
import sys


class wifi_tx_rx(gr.top_block, Qt.QWidget):

<<<<<<< HEAD
    def __init__(self):
=======
    def __init__(self, chan_est=0):
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
        gr.top_block.__init__(self, "Wifi Tx Rx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wifi Tx Rx")
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
<<<<<<< HEAD
=======

        self.settings = Qt.QSettings("GNU Radio", "wifi_tx_rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e

        self.settings = Qt.QSettings("GNU Radio", "wifi_tx_rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.window_size = window_size = 48
        self.threshold = threshold = 1000
        self.sync_length = sync_length = 320
        self.samp_rate = samp_rate = 5e5
<<<<<<< HEAD
        self.period = period = 500
        self.pdu_length = pdu_length = 30
        self.out_buf_size = out_buf_size = 96000
=======
        self.period = period = 10
        self.pdu_length = pdu_length = 30
        self.out_buf_size = out_buf_size = 96000
        self.header_formatter = header_formatter = ieee802_11.wifi_signal_field()
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
        self.freq_sin = freq_sin = 1000
        self.freq = freq = 943e6
        self.encoding = encoding = 0
        self.decimation = decimation = 40

        ##################################################
        # Blocks
        ##################################################
<<<<<<< HEAD
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
        	256, #size
=======
        self._period_range = Range(1, 10000, 1, 10, 200)
        self._period_win = RangeWidget(self._period_range, self.set_period, "period", "counter_slider", float)
        self.top_layout.addWidget(self._period_win)
        self._pdu_length_range = Range(10, 1500, 1, 30, 200)
        self._pdu_length_win = RangeWidget(self._pdu_length_range, self.set_pdu_length, "pdu_length", "counter_slider", int)
        self.top_layout.addWidget(self._pdu_length_win)
        self._encoding_options = (0, 1, 2, )
        self._encoding_labels = ("BPSK 1/2"  , "BPSK 3/4", "QPSK 1/2", )
        self._encoding_tool_bar = Qt.QToolBar(self)
        self._encoding_tool_bar.addWidget(Qt.QLabel("Encoding"+": "))
        self._encoding_combo_box = Qt.QComboBox()
        self._encoding_tool_bar.addWidget(self._encoding_combo_box)
        for label in self._encoding_labels: self._encoding_combo_box.addItem(label)
        self._encoding_callback = lambda i: Qt.QMetaObject.invokeMethod(self._encoding_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._encoding_options.index(i)))
        self._encoding_callback(self.encoding)
        self._encoding_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_encoding(self._encoding_options[i]))
        self.top_layout.addWidget(self._encoding_tool_bar)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
        	32, #size
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
        	100, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 110)
        
<<<<<<< HEAD
        self.qtgui_time_sink_x_2.set_y_label("Amplitude", "")
=======
        self.qtgui_time_sink_x_2.set_y_label("Frame error rata", "")
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
        
        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_2.disable_legend()
        
        labels = ["Packets Reveiced", "", "", "", "",
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
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
<<<<<<< HEAD
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0.99,
            qtgui.NUM_GRAPH_HORIZ,
            1
=======
        (self.qtgui_time_sink_x_2).set_processor_affinity([3])
        self.qtgui_time_sink_x_0_0_0_1_0_1 = qtgui.time_sink_c(
        	2**10, #size
        	samp_rate/1000, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_1_0_1.set_update_time(1)
        self.qtgui_time_sink_x_0_0_0_1_0_1.set_y_axis(-0.1, 1000)
        
        self.qtgui_time_sink_x_0_0_0_1_0_1.set_y_label("Generated Samples", "")
        
        self.qtgui_time_sink_x_0_0_0_1_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.001, 5e-3, 0, "FISTOR")
        self.qtgui_time_sink_x_0_0_0_1_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0_1_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0_1_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_1_0_1.disable_legend()
        
        labels = ["correlation I", "correlation Q", "correlation_big", "", "",
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
                    self.qtgui_time_sink_x_0_0_0_1_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0_1_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0_1_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_1_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_1_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_1_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_1_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_1_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_1_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_1_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_1_0_1_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
                gr.sizeof_float,
                0.99,
                qtgui.NUM_GRAPH_HORIZ,
        	1
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
        )
        self.qtgui_number_sink_0.set_update_time(0.0000010)
        self.qtgui_number_sink_0.set_title("Frame error Rata")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
<<<<<<< HEAD
                 "", "", "", "", ""]
=======
                  "", "", "", "", ""]
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 100)
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
<<<<<<< HEAD
        self._period_range = Range(1, 10000, 1, 500, 200)
        self._period_win = RangeWidget(self._period_range, self.set_period, "period", "counter_slider", float)
        self.top_layout.addWidget(self._period_win)
        self._pdu_length_range = Range(10, 1500, 1, 30, 200)
        self._pdu_length_win = RangeWidget(self._pdu_length_range, self.set_pdu_length, "pdu_length", "counter_slider", int)
        self.top_layout.addWidget(self._pdu_length_win)
        self.ofdm_80211_short_MF_v2_0 = ofdm_80211.short_MF_v2(160, 16)
        self.ieee802_11_ofdm_sync_long_0 = ieee802_11.ofdm_sync_long(sync_length, False, False)
        self.ieee802_11_ofdm_parse_mac_0 = ieee802_11.ofdm_parse_mac(False, True)
        self.ieee802_11_ofdm_equalize_symbols_0 = ieee802_11.ofdm_equalize_symbols(ieee802_11.LMS, False)
        self.ieee802_11_ofdm_decode_signal_0 = ieee802_11.ofdm_decode_signal(False, False)
        self.ieee802_11_ofdm_decode_mac_0 = ieee802_11.ofdm_decode_mac(False, False)
        self._freq_sin_range = Range(-2.5e5, 2.5e5, 500, 1000, 200)
        self._freq_sin_win = RangeWidget(self._freq_sin_range, self.set_freq_sin, "freq_sin", "counter_slider", float)
        self.top_layout.addWidget(self._freq_sin_win)
        self.fft_vxx_0 = fft.fft_vcc(64, True, (window.rectangular(64)), True, 1)
        self.carajito = ofdm_80211.ofdm_sync_short(threshold, 2, False, False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 5e5,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 64)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.float_t, "packet_len")
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((3, ))
        self.blocks_file_source_0_1_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/juan/juan/COWN/waveforms/recorded_ideal_frames_20160114_v2.bin", True)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, sync_length)
=======
        (self.qtgui_number_sink_0).set_processor_affinity([3])
        self.nutaq_rtdex_source_0 = nutaq.rtdex_source("nutaq_carrier_perseus_0",gr.sizeof_int,1,0)
        self.nutaq_rtdex_source_0.set_type(0)
        self.nutaq_rtdex_source_0.set_packet_size(8192)
        self.nutaq_rtdex_source_0.set_channels("0")
        (self.nutaq_rtdex_source_0).set_processor_affinity([1])
        self.nutaq_rtdex_sink_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_0",gr.sizeof_short,1,1)
        self.nutaq_rtdex_sink_0.set_type(0)
        self.nutaq_rtdex_sink_0.set_packet_size(8192)
        self.nutaq_rtdex_sink_0.set_channels("0")
        (self.nutaq_rtdex_sink_0).set_processor_affinity([3])
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 1, 0)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(943e6)
        self.nutaq_radio420_tx_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_tx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0_0.set_default_band(0)
        self.nutaq_radio420_tx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-15)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(5)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain3(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_lpf_bandwidth(2)
        self.nutaq_radio420_tx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 1, 1)
        self.nutaq_radio420_rx_0.set_default_enable(1)
        self.nutaq_radio420_rx_0.set_default_rx_freq(943e6)
        self.nutaq_radio420_rx_0.set_default_reference(0)
        self.nutaq_radio420_rx_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_rx_0.set_default_calibrate(0)
        self.nutaq_radio420_rx_0.set_default_band(0)
        self.nutaq_radio420_rx_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0.set_default_rx_lna_gain(3)
        self.nutaq_radio420_rx_0.set_default_rx_vga1_gain(3)
        self.nutaq_radio420_rx_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain3(3)
        self.nutaq_radio420_rx_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0.set_default_rx_lpf_bandwidth(2)
        self.nutaq_radio420_rx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_custom_register_0_2 = nutaq.custom_register("nutaq_carrier_perseus_0",4)
        self.nutaq_custom_register_0_2.set_index(0)
        self.nutaq_custom_register_0_2.set_default_value(int((4e6)/samp_rate/40*(2**32)))
        self.nutaq_custom_register_0_2.set_update_rate(1)
          
        self.nutaq_custom_register_0_1 = nutaq.custom_register("nutaq_carrier_perseus_0",4)
        self.nutaq_custom_register_0_1.set_index(2)
        self.nutaq_custom_register_0_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_0_1 = nutaq.custom_register("nutaq_carrier_perseus_0",5)
        self.nutaq_custom_register_0_0_1.set_index(3)
        self.nutaq_custom_register_0_0_1.set_default_value(7)
        self.nutaq_custom_register_0_0_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",5)
        self.nutaq_custom_register_0_0_0.set_index(6)
        self.nutaq_custom_register_0_0_0.set_default_value(600)
        self.nutaq_custom_register_0_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",5)
        self.nutaq_custom_register_0_0.set_index(4)
        self.nutaq_custom_register_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0 = nutaq.custom_register("nutaq_carrier_perseus_0",4)
        self.nutaq_custom_register_0.set_index(1)
        self.nutaq_custom_register_0.set_default_value(3)
        self.nutaq_custom_register_0.set_update_rate(1)
          
        self.nutaq_carrier_perseus_0 = nutaq.carrier(0,"nutaq_carrier_perseus_0", "192.168.0.101")
        self.ieee802_11_ofdm_sync_short_0 = ieee802_11.ofdm_sync_short(0.56, 2, False, False)
        (self.ieee802_11_ofdm_sync_short_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_sync_short_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_sync_long_0 = ieee802_11.ofdm_sync_long(sync_length, False, False)
        (self.ieee802_11_ofdm_sync_long_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_sync_long_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_parse_mac_0 = ieee802_11.ofdm_parse_mac(False, True)
        (self.ieee802_11_ofdm_parse_mac_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_parse_mac_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_mapper_0 = ieee802_11.ofdm_mapper(encoding, False)
        self.ieee802_11_ofdm_mac_0 = ieee802_11.ofdm_mac(([0x23, 0x23, 0x23, 0x23, 0x23, 0x23]), ([0x42, 0x42, 0x42, 0x42, 0x42, 0x42]), ([0xff, 0xff, 0xff, 0xff, 0xff, 255]))
        (self.ieee802_11_ofdm_mac_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_mac_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_equalize_symbols_0 = ieee802_11.ofdm_equalize_symbols(chan_est, False)
        (self.ieee802_11_ofdm_equalize_symbols_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_equalize_symbols_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_decode_signal_0 = ieee802_11.ofdm_decode_signal(False, False)
        (self.ieee802_11_ofdm_decode_signal_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_decode_signal_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_decode_mac_0 = ieee802_11.ofdm_decode_mac(False, False)
        (self.ieee802_11_ofdm_decode_mac_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_decode_mac_0).set_min_output_buffer(96000)
        self.ieee802_11_moving_average_xx_1 = ieee802_11.moving_average_ff(window_size + 16)
        (self.ieee802_11_moving_average_xx_1).set_processor_affinity([3])
        (self.ieee802_11_moving_average_xx_1).set_min_output_buffer(96000)
        self.ieee802_11_moving_average_xx_0 = ieee802_11.moving_average_cc(window_size)
        (self.ieee802_11_moving_average_xx_0).set_processor_affinity([3])
        (self.ieee802_11_moving_average_xx_0).set_min_output_buffer(96000)
        self.ieee802_11_chunks_to_symbols_xx_0 = ieee802_11.chunks_to_symbols()
        (self.ieee802_11_chunks_to_symbols_xx_0).set_min_output_buffer(96000)
        self._freq_sin_range = Range(-2.5e5, 2.5e5, 500, 1000, 200)
        self._freq_sin_win = RangeWidget(self._freq_sin_range, self.set_freq_sin, "freq_sin", "counter_slider", float)
        self.top_layout.addWidget(self._freq_sin_win)
        self.foo_packet_pad2_0_0 = foo.packet_pad2(False, False, 0.0001, 100000, 100000)
        (self.foo_packet_pad2_0_0).set_processor_affinity([3])
        (self.foo_packet_pad2_0_0).set_min_output_buffer(262144)
        self.fft_vxx_0_0 = fft.fft_vcc(64, False, (tuple([1/52**.5] * 64)), True, 1)
        (self.fft_vxx_0_0).set_min_output_buffer(96000)
        self.fft_vxx_0 = fft.fft_vcc(64, True, (window.rectangular(64)), True, 1)
        (self.fft_vxx_0).set_processor_affinity([3])
        (self.fft_vxx_0).set_min_output_buffer(96000)
        self.digital_packet_headergenerator_bb_0 = digital.packet_headergenerator_bb(header_formatter.formatter(), "packet_len")
        self.digital_ofdm_cyclic_prefixer_0_0 = digital.ofdm_cyclic_prefixer(64, 64+16, 2, "packet_len")
        (self.digital_ofdm_cyclic_prefixer_0_0).set_min_output_buffer(96000)
        self.digital_ofdm_carrier_allocator_cvc_0_0_0 = digital.ofdm_carrier_allocator_cvc(64, (range(-26, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27),), ((-21, -7, 7, 21), ), ((1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (1, 1, 1, -1), (1, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1), (-1, -1, -1, 1)), ((0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (-1.4719601443879746-1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, (1.4719601443879746+1.4719601443879746j), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (0, 0j, 0, 0j, 0, 0j, -1, 1j, -1, 1j, -1, 1j, -1, -1j, 1, 1j, 1, -1j, -1, 1j, 1, 1j, 1, 1j, 1, 1j, -1, (-0-1j), 1, -1j, -1, 1j, 0, -1j, 1, (-0-1j), 1, -1j, 1, 1j, -1, -1j, 1, (-0-1j), -1, 1j, 1, 1j, 1, 1j, 1, 1j, -1, -1j, 1, 1j, 1, -1j, -1, 0j, 0, 0j, 0, 0j), (0, 0, 0, 0, 0, 0, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 0, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 0, 0, 0, 0, 0)), "packet_len")
        (self.digital_ofdm_carrier_allocator_cvc_0_0_0).set_min_output_buffer(96000)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(([-1, 1]), 1)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, "packet_len", 1)
        (self.blocks_tagged_stream_mux_0).set_min_output_buffer(96000)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 64)
        (self.blocks_stream_to_vector_0).set_processor_affinity([3])
        (self.blocks_stream_to_vector_0).set_min_output_buffer(96000)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.float_t, "packet_len")
        (self.blocks_pdu_to_tagged_stream_0).set_processor_affinity([3])
        (self.blocks_pdu_to_tagged_stream_0).set_min_output_buffer(96000)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_int*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        (self.blocks_multiply_xx_0).set_processor_affinity([3])
        (self.blocks_multiply_xx_0).set_min_output_buffer(96000)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern("".join("x" for i in range(pdu_length)) + "1234"), period)
        (self.blocks_message_strobe_0_0).set_processor_affinity([3])
        (self.blocks_message_strobe_0_0).set_min_output_buffer(96000)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        (self.blocks_interleave_0).set_processor_affinity([3])
        self.blocks_float_to_short_0_0_0 = blocks.float_to_short(1, 2**11-1)
        (self.blocks_float_to_short_0_0_0).set_processor_affinity([3])
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 2**11-1)
        (self.blocks_float_to_short_0_0).set_processor_affinity([3])
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        (self.blocks_float_to_complex_0).set_processor_affinity([2])
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        (self.blocks_divide_xx_0).set_processor_affinity([3])
        (self.blocks_divide_xx_0).set_min_output_buffer(96000)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 16)
        (self.blocks_delay_0_0).set_processor_affinity([3])
        (self.blocks_delay_0_0).set_min_output_buffer(96000)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, sync_length)
        (self.blocks_delay_0).set_processor_affinity([3])
        (self.blocks_delay_0).set_min_output_buffer(96000)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_int*1, 1)
        (self.blocks_deinterleave_0).set_processor_affinity([1])
        (self.blocks_deinterleave_0).set_min_output_buffer(32768)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        (self.blocks_conjugate_cc_0).set_processor_affinity([3])
        (self.blocks_conjugate_cc_0).set_min_output_buffer(96000)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        (self.blocks_complex_to_mag_squared_0).set_processor_affinity([3])
        (self.blocks_complex_to_mag_squared_0).set_min_output_buffer(96000)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        (self.blocks_complex_to_mag_0).set_processor_affinity([3])
        (self.blocks_complex_to_mag_0).set_min_output_buffer(96000)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        (self.blocks_complex_to_float_0).set_processor_affinity([3])
        (self.blocks_complex_to_float_0).set_min_output_buffer(16384)
        self.COWN_syncher2_0 = COWN.syncher2()
        (self.COWN_syncher2_0).set_processor_affinity([1])
        self.COWN_resta_0 = COWN.resta()
        (self.COWN_resta_0).set_processor_affinity([1])
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e

        ##################################################
        # Connections
        ##################################################
<<<<<<< HEAD
        self.msg_connect((self.ieee802_11_ofdm_decode_mac_0, 'out'), (self.ieee802_11_ofdm_parse_mac_0, 'in'))    
        self.msg_connect((self.ieee802_11_ofdm_parse_mac_0, 'fer'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))    
        self.connect((self.blocks_delay_0, 0), (self.ieee802_11_ofdm_sync_long_0, 1))    
        self.connect((self.blocks_file_source_0_1_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.qtgui_time_sink_x_2, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.ofdm_80211_short_MF_v2_0, 0))    
        self.connect((self.carajito, 0), (self.blocks_delay_0, 0))    
        self.connect((self.carajito, 0), (self.ieee802_11_ofdm_sync_long_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.ieee802_11_ofdm_equalize_symbols_0, 0))    
        self.connect((self.ieee802_11_ofdm_decode_signal_0, 0), (self.ieee802_11_ofdm_decode_mac_0, 0))    
        self.connect((self.ieee802_11_ofdm_equalize_symbols_0, 0), (self.ieee802_11_ofdm_decode_signal_0, 0))    
        self.connect((self.ieee802_11_ofdm_sync_long_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 2), (self.blocks_null_sink_0_1, 0))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 1), (self.carajito, 1))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 3), (self.carajito, 2))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 0), (self.carajito, 0))    
=======
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.ieee802_11_ofdm_mac_0, 'app in'))    
        self.msg_connect((self.ieee802_11_ofdm_decode_mac_0, 'out'), (self.ieee802_11_ofdm_parse_mac_0, 'in'))    
        self.msg_connect((self.ieee802_11_ofdm_mac_0, 'phy out'), (self.ieee802_11_ofdm_mapper_0, 'in'))    
        self.msg_connect((self.ieee802_11_ofdm_parse_mac_0, 'fer'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))    
        self.connect((self.COWN_resta_0, 0), (self.blocks_null_sink_0_0, 0))    
        self.connect((self.COWN_syncher2_0, 0), (self.blocks_deinterleave_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.ieee802_11_moving_average_xx_1, 0))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_deinterleave_0, 3), (self.COWN_resta_0, 0))    
        self.connect((self.blocks_deinterleave_0, 2), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.ieee802_11_ofdm_sync_long_0, 1))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.ieee802_11_ofdm_sync_short_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.ieee802_11_ofdm_sync_short_0, 2))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 0))    
        self.connect((self.blocks_float_to_short_0_0_0, 0), (self.blocks_interleave_0, 1))    
        self.connect((self.blocks_interleave_0, 0), (self.nutaq_rtdex_sink_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.ieee802_11_moving_average_xx_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.qtgui_time_sink_x_2, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0_0_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_tagged_stream_mux_0, 0))    
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0_0_0, 0), (self.fft_vxx_0_0, 0))    
        self.connect((self.digital_ofdm_cyclic_prefixer_0_0, 0), (self.foo_packet_pad2_0_0, 0))    
        self.connect((self.digital_ofdm_cyclic_prefixer_0_0, 0), (self.qtgui_time_sink_x_0_0_0_1_0_1, 0))    
        self.connect((self.digital_packet_headergenerator_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.ieee802_11_ofdm_equalize_symbols_0, 0))    
        self.connect((self.fft_vxx_0_0, 0), (self.digital_ofdm_cyclic_prefixer_0_0, 0))    
        self.connect((self.foo_packet_pad2_0_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.ieee802_11_chunks_to_symbols_xx_0, 0), (self.blocks_tagged_stream_mux_0, 1))    
        self.connect((self.ieee802_11_moving_average_xx_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.ieee802_11_moving_average_xx_0, 0), (self.ieee802_11_ofdm_sync_short_0, 1))    
        self.connect((self.ieee802_11_moving_average_xx_1, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self.ieee802_11_ofdm_decode_signal_0, 0), (self.ieee802_11_ofdm_decode_mac_0, 0))    
        self.connect((self.ieee802_11_ofdm_equalize_symbols_0, 0), (self.ieee802_11_ofdm_decode_signal_0, 0))    
        self.connect((self.ieee802_11_ofdm_mapper_0, 0), (self.digital_packet_headergenerator_bb_0, 0))    
        self.connect((self.ieee802_11_ofdm_mapper_0, 0), (self.ieee802_11_chunks_to_symbols_xx_0, 0))    
        self.connect((self.ieee802_11_ofdm_sync_long_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.ieee802_11_ofdm_sync_short_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.ieee802_11_ofdm_sync_short_0, 0), (self.blocks_null_sink_0_0_0, 0))    
        self.connect((self.ieee802_11_ofdm_sync_short_0, 0), (self.ieee802_11_ofdm_sync_long_0, 0))    
        self.connect((self.nutaq_rtdex_source_0, 0), (self.COWN_syncher2_0, 0))    
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wifi_tx_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()
<<<<<<< HEAD
=======

    def get_chan_est(self):
        return self.chan_est

    def set_chan_est(self, chan_est):
        self.chan_est = chan_est
        self.ieee802_11_ofdm_equalize_symbols_0.set_algorithm(self.chan_est)
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e

    def get_window_size(self):
        return self.window_size

    def set_window_size(self, window_size):
        self.window_size = window_size
        self.ieee802_11_moving_average_xx_0.set_length(self.window_size)
        self.ieee802_11_moving_average_xx_1.set_length(self.window_size + 16)

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_sync_length(self):
        return self.sync_length

    def set_sync_length(self, sync_length):
        self.sync_length = sync_length
        self.blocks_delay_0.set_dly(self.sync_length)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
<<<<<<< HEAD
=======
        self.nutaq_custom_register_0_2.set_value(int((4e6)/self.samp_rate/40*(2**32)))
        self.qtgui_time_sink_x_0_0_0_1_0_1.set_samp_rate(self.samp_rate/1000)
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period
<<<<<<< HEAD
=======
        self.blocks_message_strobe_0_0.set_period(self.period)
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e

    def get_pdu_length(self):
        return self.pdu_length

    def set_pdu_length(self, pdu_length):
        self.pdu_length = pdu_length
<<<<<<< HEAD
=======
        self.blocks_message_strobe_0_0.set_msg(pmt.intern("".join("x" for i in range(self.pdu_length)) + "1234"))
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e

    def get_out_buf_size(self):
        return self.out_buf_size

    def set_out_buf_size(self, out_buf_size):
        self.out_buf_size = out_buf_size

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter
        self.digital_packet_headergenerator_bb_0.set_header_formatter(self.header_formatter.formatter())

    def get_freq_sin(self):
        return self.freq_sin

    def set_freq_sin(self, freq_sin):
        self.freq_sin = freq_sin

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_encoding(self):
        return self.encoding

    def set_encoding(self, encoding):
        self.encoding = encoding
        self._encoding_callback(self.encoding)
        self.ieee802_11_ofdm_mapper_0.set_encoding(self.encoding)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = wifi_tx_rx()
<<<<<<< HEAD
    tb.start(16384)
=======
    tb.start()
>>>>>>> b19f946300deb8819390f5fab6a8ed8f5788db9e
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
