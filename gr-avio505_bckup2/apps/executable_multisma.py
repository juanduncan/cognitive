#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Executable MultiSDA 
# Generated: Thu Jan 21 13:06:15 2016
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import avio505
import nutaq
import sip
import sys


class executable_multisma(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Executable MultiSDA ")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Executable MultiSDA ")
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

        self.settings = Qt.QSettings("GNU Radio", "executable_multisma")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1.28e6
        self.reg28 = reg28 = 5
        self.frq_DME_2 = frq_DME_2 = 1e5
        self.frq_DME_1 = frq_DME_1 = 1e5
        self.frq_ADSB = frq_ADSB = 1e5
        self.freq_VOR_DME2 = freq_VOR_DME2 = 108.5
        self.freq_VOR_DME1 = freq_VOR_DME1 = 108.00
        self.Radio2_chooser = Radio2_chooser = 0
        self.Radio1_chooser = Radio1_chooser = 0

        ##################################################
        # Blocks
        ##################################################
        self._reg28_tool_bar = Qt.QToolBar(self)
        self._reg28_tool_bar.addWidget(Qt.QLabel("REG28[3:0]"+": "))
        self._reg28_line_edit = Qt.QLineEdit(str(self.reg28))
        self._reg28_tool_bar.addWidget(self._reg28_line_edit)
        self._reg28_line_edit.returnPressed.connect(
        	lambda: self.set_reg28(int(str(self._reg28_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._reg28_tool_bar)
        self._frq_DME_1_range = Range(-250e3, 250e3, 1, 1e5, 200)
        self._frq_DME_1_win = RangeWidget(self._frq_DME_1_range, self.set_frq_DME_1, "frq_DME_1", "counter_slider", float)
        self.top_layout.addWidget(self._frq_DME_1_win)
        self._Radio2_chooser_options = (0, 1, 2, 3, )
        self._Radio2_chooser_labels = ("Constante", "ADS-B", "DME1", "DME2", )
        self._Radio2_chooser_group_box = Qt.QGroupBox("Radio2")
        self._Radio2_chooser_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._Radio2_chooser_button_group = variable_chooser_button_group()
        self._Radio2_chooser_group_box.setLayout(self._Radio2_chooser_box)
        for i, label in enumerate(self._Radio2_chooser_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._Radio2_chooser_box.addWidget(radio_button)
        	self._Radio2_chooser_button_group.addButton(radio_button, i)
        self._Radio2_chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Radio2_chooser_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._Radio2_chooser_options.index(i)))
        self._Radio2_chooser_callback(self.Radio2_chooser)
        self._Radio2_chooser_button_group.buttonClicked[int].connect(
        	lambda i: self.set_Radio2_chooser(self._Radio2_chooser_options[i]))
        self.top_grid_layout.addWidget(self._Radio2_chooser_group_box, 1,2,1,1)
        self._Radio1_chooser_options = (0, 1, 2, 3, )
        self._Radio1_chooser_labels = ("Constante", "ADS-B", "DME1", "DME2", )
        self._Radio1_chooser_group_box = Qt.QGroupBox("Radio1")
        self._Radio1_chooser_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._Radio1_chooser_button_group = variable_chooser_button_group()
        self._Radio1_chooser_group_box.setLayout(self._Radio1_chooser_box)
        for i, label in enumerate(self._Radio1_chooser_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._Radio1_chooser_box.addWidget(radio_button)
        	self._Radio1_chooser_button_group.addButton(radio_button, i)
        self._Radio1_chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Radio1_chooser_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._Radio1_chooser_options.index(i)))
        self._Radio1_chooser_callback(self.Radio1_chooser)
        self._Radio1_chooser_button_group.buttonClicked[int].connect(
        	lambda i: self.set_Radio1_chooser(self._Radio1_chooser_options[i]))
        self.top_grid_layout.addWidget(self._Radio1_chooser_group_box, 1,1,1,1)
        self.qtgui_time_sink_x_3 = qtgui.time_sink_f(
        	1024, #size
        	20, #samp_rate
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_3.set_update_time(0.10)
        self.qtgui_time_sink_x_3.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_3.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_3.enable_tags(-1, True)
        self.qtgui_time_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3.enable_autoscale(False)
        self.qtgui_time_sink_x_3.enable_grid(False)
        self.qtgui_time_sink_x_3.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_3.disable_legend()
        
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
                self.qtgui_time_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_3_win = sip.wrapinstance(self.qtgui_time_sink_x_3.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_3_win)
        self.qtgui_time_sink_x_2_0 = qtgui.time_sink_c(
        	2048, #size
        	samp_rate/20, #samp_rate
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_2_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_2_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_NEG, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_2_0.enable_grid(False)
        self.qtgui_time_sink_x_2_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_2_0.disable_legend()
        
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
                    self.qtgui_time_sink_x_2_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_0_win, 5,2,1,1)
        (self.qtgui_time_sink_x_2_0).set_processor_affinity([7])
        self.qtgui_time_sink_x_2 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate/20, #samp_rate
        	"QT GUI Plot hola", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_2.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_2.disable_legend()
        
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
                    self.qtgui_time_sink_x_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_win, 5,1,1,1)
        (self.qtgui_time_sink_x_2).set_processor_affinity([7])
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/5, #bw
        	"QT GUI Plot", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        (self.qtgui_sink_x_0).set_processor_affinity([7])
        self.nutaq_rtdex_source_0_0_0 = nutaq.rtdex_source("nutaq_carrier_perseus_0",gr.sizeof_int,1,7)
        self.nutaq_rtdex_source_0_0_0.set_type(0)
        self.nutaq_rtdex_source_0_0_0.set_packet_size(8192)
        self.nutaq_rtdex_source_0_0_0.set_channels("0")
        (self.nutaq_rtdex_source_0_0_0).set_processor_affinity([3])
        (self.nutaq_rtdex_source_0_0_0).set_min_output_buffer(32768)
        (self.nutaq_rtdex_source_0_0_0).set_max_output_buffer(32768)
        self.nutaq_rtdex_sink_0_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_0",gr.sizeof_int,1,8)
        self.nutaq_rtdex_sink_0_0.set_type(0)
        self.nutaq_rtdex_sink_0_0.set_packet_size(8192)
        self.nutaq_rtdex_sink_0_0.set_channels("0")
        (self.nutaq_rtdex_sink_0_0).set_processor_affinity([5])
        self.nutaq_radio420_tx_2 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 2, 2)
        self.nutaq_radio420_tx_2.set_default_enable(1)
        self.nutaq_radio420_tx_2.set_default_tx_freq(2000e6)
        self.nutaq_radio420_tx_2.set_default_reference(1)
        self.nutaq_radio420_tx_2.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_tx_2.set_default_calibrate(0)
        self.nutaq_radio420_tx_2.set_default_band(1)
        self.nutaq_radio420_tx_2.set_default_update_rate(1)
        self.nutaq_radio420_tx_2.set_default_tx_vga1_gain(-4)
        self.nutaq_radio420_tx_2.set_default_tx_vga2_gain(10)
        self.nutaq_radio420_tx_2.set_default_tx_gain3(0)
        self.nutaq_radio420_tx_2.set_default_tx_lpf_bandwidth(0)
        self.nutaq_radio420_tx_2.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_2.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_2.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_2.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_tx_1 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 1, 0)
        self.nutaq_radio420_tx_1.set_default_enable(1)
        self.nutaq_radio420_tx_1.set_default_tx_freq(541e6)
        self.nutaq_radio420_tx_1.set_default_reference(0)
        self.nutaq_radio420_tx_1.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_tx_1.set_default_calibrate(0)
        self.nutaq_radio420_tx_1.set_default_band(0)
        self.nutaq_radio420_tx_1.set_default_update_rate(1)
        self.nutaq_radio420_tx_1.set_default_tx_vga1_gain(-4)
        self.nutaq_radio420_tx_1.set_default_tx_vga2_gain(10)
        self.nutaq_radio420_tx_1.set_default_tx_gain3(0)
        self.nutaq_radio420_tx_1.set_default_tx_lpf_bandwidth(0)
        self.nutaq_radio420_tx_1.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_1.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_1.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_1.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_2 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 2, 3)
        self.nutaq_radio420_rx_2.set_default_enable(1)
        self.nutaq_radio420_rx_2.set_default_rx_freq(2500e6)
        self.nutaq_radio420_rx_2.set_default_reference(1)
        self.nutaq_radio420_rx_2.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_2.set_default_calibrate(1)
        self.nutaq_radio420_rx_2.set_default_band(1)
        self.nutaq_radio420_rx_2.set_default_update_rate(1)
        self.nutaq_radio420_rx_2.set_default_rx_lna_gain(3)
        self.nutaq_radio420_rx_2.set_default_rx_vga1_gain(1)
        self.nutaq_radio420_rx_2.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_2.set_default_rx_gain3(18)
        self.nutaq_radio420_rx_2.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_2.set_default_rx_lpf_bandwidth(1)
        self.nutaq_radio420_rx_2.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_2.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_2.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_2.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_1 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 1, 1)
        self.nutaq_radio420_rx_1.set_default_enable(1)
        self.nutaq_radio420_rx_1.set_default_rx_freq(1.041e9)
        self.nutaq_radio420_rx_1.set_default_reference(0)
        self.nutaq_radio420_rx_1.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_1.set_default_calibrate(1)
        self.nutaq_radio420_rx_1.set_default_band(0)
        self.nutaq_radio420_rx_1.set_default_update_rate(1)
        self.nutaq_radio420_rx_1.set_default_rx_lna_gain(3)
        self.nutaq_radio420_rx_1.set_default_rx_vga1_gain(1)
        self.nutaq_radio420_rx_1.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_1.set_default_rx_gain3(18)
        self.nutaq_radio420_rx_1.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_1.set_default_rx_lpf_bandwidth(1)
        self.nutaq_radio420_rx_1.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_1.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_1.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_1.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_custom_register_28 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_28.set_index(28)
        self.nutaq_custom_register_28.set_default_value((Radio1_chooser*4+Radio2_chooser)*16 + reg28)
        self.nutaq_custom_register_28.set_update_rate(10)
          
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
        self.nutaq_custom_register_0_0_0_0.set_update_rate(20)
          
        self.nutaq_custom_register_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0.set_index(4)
        self.nutaq_custom_register_0_0.set_default_value(6)
        self.nutaq_custom_register_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0 = nutaq.custom_register("nutaq_carrier_perseus_0",0)
        self.nutaq_custom_register_0.set_index(1)
        self.nutaq_custom_register_0.set_default_value(6)
        self.nutaq_custom_register_0.set_update_rate(1)
          
        self.nutaq_carrier_perseus_0 = nutaq.carrier(0,"nutaq_carrier_perseus_0", "192.168.0.101")
        self._frq_DME_2_range = Range(-250e3, 250e3, 1, 1e5, 200)
        self._frq_DME_2_win = RangeWidget(self._frq_DME_2_range, self.set_frq_DME_2, "frq_DME_2", "counter_slider", float)
        self.top_layout.addWidget(self._frq_DME_2_win)
        self._frq_ADSB_range = Range(-250e3, 250e3, 1, 1e5, 200)
        self._frq_ADSB_win = RangeWidget(self._frq_ADSB_range, self.set_frq_ADSB, "frq_ADSB", "counter_slider", float)
        self.top_layout.addWidget(self._frq_ADSB_win)
        self._freq_VOR_DME2_tool_bar = Qt.QToolBar(self)
        self._freq_VOR_DME2_tool_bar.addWidget(Qt.QLabel("DME 2, VOR frequency (MHz)"+": "))
        self._freq_VOR_DME2_line_edit = Qt.QLineEdit(str(self.freq_VOR_DME2))
        self._freq_VOR_DME2_tool_bar.addWidget(self._freq_VOR_DME2_line_edit)
        self._freq_VOR_DME2_line_edit.returnPressed.connect(
        	lambda: self.set_freq_VOR_DME2(eng_notation.str_to_num(str(self._freq_VOR_DME2_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._freq_VOR_DME2_tool_bar, 3,2,1,1)
        self._freq_VOR_DME1_tool_bar = Qt.QToolBar(self)
        self._freq_VOR_DME1_tool_bar.addWidget(Qt.QLabel("DME 1, VOR frequency (MHz)"+": "))
        self._freq_VOR_DME1_line_edit = Qt.QLineEdit(str(self.freq_VOR_DME1))
        self._freq_VOR_DME1_tool_bar.addWidget(self._freq_VOR_DME1_line_edit)
        self._freq_VOR_DME1_line_edit.returnPressed.connect(
        	lambda: self.set_freq_VOR_DME1(eng_notation.str_to_num(str(self._freq_VOR_DME1_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._freq_VOR_DME1_tool_bar, 3,1,1,1)
        self.blocks_null_source_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_interleaved_short_to_complex_1_1 = blocks.interleaved_short_to_complex(True, False)
        (self.blocks_interleaved_short_to_complex_1_1).set_processor_affinity([4])
        (self.blocks_interleaved_short_to_complex_1_1).set_min_output_buffer(16384)
        (self.blocks_interleaved_short_to_complex_1_1).set_max_output_buffer(16384)
        self.blocks_interleaved_short_to_complex_1_0 = blocks.interleaved_short_to_complex(True, False)
        (self.blocks_interleaved_short_to_complex_1_0).set_processor_affinity([4])
        (self.blocks_interleaved_short_to_complex_1_0).set_min_output_buffer(16384)
        (self.blocks_interleaved_short_to_complex_1_0).set_max_output_buffer(16384)
        self.blocks_interleaved_short_to_complex_1 = blocks.interleaved_short_to_complex(True, False)
        (self.blocks_interleaved_short_to_complex_1).set_processor_affinity([4])
        (self.blocks_interleaved_short_to_complex_1).set_min_output_buffer(16384)
        (self.blocks_interleaved_short_to_complex_1).set_max_output_buffer(16384)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_int*1, 1)
        (self.blocks_interleave_0).set_processor_affinity([4])
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_int*1, 1)
        (self.blocks_deinterleave_0).set_processor_affinity([3])
        self.avio505_three_ch_mux_rtdex_v2_1 = avio505.three_ch_mux_rtdex_v2()
        (self.avio505_three_ch_mux_rtdex_v2_1).set_processor_affinity((5, 6))
        self.avio505_syncher_0 = avio505.syncher()
        (self.avio505_syncher_0).set_processor_affinity([4])
        (self.avio505_syncher_0).set_min_output_buffer(32768)
        (self.avio505_syncher_0).set_max_output_buffer(32768)
        self.avio505_resta_0 = avio505.resta()
        (self.avio505_resta_0).set_processor_affinity([4])
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate/20, analog.GR_SIN_WAVE, frq_DME_1, 0.5, 0)
        (self.analog_sig_source_x_0_1).set_processor_affinity([3])

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_1, 0), (self.avio505_three_ch_mux_rtdex_v2_1, 0))    
        self.connect((self.avio505_resta_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.avio505_syncher_0, 0), (self.blocks_deinterleave_0, 0))    
        self.connect((self.avio505_three_ch_mux_rtdex_v2_1, 0), (self.nutaq_rtdex_sink_0_0, 0))    
        self.connect((self.blocks_deinterleave_0, 6), (self.avio505_resta_0, 0))    
        self.connect((self.blocks_deinterleave_0, 2), (self.blocks_interleave_0, 0))    
        self.connect((self.blocks_deinterleave_0, 3), (self.blocks_interleave_0, 1))    
        self.connect((self.blocks_deinterleave_0, 4), (self.blocks_interleave_0, 2))    
        self.connect((self.blocks_deinterleave_0, 5), (self.blocks_interleave_0, 3))    
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_interleaved_short_to_complex_1_0, 0))    
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_interleaved_short_to_complex_1_1, 0))    
        self.connect((self.blocks_interleave_0, 0), (self.blocks_interleaved_short_to_complex_1, 0))    
        self.connect((self.blocks_interleaved_short_to_complex_1, 0), (self.qtgui_sink_x_0, 0))    
        self.connect((self.blocks_interleaved_short_to_complex_1_0, 0), (self.qtgui_time_sink_x_2, 0))    
        self.connect((self.blocks_interleaved_short_to_complex_1_1, 0), (self.qtgui_time_sink_x_2_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.avio505_three_ch_mux_rtdex_v2_1, 1))    
        self.connect((self.blocks_null_source_1, 0), (self.avio505_three_ch_mux_rtdex_v2_1, 2))    
        self.connect((self.nutaq_custom_register_0_0_0_0, 0), (self.qtgui_time_sink_x_3, 0))    
        self.connect((self.nutaq_rtdex_source_0_0_0, 0), (self.avio505_syncher_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "executable_multisma")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate/20)
        self.nutaq_custom_register_0_1.set_value(int((2e5)/self.samp_rate*(2**32)))
        self.nutaq_custom_register_0_1_0.set_value(int((7.5e4)/self.samp_rate*(2**32)))
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate/5)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate/20)
        self.qtgui_time_sink_x_2_0.set_samp_rate(self.samp_rate/20)

    def get_reg28(self):
        return self.reg28

    def set_reg28(self, reg28):
        self.reg28 = reg28
        Qt.QMetaObject.invokeMethod(self._reg28_line_edit, "setText", Qt.Q_ARG("QString", str(self.reg28)))
        self.nutaq_custom_register_28.set_value((self.Radio1_chooser*4+self.Radio2_chooser)*16 + self.reg28)

    def get_frq_DME_2(self):
        return self.frq_DME_2

    def set_frq_DME_2(self, frq_DME_2):
        self.frq_DME_2 = frq_DME_2

    def get_frq_DME_1(self):
        return self.frq_DME_1

    def set_frq_DME_1(self, frq_DME_1):
        self.frq_DME_1 = frq_DME_1
        self.analog_sig_source_x_0_1.set_frequency(self.frq_DME_1)

    def get_frq_ADSB(self):
        return self.frq_ADSB

    def set_frq_ADSB(self, frq_ADSB):
        self.frq_ADSB = frq_ADSB

    def get_freq_VOR_DME2(self):
        return self.freq_VOR_DME2

    def set_freq_VOR_DME2(self, freq_VOR_DME2):
        self.freq_VOR_DME2 = freq_VOR_DME2
        Qt.QMetaObject.invokeMethod(self._freq_VOR_DME2_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.freq_VOR_DME2)))

    def get_freq_VOR_DME1(self):
        return self.freq_VOR_DME1

    def set_freq_VOR_DME1(self, freq_VOR_DME1):
        self.freq_VOR_DME1 = freq_VOR_DME1
        Qt.QMetaObject.invokeMethod(self._freq_VOR_DME1_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.freq_VOR_DME1)))

    def get_Radio2_chooser(self):
        return self.Radio2_chooser

    def set_Radio2_chooser(self, Radio2_chooser):
        self.Radio2_chooser = Radio2_chooser
        self._Radio2_chooser_callback(self.Radio2_chooser)
        self.nutaq_custom_register_28.set_value((self.Radio1_chooser*4+self.Radio2_chooser)*16 + self.reg28)

    def get_Radio1_chooser(self):
        return self.Radio1_chooser

    def set_Radio1_chooser(self, Radio1_chooser):
        self.Radio1_chooser = Radio1_chooser
        self._Radio1_chooser_callback(self.Radio1_chooser)
        self.nutaq_custom_register_28.set_value((self.Radio1_chooser*4+self.Radio2_chooser)*16 + self.reg28)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = executable_multisma()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
