#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Tx
# Generated: Wed Nov 11 13:57:46 2015
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
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from wifi_phy_hier import wifi_phy_hier  # grc-generated hier_block
import ieee802_11
import nutaq
import pmt


class wifi_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Wifi Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wifi Tx")
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

        self.settings = Qt.QSettings("GNU Radio", "wifi_tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 10
        self.samp_rate = samp_rate = 500000
        self.period = period = 1000
        self.pdu_length = pdu_length = 100
        self.packet_size = packet_size = 1024
        self.out_buf_size = out_buf_size = 96000
        self.mult_gaussian = mult_gaussian = 0.01
        self.mult = mult = 0.5
        self.lo_offset = lo_offset = 0
        self.freq_cos = freq_cos = 50000
        self.encoding = encoding = 0
        self.decimation = decimation = 40
        self.amplitude = amplitude = 0.125
        self.RF_freq_0 = RF_freq_0 = 943e6
        self.RF_freq = RF_freq = 943e6
        self.PSD_averaging = PSD_averaging = 600

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_options = (500000, 1000000, 2000000, )
        self._samp_rate_labels = ('500KHz', '1MHz', '2MHz', )
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
        self._period_range = Range(1, 10000, 1, 1000, 200)
        self._period_win = RangeWidget(self._period_range, self.set_period, "period", "counter_slider", float)
        self.top_layout.addWidget(self._period_win)
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
        self.wifi_phy_hier_0 = wifi_phy_hier(
            chan_est=0,
            encoding=encoding,
        )
        self._tx_gain_range = Range(0, 100, 1, 10, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, "tx_gain", "counter_slider", float)
        self.top_layout.addWidget(self._tx_gain_win)
        self._pdu_length_range = Range(0, 1500, 1, 100, 200)
        self._pdu_length_win = RangeWidget(self._pdu_length_range, self.set_pdu_length, "pdu_length", "counter_slider", float)
        self.top_layout.addWidget(self._pdu_length_win)
        self.nutaq_rtdex_sink_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_TX",gr.sizeof_short,1,1)
        self.nutaq_rtdex_sink_0.set_type(0)
        self.nutaq_rtdex_sink_0.set_packet_size(packet_size)
        self.nutaq_rtdex_sink_0.set_channels("1")
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_TX", 2, 1)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(RF_freq)
        self.nutaq_radio420_tx_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_tx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0_0.set_default_band(1)
        self.nutaq_radio420_tx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-10)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(15)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain3(3)
        self.nutaq_radio420_tx_0_0.set_default_tx_lpf_bandwidth(2)
        self.nutaq_radio420_tx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_tx_0 = nutaq.radio420_tx("nutaq_carrier_perseus_TX", 1, 0)
        self.nutaq_radio420_tx_0.set_default_enable(1)
        self.nutaq_radio420_tx_0.set_default_tx_freq(RF_freq)
        self.nutaq_radio420_tx_0.set_default_reference(0)
        self.nutaq_radio420_tx_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_tx_0.set_default_calibrate(1)
        self.nutaq_radio420_tx_0.set_default_band(0)
        self.nutaq_radio420_tx_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0.set_default_tx_vga1_gain(-5)
        self.nutaq_radio420_tx_0.set_default_tx_vga2_gain(25)
        self.nutaq_radio420_tx_0.set_default_tx_gain3(10)
        self.nutaq_radio420_tx_0.set_default_tx_lpf_bandwidth(2)
        self.nutaq_radio420_tx_0.set_default_ref_clk_ctrl(1)
        self.nutaq_radio420_tx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0_0 = nutaq.radio420_rx("nutaq_carrier_perseus_TX", 2, 3)
        self.nutaq_radio420_rx_0_0.set_default_enable(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_freq(RF_freq)
        self.nutaq_radio420_rx_0_0.set_default_reference(0)
        self.nutaq_radio420_rx_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_rx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_rx_0_0.set_default_band(0)
        self.nutaq_radio420_rx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_vga1_gain(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain3(-8)
        self.nutaq_radio420_rx_0_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_lpf_bandwidth(2)
        self.nutaq_radio420_rx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0 = nutaq.radio420_rx("nutaq_carrier_perseus_TX", 1, 2)
        self.nutaq_radio420_rx_0.set_default_enable(1)
        self.nutaq_radio420_rx_0.set_default_rx_freq(RF_freq)
        self.nutaq_radio420_rx_0.set_default_reference(0)
        self.nutaq_radio420_rx_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_rx_0.set_default_calibrate(0)
        self.nutaq_radio420_rx_0.set_default_band(0)
        self.nutaq_radio420_rx_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0.set_default_rx_vga1_gain(2)
        self.nutaq_radio420_rx_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain3(-8)
        self.nutaq_radio420_rx_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0.set_default_rx_lpf_bandwidth(2)
        self.nutaq_radio420_rx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_custom_register_0_1_1 = nutaq.custom_register("nutaq_carrier_perseus_TX",9)
        self.nutaq_custom_register_0_1_1.set_index(6)
        self.nutaq_custom_register_0_1_1.set_default_value(PSD_averaging)
        self.nutaq_custom_register_0_1_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_1_0 = nutaq.custom_register("nutaq_carrier_perseus_TX",7)
        self.nutaq_custom_register_0_1_0.set_index(2)
        self.nutaq_custom_register_0_1_0.set_update_rate(1)
          
        self.nutaq_custom_register_0_1 = nutaq.custom_register("nutaq_carrier_perseus_TX",36)
        self.nutaq_custom_register_0_1.set_index(0)
        self.nutaq_custom_register_0_1.set_default_value(int((4e6)/samp_rate/40*(2**32)))
        self.nutaq_custom_register_0_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_0_0 = nutaq.custom_register("nutaq_carrier_perseus_TX",8)
        self.nutaq_custom_register_0_0_0.set_index(3)
        self.nutaq_custom_register_0_0_0.set_default_value(7)
        self.nutaq_custom_register_0_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0_0 = nutaq.custom_register("nutaq_carrier_perseus_TX",5)
        self.nutaq_custom_register_0_0.set_index(4)
        self.nutaq_custom_register_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0 = nutaq.custom_register("nutaq_carrier_perseus_TX",1)
        self.nutaq_custom_register_0.set_index(1)
        self.nutaq_custom_register_0.set_default_value(3)
        self.nutaq_custom_register_0.set_update_rate(0.01)
          
        self.nutaq_carrier_perseus_TX = nutaq.carrier(0,"nutaq_carrier_perseus_TX", "192.168.0.103")
        self._mult_gaussian_range = Range(0, 1, 0.001, 0.01, 200)
        self._mult_gaussian_win = RangeWidget(self._mult_gaussian_range, self.set_mult_gaussian, "mult_gaussian", "counter_slider", float)
        self.top_layout.addWidget(self._mult_gaussian_win)
        self._mult_range = Range(0, 2, 0.001, 0.5, 200)
        self._mult_win = RangeWidget(self._mult_range, self.set_mult, "mult", "counter_slider", float)
        self.top_layout.addWidget(self._mult_win)
        self._lo_offset_options = (0, 6e6, 11e6, )
        self._lo_offset_labels = ("'0 MHz',", "'6 MHz',", '11 MHz', )
        self._lo_offset_tool_bar = Qt.QToolBar(self)
        self._lo_offset_tool_bar.addWidget(Qt.QLabel("LO offset"+": "))
        self._lo_offset_combo_box = Qt.QComboBox()
        self._lo_offset_tool_bar.addWidget(self._lo_offset_combo_box)
        for label in self._lo_offset_labels: self._lo_offset_combo_box.addItem(label)
        self._lo_offset_callback = lambda i: Qt.QMetaObject.invokeMethod(self._lo_offset_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._lo_offset_options.index(i)))
        self._lo_offset_callback(self.lo_offset)
        self._lo_offset_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_lo_offset(self._lo_offset_options[i]))
        self.top_layout.addWidget(self._lo_offset_tool_bar)
        self.ieee802_11_ofdm_mac_0 = ieee802_11.ofdm_mac(([0x23, 0x23, 0x23, 0x23, 0x23, 0x23]), ([0x42, 0x42, 0x42, 0x42, 0x42, 0x42]), ([0xff, 0xff, 0xff, 0xff, 0xff, 255]))
        self._freq_cos_range = Range(-250000, 250000, 1, 50000, 200)
        self._freq_cos_win = RangeWidget(self._freq_cos_range, self.set_freq_cos, "freq_cos", "counter_slider", float)
        self.top_layout.addWidget(self._freq_cos_win)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_message_strobe_0_0_0 = blocks.message_strobe(pmt.intern("Hello BBBBBBBBBBBB1234"), period)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        self.blocks_float_to_short_0_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/juan/Desktop/waveforms/fmcw_chirp_80pc.bin", True)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        (self.blocks_complex_to_float_0).set_min_output_buffer(8192)
        (self.blocks_complex_to_float_0).set_max_output_buffer(8192)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0_0_0, 'strobe'), (self.ieee802_11_ofdm_mac_0, 'app in'))    
        self.msg_connect((self.ieee802_11_ofdm_mac_0, 'phy out'), (self.wifi_phy_hier_0, 'mac_in'))    
        self.msg_connect((self.wifi_phy_hier_0, 'mac_out'), (self.ieee802_11_ofdm_mac_0, 'phy in'))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 0))    
        self.connect((self.blocks_float_to_short_0_0_0, 0), (self.blocks_interleave_0, 1))    
        self.connect((self.blocks_interleave_0, 0), (self.nutaq_rtdex_sink_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.wifi_phy_hier_0, 0))    
        self.connect((self.wifi_phy_hier_0, 1), (self.blocks_null_sink_0, 0))    
        self.connect((self.wifi_phy_hier_0, 0), (self.blocks_null_sink_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wifi_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self._samp_rate_callback(self.samp_rate)
        self.nutaq_custom_register_0_1.set_value(int((4e6)/self.samp_rate/40*(2**32)))
        self.nutaq_custom_register_0_1_0.set_value(int(0e6/self.samp_rate/40*(2**32)))

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period
        self.blocks_message_strobe_0_0_0.set_period(self.period)

    def get_pdu_length(self):
        return self.pdu_length

    def set_pdu_length(self, pdu_length):
        self.pdu_length = pdu_length

    def get_packet_size(self):
        return self.packet_size

    def set_packet_size(self, packet_size):
        self.packet_size = packet_size

    def get_out_buf_size(self):
        return self.out_buf_size

    def set_out_buf_size(self, out_buf_size):
        self.out_buf_size = out_buf_size

    def get_mult_gaussian(self):
        return self.mult_gaussian

    def set_mult_gaussian(self, mult_gaussian):
        self.mult_gaussian = mult_gaussian

    def get_mult(self):
        return self.mult

    def set_mult(self, mult):
        self.mult = mult

    def get_lo_offset(self):
        return self.lo_offset

    def set_lo_offset(self, lo_offset):
        self.lo_offset = lo_offset
        self._lo_offset_callback(self.lo_offset)

    def get_freq_cos(self):
        return self.freq_cos

    def set_freq_cos(self, freq_cos):
        self.freq_cos = freq_cos

    def get_encoding(self):
        return self.encoding

    def set_encoding(self, encoding):
        self.encoding = encoding
        self._encoding_callback(self.encoding)
        self.wifi_phy_hier_0.set_encoding(self.encoding)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude

    def get_RF_freq_0(self):
        return self.RF_freq_0

    def set_RF_freq_0(self, RF_freq_0):
        self.RF_freq_0 = RF_freq_0

    def get_RF_freq(self):
        return self.RF_freq

    def set_RF_freq(self, RF_freq):
        self.RF_freq = RF_freq
        self.nutaq_radio420_rx_0.set_rx_gain(-8)
        self.nutaq_radio420_rx_0.set_rx_freq(self.RF_freq)
          
        self.nutaq_radio420_rx_0_0.set_rx_gain(-8)
        self.nutaq_radio420_rx_0_0.set_rx_freq(self.RF_freq)
          
        self.nutaq_radio420_tx_0.set_tx_gain(10)
        self.nutaq_radio420_tx_0.set_tx_freq(self.RF_freq)
          
        self.nutaq_radio420_tx_0_0.set_tx_gain(3)
        self.nutaq_radio420_tx_0_0.set_tx_freq(self.RF_freq)
          

    def get_PSD_averaging(self):
        return self.PSD_averaging

    def set_PSD_averaging(self, PSD_averaging):
        self.PSD_averaging = PSD_averaging
        self.nutaq_custom_register_0_1_1.set_value(self.PSD_averaging)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = wifi_tx()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
