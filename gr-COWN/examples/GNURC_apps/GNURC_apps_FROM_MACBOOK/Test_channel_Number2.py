#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Test Channel Number2
# Generated: Tue Feb 17 14:54:50 2015
##################################################

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import nutaq
import pmt
import sip
import spectsensing
import sys

class Test_channel_Number2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Test Channel Number2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Test Channel Number2")
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

        self.settings = Qt.QSettings("GNU Radio", "Test_channel_Number2")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.packet_size_gige = packet_size_gige = 1024
        self.samp_rate = samp_rate = 20e6
        self.packet_size = packet_size = packet_size_gige
        self.cucala = cucala = 2.5e6
        self.RF_freq = RF_freq = 943e6

        ##################################################
        # Blocks
        ##################################################
        self.spectsensing_subband_selector_0 = spectsensing.subband_selector(40, 40)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate/1e5/40, #samp_rate
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	2048, #size
        	samp_rate/1e5, #samp_rate
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_TX", 2, 1)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(RF_freq)
        self.nutaq_radio420_tx_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_tx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0_0.set_default_band(1)
        self.nutaq_radio420_tx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-10)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(15)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain3(3)
        self.nutaq_radio420_tx_0_0.set_default_tx_lpf_bandwidth(1)
        self.nutaq_radio420_tx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_tx_0 = nutaq.radio420_tx("nutaq_carrier_perseus_TX", 1, 0)
        self.nutaq_radio420_tx_0.set_default_enable(1)
        self.nutaq_radio420_tx_0.set_default_tx_freq(RF_freq)
        self.nutaq_radio420_tx_0.set_default_reference(0)
        self.nutaq_radio420_tx_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_tx_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0.set_default_band(1)
        self.nutaq_radio420_tx_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0.set_default_tx_vga1_gain(-10)
        self.nutaq_radio420_tx_0.set_default_tx_vga2_gain(15)
        self.nutaq_radio420_tx_0.set_default_tx_gain3(3)
        self.nutaq_radio420_tx_0.set_default_tx_lpf_bandwidth(1)
        self.nutaq_radio420_tx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_tx_gain_ctrl(1)
        self.nutaq_radio420_tx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0_0 = nutaq.radio420_rx("nutaq_carrier_perseus_TX", 2, 3)
        self.nutaq_radio420_rx_0_0.set_default_enable(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_freq(RF_freq)
        self.nutaq_radio420_rx_0_0.set_default_reference(0)
        self.nutaq_radio420_rx_0_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_rx_0_0.set_default_band(1)
        self.nutaq_radio420_rx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_vga1_gain(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain3(-8)
        self.nutaq_radio420_rx_0_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_lpf_bandwidth(1)
        self.nutaq_radio420_rx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0 = nutaq.radio420_rx("nutaq_carrier_perseus_TX", 1, 2)
        self.nutaq_radio420_rx_0.set_default_enable(1)
        self.nutaq_radio420_rx_0.set_default_rx_freq(RF_freq)
        self.nutaq_radio420_rx_0.set_default_reference(0)
        self.nutaq_radio420_rx_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_0.set_default_calibrate(0)
        self.nutaq_radio420_rx_0.set_default_band(1)
        self.nutaq_radio420_rx_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0.set_default_rx_vga1_gain(2)
        self.nutaq_radio420_rx_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain3(-8)
        self.nutaq_radio420_rx_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0.set_default_rx_lpf_bandwidth(1)
        self.nutaq_radio420_rx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_custom_register_0_1_1 = nutaq.custom_register("nutaq_carrier_perseus_TX",9)
        self.nutaq_custom_register_0_1_1.set_index(6)
        self.nutaq_custom_register_0_1_1.set_default_value(820)
        self.nutaq_custom_register_0_1_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_1_0 = nutaq.custom_register("nutaq_carrier_perseus_TX",7)
        self.nutaq_custom_register_0_1_0.set_index(2)
        self.nutaq_custom_register_0_1_0.set_update_rate(1)
          
        self.nutaq_custom_register_0_1 = nutaq.custom_register("nutaq_carrier_perseus_TX",6)
        self.nutaq_custom_register_0_1.set_index(0)
        self.nutaq_custom_register_0_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_0_0 = nutaq.custom_register("nutaq_carrier_perseus_TX",8)
        self.nutaq_custom_register_0_0_0.set_index(3)
        self.nutaq_custom_register_0_0_0.set_default_value(7)
        self.nutaq_custom_register_0_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0_0 = nutaq.custom_register("nutaq_carrier_perseus_TX",5)
        self.nutaq_custom_register_0_0.set_index(4)
        self.nutaq_custom_register_0_0.set_default_value(1)
        self.nutaq_custom_register_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0 = nutaq.custom_register("nutaq_carrier_perseus_TX",4)
        self.nutaq_custom_register_0.set_index(1)
        self.nutaq_custom_register_0.set_update_rate(1)
          
        self.nutaq_carrier_perseus_TX = nutaq.carrier(0,"nutaq_carrier_perseus_TX", "192.168.0.101")
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate/1e4,True)
        self.blocks_tags_strobe_0 = blocks.tags_strobe(gr.sizeof_float*1, pmt.intern("TEST"), 1000, pmt.intern("strobe"))
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.float_t, "packet_len")
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, 40)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_float_to_int_0_0_0 = blocks.float_to_int(1, 1)
        self.blocks_float_to_int_0_0 = blocks.float_to_int(1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate/1e5, analog.GR_COS_WAVE, 10, 1, 0)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1e5*(2**32)/samp_rate)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, ( cucala)/samp_rate*(2**32))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_int_0_0, 0), (self.nutaq_custom_register_0_1_0, 0))
        self.connect((self.blocks_float_to_int_0_0_0, 0), (self.nutaq_custom_register_0_1, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_int_0_0_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_int_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.spectsensing_subband_selector_0, 1))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.spectsensing_subband_selector_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.spectsensing_subband_selector_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_tags_strobe_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.blocks_tagged_stream_to_pdu_0, "pdus", self.blocks_message_debug_0, "print")
        self.msg_connect(self.blocks_tagged_stream_to_pdu_0, "pdus", self.blocks_message_debug_0, "print_pdu")

# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Test_channel_Number2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_packet_size_gige(self):
        return self.packet_size_gige

    def set_packet_size_gige(self, packet_size_gige):
        self.packet_size_gige = packet_size_gige
        self.set_packet_size(self.packet_size_gige)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_const_source_x_0_0.set_offset(1e5*(2**32)/self.samp_rate)
        self.analog_const_source_x_0.set_offset(( self.cucala)/self.samp_rate*(2**32))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/1e5)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/1e4)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate/1e5/40)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/1e5)

    def get_packet_size(self):
        return self.packet_size

    def set_packet_size(self, packet_size):
        self.packet_size = packet_size

    def get_cucala(self):
        return self.cucala

    def set_cucala(self, cucala):
        self.cucala = cucala
        self.analog_const_source_x_0.set_offset(( self.cucala)/self.samp_rate*(2**32))

    def get_RF_freq(self):
        return self.RF_freq

    def set_RF_freq(self, RF_freq):
        self.RF_freq = RF_freq
        self.nutaq_radio420_rx_0.set_rx_gain(-8)
        self.nutaq_radio420_rx_0.set_rx_freq(self.RF_freq)
          
        self.nutaq_radio420_tx_0.set_tx_gain(3)
        self.nutaq_radio420_tx_0.set_tx_freq(self.RF_freq)
          
        self.nutaq_radio420_tx_0_0.set_tx_gain(3)
        self.nutaq_radio420_tx_0_0.set_tx_freq(self.RF_freq)
          
        self.nutaq_radio420_rx_0_0.set_rx_gain(-8)
        self.nutaq_radio420_rx_0_0.set_rx_freq(self.RF_freq)
          

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = Test_channel_Number2()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

