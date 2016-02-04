#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Tag Generator
# Generated: Thu Jan 28 14:36:44 2016
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import COWN
import nutaq
import sip
import sys


class top_tag_generator(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Tag Generator")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Tag Generator")
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

        self.settings = Qt.QSettings("GNU Radio", "top_tag_generator")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 5e5
        self.freq_sin = freq_sin = 1000
        self.freq = freq = 943e6
        self.decimation = decimation = 40

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	2**13, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0, 1e-3, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()
        
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
        
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 2,2,1,1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.nutaq_rtdex_source_0 = nutaq.rtdex_source("nutaq_carrier_perseus_0",gr.sizeof_float,1,0)
        self.nutaq_rtdex_source_0.set_type(0)
        self.nutaq_rtdex_source_0.set_packet_size(8192)
        self.nutaq_rtdex_source_0.set_channels("0")
        (self.nutaq_rtdex_source_0).set_min_output_buffer(819200)
        (self.nutaq_rtdex_source_0).set_max_output_buffer(819200)
        self.nutaq_rtdex_sink_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_0",gr.sizeof_short,1,1)
        self.nutaq_rtdex_sink_0.set_type(0)
        self.nutaq_rtdex_sink_0.set_packet_size(8192)
        self.nutaq_rtdex_sink_0.set_channels("0")
        self.nutaq_radio420_tx_0_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 2, 2)
        self.nutaq_radio420_tx_0_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_freq(943e6)
        self.nutaq_radio420_tx_0_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_tx_0_0_0.set_default_calibrate(0)
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
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-20)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain3(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_lpf_bandwidth(2)
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
        self.nutaq_radio420_rx_0_0.set_default_rx_vga1_gain(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain3(8)
        self.nutaq_radio420_rx_0_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_lpf_bandwidth(2)
        self.nutaq_radio420_rx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 1, 1)
        self.nutaq_radio420_rx_0.set_default_enable(1)
        self.nutaq_radio420_rx_0.set_default_rx_freq(943e6)
        self.nutaq_radio420_rx_0.set_default_reference(0)
        self.nutaq_radio420_rx_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_rx_0.set_default_calibrate(1)
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
          
        self.nutaq_custom_register_0_3 = nutaq.custom_register("nutaq_carrier_perseus_0",11)
        self.nutaq_custom_register_0_3.set_index(2)
        self.nutaq_custom_register_0_3.set_update_rate(1)
          
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
        self._freq_sin_range = Range(-2.5e5, 2.5e5, 500, 1000, 200)
        self._freq_sin_win = RangeWidget(self._freq_sin_range, self.set_freq_sin, "freq_sin", "counter_slider", float)
        self.top_layout.addWidget(self._freq_sin_win)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.6, ))
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        self.blocks_float_to_short_0_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        (self.blocks_float_to_complex_1).set_processor_affinity([4])
        (self.blocks_float_to_complex_1).set_min_output_buffer(262144)
        (self.blocks_float_to_complex_1).set_max_output_buffer(262144)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/juan/cognitive/fornutaq/gr-ofdm_80211/examples/waveforms/fmcw_chirp_80pc.bin", True)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_int*1, 1)
        (self.blocks_deinterleave_0).set_processor_affinity([7])
        (self.blocks_deinterleave_0).set_min_output_buffer(262144)
        (self.blocks_deinterleave_0).set_max_output_buffer(262144)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        (self.blocks_complex_to_float_0).set_min_output_buffer(131072)
        (self.blocks_complex_to_float_0).set_max_output_buffer(131072)
        self.COWN_syncher2_0 = COWN.syncher2()
        (self.COWN_syncher2_0).set_processor_affinity([7])
        (self.COWN_syncher2_0).set_min_output_buffer(262144)
        (self.COWN_syncher2_0).set_max_output_buffer(262144)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.COWN_syncher2_0, 0), (self.blocks_deinterleave_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))    
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.blocks_deinterleave_0, 2), (self.blocks_float_to_complex_1, 1))    
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_deinterleave_0, 3), (self.blocks_null_sink_0_0, 0))    
        self.connect((self.blocks_deinterleave_0, 1), (self.qtgui_time_sink_x_0_0_0_0, 1))    
        self.connect((self.blocks_deinterleave_0, 2), (self.qtgui_time_sink_x_0_0_0_0, 2))    
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 0))    
        self.connect((self.blocks_float_to_short_0_0_0, 0), (self.blocks_interleave_0, 1))    
        self.connect((self.blocks_interleave_0, 0), (self.nutaq_rtdex_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.nutaq_rtdex_source_0, 0), (self.COWN_syncher2_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_tag_generator")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.nutaq_custom_register_0_2.set_value(int((4e6)/self.samp_rate/40*(2**32)))
        self.nutaq_custom_register_0_3.set_value(int((4.0e6*0 + self.freq_sin*0)/self.samp_rate/40*(2**32)))
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.samp_rate)

    def get_freq_sin(self):
        return self.freq_sin

    def set_freq_sin(self, freq_sin):
        self.freq_sin = freq_sin
        self.nutaq_custom_register_0_3.set_value(int((4.0e6*0 + self.freq_sin*0)/self.samp_rate/40*(2**32)))

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
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_tag_generator()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
