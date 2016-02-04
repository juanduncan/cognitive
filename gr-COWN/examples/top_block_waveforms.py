#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block Waveforms
# Generated: Tue Feb  2 23:33:11 2016
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
from wifi_PHY_tx_hier import wifi_PHY_tx_hier  # grc-generated hier_block
import COWN
import ieee802_11
import nutaq
import ofdm_80211
import pmt
import sip


class top_block_waveforms(gr.top_block, Qt.QWidget):

    def __init__(self, chan_est=0):
        gr.top_block.__init__(self, "Top Block Waveforms")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block Waveforms")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block_waveforms")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.chan_est = chan_est

        ##################################################
        # Variables
        ##################################################
        self.window_size = window_size = 48
        self.threshold = threshold = 1000
        self.sync_length = sync_length = 320
        self.samp_rate = samp_rate = 5e5
        self.period = period = 300
        self.pdu_length = pdu_length = 1000
        self.out_buf_size = out_buf_size = 96000
        self.freq_sin = freq_sin = 1000
        self.freq = freq = 943e6
        self.decimation = decimation = 40

        ##################################################
        # Blocks
        ##################################################
        self._period_range = Range(1, 10000, 1, 300, 200)
        self._period_win = RangeWidget(self._period_range, self.set_period, "period", "counter_slider", float)
        self.top_layout.addWidget(self._period_win)
        self._pdu_length_range = Range(10, 1500, 1, 1000, 200)
        self._pdu_length_win = RangeWidget(self._pdu_length_range, self.set_pdu_length, "pdu_length", "counter_slider", int)
        self.top_layout.addWidget(self._pdu_length_win)
        self.wifi_PHY_tx_hier_1 = wifi_PHY_tx_hier(
            chan_est=1,
            encoding=ieee802_11.BPSK_1_2,
        )
        (self.wifi_PHY_tx_hier_1).set_min_output_buffer(262144)
        self.qtgui_time_sink_x_2_0 = qtgui.time_sink_f(
        	128, #size
        	100, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0.set_y_axis(-1, 110)
        
        self.qtgui_time_sink_x_2_0.set_y_label("Frame error rata", "")
        
        self.qtgui_time_sink_x_2_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_2_0.enable_grid(True)
        self.qtgui_time_sink_x_2_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_2_0.disable_legend()
        
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
                self.qtgui_time_sink_x_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_0_win)
        (self.qtgui_time_sink_x_2_0).set_processor_affinity([3])
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	64, #size
        	1, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.050)
        self.qtgui_time_sink_x_1.set_y_axis(-20, 20)
        
        self.qtgui_time_sink_x_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, False)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.5, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 0, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
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
        self.qtgui_time_sink_x_0_0_0_1 = qtgui.time_sink_c(
        	2**16, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_1.set_y_axis(-0.1, 1000)
        
        self.qtgui_time_sink_x_0_0_0_1.set_y_label("Received Samples", "")
        
        self.qtgui_time_sink_x_0_0_0_1.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.05, 5e-3, 0, "FISTOR")
        self.qtgui_time_sink_x_0_0_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_1.disable_legend()
        
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
        (self.ofdm_80211_short_MF_v2_0).set_processor_affinity([2])
        (self.ofdm_80211_short_MF_v2_0).set_min_output_buffer(131072)
        self.nutaq_rtdex_source_0 = nutaq.rtdex_source("nutaq_carrier_perseus_0",gr.sizeof_int,1,0)
        self.nutaq_rtdex_source_0.set_type(0)
        self.nutaq_rtdex_source_0.set_packet_size(8600)
        self.nutaq_rtdex_source_0.set_channels("0")
        (self.nutaq_rtdex_source_0).set_min_output_buffer(2048)
        self.nutaq_rtdex_sink_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_0",gr.sizeof_short,1,1)
        self.nutaq_rtdex_sink_0.set_type(0)
        self.nutaq_rtdex_sink_0.set_packet_size(8192)
        self.nutaq_rtdex_sink_0.set_channels("0")
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 1, 0)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(943e6)
        self.nutaq_radio420_tx_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_tx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0_0.set_default_band(0)
        self.nutaq_radio420_tx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-20)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(0)
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
          
        self.nutaq_carrier_perseus_0 = nutaq.carrier(0,"nutaq_carrier_perseus_0", "192.168.0.102")
        self.ieee802_11_ofdm_sync_long_0 = ieee802_11.ofdm_sync_long(sync_length, False, False)
        (self.ieee802_11_ofdm_sync_long_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_sync_long_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_parse_mac_0 = ieee802_11.ofdm_parse_mac(False, True)
        (self.ieee802_11_ofdm_parse_mac_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_parse_mac_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_mac_0 = ieee802_11.ofdm_mac(([0x23, 0x23, 0x23, 0x23, 0x23, 0x23]), ([0x42, 0x42, 0x42, 0x42, 0x42, 0x42]), ([0xff, 0xff, 0xff, 0xff, 0xff, 255]))
        self.ieee802_11_ofdm_equalize_symbols_0 = ieee802_11.ofdm_equalize_symbols(chan_est, False)
        (self.ieee802_11_ofdm_equalize_symbols_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_equalize_symbols_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_decode_signal_0 = ieee802_11.ofdm_decode_signal(False, False)
        (self.ieee802_11_ofdm_decode_signal_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_decode_signal_0).set_min_output_buffer(96000)
        self.ieee802_11_ofdm_decode_mac_0 = ieee802_11.ofdm_decode_mac(False, False)
        (self.ieee802_11_ofdm_decode_mac_0).set_processor_affinity([3])
        (self.ieee802_11_ofdm_decode_mac_0).set_min_output_buffer(96000)
        self._freq_sin_range = Range(-2.5e5, 2.5e5, 500, 1000, 200)
        self._freq_sin_win = RangeWidget(self._freq_sin_range, self.set_freq_sin, "freq_sin", "counter_slider", float)
        self.top_layout.addWidget(self._freq_sin_win)
        self.fft_vxx_0 = fft.fft_vcc(64, True, (window.rectangular(64)), True, 1)
        (self.fft_vxx_0).set_processor_affinity([3])
        (self.fft_vxx_0).set_min_output_buffer(96000)
        self.carajito = ofdm_80211.ofdm_sync_short(threshold, 2, False, False)
        (self.carajito).set_processor_affinity([2])
        (self.carajito).set_min_output_buffer(131072)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 64)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 64)
        (self.blocks_stream_to_vector_0).set_processor_affinity([3])
        (self.blocks_stream_to_vector_0).set_min_output_buffer(96000)
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.float_t, "packet_len")
        (self.blocks_pdu_to_tagged_stream_0_0).set_processor_affinity([3])
        (self.blocks_pdu_to_tagged_stream_0_0).set_min_output_buffer(96000)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern("Hello__" +"".join("x" for i in range(pdu_length)) + "1234"), period)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        (self.blocks_interleave_0).set_min_output_buffer(262144)
        self.blocks_float_to_short_0_0_0 = blocks.float_to_short(1, 2**8-1)
        (self.blocks_float_to_short_0_0_0).set_min_output_buffer(262144)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 2**8-1)
        (self.blocks_float_to_short_0_0).set_min_output_buffer(262144)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, sync_length)
        (self.blocks_delay_0).set_processor_affinity([3])
        (self.blocks_delay_0).set_min_output_buffer(96000)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_int*1, 1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        (self.blocks_complex_to_float_0).set_min_output_buffer(262144)
        self.COWN_tx_valve_0 = COWN.tx_valve()
        self.COWN_syncher2_0 = COWN.syncher2()
        (self.COWN_syncher2_0).set_min_output_buffer(16384)
        self.COWN_resta_0 = COWN.resta()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.ieee802_11_ofdm_mac_0, 'app in'))    
        self.msg_connect((self.ieee802_11_ofdm_decode_mac_0, 'out'), (self.ieee802_11_ofdm_parse_mac_0, 'in'))    
        self.msg_connect((self.ieee802_11_ofdm_mac_0, 'phy out'), (self.wifi_PHY_tx_hier_1, 'mac_in'))    
        self.msg_connect((self.ieee802_11_ofdm_parse_mac_0, 'fer'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))    
        self.connect((self.COWN_resta_0, 0), (self.blocks_null_sink_0_0, 0))    
        self.connect((self.COWN_syncher2_0, 0), (self.blocks_deinterleave_0, 0))    
        self.connect((self.COWN_tx_valve_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0_0, 0))    
        self.connect((self.blocks_deinterleave_0, 3), (self.COWN_resta_0, 0))    
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.blocks_deinterleave_0, 2), (self.blocks_float_to_complex_1, 1))    
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.ieee802_11_ofdm_sync_long_0, 1))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.ofdm_80211_short_MF_v2_0, 0))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.qtgui_time_sink_x_0_0_0_1, 0))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 0))    
        self.connect((self.blocks_float_to_short_0_0_0, 0), (self.blocks_interleave_0, 1))    
        self.connect((self.blocks_interleave_0, 0), (self.nutaq_rtdex_sink_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.qtgui_time_sink_x_2_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.carajito, 0), (self.blocks_delay_0, 0))    
        self.connect((self.carajito, 0), (self.ieee802_11_ofdm_sync_long_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.ieee802_11_ofdm_equalize_symbols_0, 0))    
        self.connect((self.ieee802_11_ofdm_decode_signal_0, 0), (self.ieee802_11_ofdm_decode_mac_0, 0))    
        self.connect((self.ieee802_11_ofdm_equalize_symbols_0, 0), (self.ieee802_11_ofdm_decode_signal_0, 0))    
        self.connect((self.ieee802_11_ofdm_sync_long_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.nutaq_rtdex_source_0, 0), (self.COWN_syncher2_0, 0))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 2), (self.blocks_null_sink_0_1, 0))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 0), (self.carajito, 0))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 1), (self.carajito, 1))    
        self.connect((self.ofdm_80211_short_MF_v2_0, 3), (self.carajito, 2))    
        self.connect((self.wifi_PHY_tx_hier_1, 0), (self.COWN_tx_valve_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block_waveforms")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_chan_est(self):
        return self.chan_est

    def set_chan_est(self, chan_est):
        self.chan_est = chan_est
        self.ieee802_11_ofdm_equalize_symbols_0.set_algorithm(self.chan_est)

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

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period
        self.blocks_message_strobe_0_0.set_period(self.period)

    def get_pdu_length(self):
        return self.pdu_length

    def set_pdu_length(self, pdu_length):
        self.pdu_length = pdu_length
        self.blocks_message_strobe_0_0.set_msg(pmt.intern("Hello__" +"".join("x" for i in range(self.pdu_length)) + "1234"))

    def get_out_buf_size(self):
        return self.out_buf_size

    def set_out_buf_size(self, out_buf_size):
        self.out_buf_size = out_buf_size

    def get_freq_sin(self):
        return self.freq_sin

    def set_freq_sin(self, freq_sin):
        self.freq_sin = freq_sin

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block_waveforms()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
