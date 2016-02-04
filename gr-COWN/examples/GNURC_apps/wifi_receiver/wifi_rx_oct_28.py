#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Rx Oct 28
# Generated: Mon Nov 16 20:35:30 2015
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
import ieee802_11
import nutaq
import ofdm_80211
import sip
import sys

from distutils.version import StrictVersion
class wifi_rx_oct_28(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Wifi Rx Oct 28")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wifi Rx Oct 28")
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

        self.settings = Qt.QSettings("GNU Radio", "wifi_rx_oct_28")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.window_size = window_size = 48
        self.threshold = threshold = 1000
        self.sync_length = sync_length = 320
        self.samp_rate = samp_rate = 0.25e6
        self.lo_offset = lo_offset = 0
        self.gain = gain = 20
        self.freq = freq = 943000000.0
        self.decimation = decimation = 40
        self.chan_est = chan_est = 1

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_options = [0.25e6, 1e6, 5e6, 10e6, 20e6]
        self._samp_rate_labels = ["500 KHz",  "1 MHz",  "5 MHz", "10 MHz", "20 MHz"]
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel("Sample Rate"+": "))
        self._samp_rate_combo_box = Qt.QComboBox()
        self._samp_rate_tool_bar.addWidget(self._samp_rate_combo_box)
        for label in self._samp_rate_labels: self._samp_rate_combo_box.addItem(label)
        self._samp_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._samp_rate_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._samp_rate_options.index(i)))
        self._samp_rate_callback(self.samp_rate)
        self._samp_rate_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_samp_rate(self._samp_rate_options[i]))
        self.top_layout.addWidget(self._samp_rate_tool_bar)
        self.qtgui_time_sink_x_0_0_0_1 = qtgui.time_sink_c(
        	2**13, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_1.set_y_axis(-0.8, 0.8)
        
        self.qtgui_time_sink_x_0_0_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, threshold, 0.25e-3, 0, "BAD TAG")
        self.qtgui_time_sink_x_0_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_1.disable_legend()
        
        labels = ["I", "Q", "correlation_big", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1, 1, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_1_win)
        self.ofdm_80211_short_MF_v2_0 = ofdm_80211.short_MF_v2(160, 16)
        self.ofdm_80211_adc_tags_gen_0 = ofdm_80211.adc_tags_gen()
        self.nutaq_rtdex_source_0 = nutaq.rtdex_source("nutaq_carrier_perseus_0",gr.sizeof_float,1,0)
        self.nutaq_rtdex_source_0.set_type(0)
        self.nutaq_rtdex_source_0.set_packet_size(8192)
        self.nutaq_rtdex_source_0.set_channels("0")
        (self.nutaq_rtdex_source_0).set_min_output_buffer(16384)
        (self.nutaq_rtdex_source_0).set_max_output_buffer(32768)
        self.nutaq_rtdex_sink_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_0",gr.sizeof_short,1,1)
        self.nutaq_rtdex_sink_0.set_type(0)
        self.nutaq_rtdex_sink_0.set_packet_size(8192)
        self.nutaq_rtdex_sink_0.set_channels("0")
        self.nutaq_radio420_tx_0_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 2, 2)
        self.nutaq_radio420_tx_0_0_0.set_default_enable(0)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_freq(943e6)
        self.nutaq_radio420_tx_0_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_tx_0_0_0.set_default_calibrate(1)
        self.nutaq_radio420_tx_0_0_0.set_default_band(0)
        self.nutaq_radio420_tx_0_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_vga1_gain(-10)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_vga2_gain(15)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_gain3(3)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_lpf_bandwidth(6)
        self.nutaq_radio420_tx_0_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 1, 0)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(943e6)
        self.nutaq_radio420_tx_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_tx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0_0.set_default_band(0)
        self.nutaq_radio420_tx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-10)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(15)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain3(3)
        self.nutaq_radio420_tx_0_0.set_default_tx_lpf_bandwidth(6)
        self.nutaq_radio420_tx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 2, 3)
        self.nutaq_radio420_rx_0_0.set_default_enable(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_freq(943e6)
        self.nutaq_radio420_rx_0_0.set_default_reference(0)
        self.nutaq_radio420_rx_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_rx_0_0.set_default_calibrate(1)
        self.nutaq_radio420_rx_0_0.set_default_band(0)
        self.nutaq_radio420_rx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_lna_gain(3)
        self.nutaq_radio420_rx_0_0.set_default_rx_vga1_gain(3)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain2(4)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain3(8)
        self.nutaq_radio420_rx_0_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_lpf_bandwidth(2)
        self.nutaq_radio420_rx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 1, 1)
        self.nutaq_radio420_rx_0.set_default_enable(0)
        self.nutaq_radio420_rx_0.set_default_rx_freq(943e6)
        self.nutaq_radio420_rx_0.set_default_reference(0)
        self.nutaq_radio420_rx_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_rx_0.set_default_calibrate(1)
        self.nutaq_radio420_rx_0.set_default_band(0)
        self.nutaq_radio420_rx_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0.set_default_rx_vga1_gain(1)
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
          
        self.nutaq_carrier_perseus_0 = nutaq.carrier(0,"nutaq_carrier_perseus_0", "192.168.0.102")
        self.ieee802_11_ofdm_sync_long_0 = ieee802_11.ofdm_sync_long(sync_length, False, False)
        self.ieee802_11_ofdm_parse_mac_0 = ieee802_11.ofdm_parse_mac(False, True)
        self.ieee802_11_ofdm_equalize_symbols_0 = ieee802_11.ofdm_equalize_symbols(ieee802_11.LMS, False)
        self.ieee802_11_ofdm_decode_signal_0 = ieee802_11.ofdm_decode_signal(False, False)
        self.ieee802_11_ofdm_decode_mac_0 = ieee802_11.ofdm_decode_mac(False, True)
        self._gain_range = Range(0, 100, 1, 20, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "gain", "slider")
        self.top_layout.addWidget(self._gain_win)
        self._freq_options = [943000000.0, 2412000000.0, 2417000000.0, 2422000000.0, 2427000000.0, 2432000000.0, 2437000000.0, 2442000000.0, 2447000000.0, 2452000000.0, 2457000000.0, 2462000000.0, 2467000000.0, 2472000000.0, 2484000000.0, 5170000000.0, 5180000000.0, 5190000000.0, 5200000000.0, 5210000000.0, 5220000000.0, 5230000000.0, 5240000000.0, 5260000000.0, 5280000000.0, 5300000000.0, 5320000000.0, 5500000000.0, 5520000000.0, 5540000000.0, 5560000000.0, 5580000000.0, 5600000000.0, 5620000000.0, 5640000000.0, 5660000000.0, 5680000000.0, 5700000000.0, 5745000000.0, 5765000000.0, 5785000000.0, 5805000000.0, 5825000000.0, 5860000000.0, 5870000000.0, 5880000000.0, 5890000000.0, 5900000000.0, 5910000000.0, 5920000000.0]
        self._freq_labels = ['  0 | 943.0 | ??', '  1 | 2412.0 | 11g', '  2 | 2417.0 | 11g', '  3 | 2422.0 | 11g', '  4 | 2427.0 | 11g', '  5 | 2432.0 | 11g', '  6 | 2437.0 | 11g', '  7 | 2442.0 | 11g', '  8 | 2447.0 | 11g', '  9 | 2452.0 | 11g', ' 10 | 2457.0 | 11g', ' 11 | 2462.0 | 11g', ' 12 | 2467.0 | 11g', ' 13 | 2472.0 | 11g', ' 14 | 2484.0 | 11g', ' 34 | 5170.0 | 11a', ' 36 | 5180.0 | 11a', ' 38 | 5190.0 | 11a', ' 40 | 5200.0 | 11a', ' 42 | 5210.0 | 11a', ' 44 | 5220.0 | 11a', ' 46 | 5230.0 | 11a', ' 48 | 5240.0 | 11a', ' 52 | 5260.0 | 11a', ' 56 | 5280.0 | 11a', ' 58 | 5300.0 | 11a', ' 60 | 5320.0 | 11a', '100 | 5500.0 | 11a', '104 | 5520.0 | 11a', '108 | 5540.0 | 11a', '112 | 5560.0 | 11a', '116 | 5580.0 | 11a', '120 | 5600.0 | 11a', '124 | 5620.0 | 11a', '128 | 5640.0 | 11a', '132 | 5660.0 | 11a', '136 | 5680.0 | 11a', '140 | 5700.0 | 11a', '149 | 5745.0 | 11a', '153 | 5765.0 | 11a', '157 | 5785.0 | 11a', '161 | 5805.0 | 11a', '165 | 5825.0 | 11a', '172 | 5860.0 | 11p', '174 | 5870.0 | 11p', '176 | 5880.0 | 11p', '178 | 5890.0 | 11p', '180 | 5900.0 | 11p', '182 | 5910.0 | 11p', '184 | 5920.0 | 11p']
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_tool_bar.addWidget(Qt.QLabel("Channel"+": "))
        self._freq_combo_box = Qt.QComboBox()
        self._freq_tool_bar.addWidget(self._freq_combo_box)
        for label in self._freq_labels: self._freq_combo_box.addItem(label)
        self._freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._freq_options.index(i)))
        self._freq_callback(self.freq)
        self._freq_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_freq(self._freq_options[i]))
        self.top_layout.addWidget(self._freq_tool_bar)
        self.fft_vxx_0 = fft.fft_vcc(64, True, (window.rectangular(64)), True, 1)
        self.carajito = ofdm_80211.ofdm_sync_short(threshold, 2, False, False)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 64)
        self.blocks_null_sink_0_1_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        self.blocks_float_to_short_0_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/juan/transmiter/waveforms/fmcw_chirp_80pc.bin", True)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_float*1, 1)
        (self.blocks_delay_2).set_min_output_buffer(16384)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, sync_length)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        (self.blocks_complex_to_float_0).set_min_output_buffer(8192)
        (self.blocks_complex_to_float_0).set_max_output_buffer(8192)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.ieee802_11_ofdm_decode_mac_0, 'out'), (self.ieee802_11_ofdm_parse_mac_0, 'in'))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.ieee802_11_ofdm_sync_long_0, 1))    
        self.connect((self.blocks_delay_2, 0), (self.ofdm_80211_adc_tags_gen_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 0))    
        self.connect((self.blocks_float_to_short_0_0_0, 0), (self.blocks_interleave_0, 1))    
        self.connect((self.blocks_interleave_0, 0), (self.nutaq_rtdex_sink_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.carajito, 0), (self.blocks_delay_0, 0))    
        self.connect((self.carajito, 0), (self.ieee802_11_ofdm_sync_long_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.ieee802_11_ofdm_equalize_symbols_0, 0))    
        self.connect((self.ieee802_11_ofdm_decode_signal_0, 0), (self.ieee802_11_ofdm_decode_mac_0, 0))    
        self.connect((self.ieee802_11_ofdm_equalize_symbols_0, 0), (self.ieee802_11_ofdm_decode_signal_0, 0))    
        self.connect((self.ieee802_11_ofdm_sync_long_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.nutaq_rtdex_source_0, 0), (self.blocks_delay_2, 0))    
        self.connect((self.ofdm_80211_adc_tags_gen_0, 0), (self.ofdm_80211_short_MF_v2_0, 0))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 2), (self.blocks_null_sink_0_1_0_0, 0))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 0), (self.carajito, 0))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 1), (self.carajito, 1))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 3), (self.carajito, 2))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 0), (self.qtgui_time_sink_x_0_0_0_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wifi_rx_oct_28")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_window_size(self):
        return self.window_size

    def set_window_size(self, window_size):
        self.window_size = window_size

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
        self.nutaq_custom_register_0_2.set_value(int((4e6)/self.samp_rate/40*(2**32)))
        self.qtgui_time_sink_x_0_0_0_1.set_samp_rate(self.samp_rate)
        self._samp_rate_callback(self.samp_rate)

    def get_lo_offset(self):
        return self.lo_offset

    def set_lo_offset(self, lo_offset):
        self.lo_offset = lo_offset

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_callback(self.freq)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation

    def get_chan_est(self):
        return self.chan_est

    def set_chan_est(self, chan_est):
        self.chan_est = chan_est


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = wifi_rx_oct_28()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
