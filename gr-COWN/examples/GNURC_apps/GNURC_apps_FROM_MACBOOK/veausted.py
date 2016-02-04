#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Veausted
# Generated: Thu Mar 26 13:09:44 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import pmt
import spectsensing
import sys

class veausted(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Veausted")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Veausted")
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

        self.settings = Qt.QSettings("GNU Radio", "veausted")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 50
        self.samp_rate = samp_rate = 32e3
        self.freq = freq = 1e3
        self.ampl = ampl = 1

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_0_layout = Qt.QVBoxLayout()
        self._variable_qtgui_range_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_range_0_layout.addWidget(self._variable_qtgui_range_0_tool_bar)
        self._variable_qtgui_range_0_tool_bar.addWidget(Qt.QLabel("variable_qtgui_range_0"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._variable_qtgui_range_0_counter = qwt_counter_pyslot()
        self._variable_qtgui_range_0_counter.setRange(0, 100, 1)
        self._variable_qtgui_range_0_counter.setNumButtons(2)
        self._variable_qtgui_range_0_counter.setValue(self.variable_qtgui_range_0)
        self._variable_qtgui_range_0_tool_bar.addWidget(self._variable_qtgui_range_0_counter)
        self._variable_qtgui_range_0_counter.valueChanged.connect(self.set_variable_qtgui_range_0)
        self._variable_qtgui_range_0_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._variable_qtgui_range_0_slider.setRange(0, 100, 1)
        self._variable_qtgui_range_0_slider.setValue(self.variable_qtgui_range_0)
        self._variable_qtgui_range_0_slider.setMinimumWidth(200)
        self._variable_qtgui_range_0_slider.valueChanged.connect(self.set_variable_qtgui_range_0)
        self._variable_qtgui_range_0_layout.addWidget(self._variable_qtgui_range_0_slider)
        self.top_layout.addLayout(self._variable_qtgui_range_0_layout)
        self.spectsensing_time_plot_0 = spectsensing.time_plot("")
        self._spectsensing_time_plot_0_win = self.spectsensing_time_plot_0;
        self.top_layout.addWidget(self._spectsensing_time_plot_0_win)
        self.spectsensing_test_plot_0 = spectsensing.test_plot()
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_tool_bar.addWidget(Qt.QLabel("freq"+": "))
        self._freq_line_edit = Qt.QLineEdit(str(self.freq))
        self._freq_tool_bar.addWidget(self._freq_line_edit)
        self._freq_line_edit.returnPressed.connect(
        	lambda: self.set_freq(eng_notation.str_to_num(self._freq_line_edit.text().toAscii())))
        self.top_layout.addWidget(self._freq_tool_bar)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_random_pdu_0 = blocks.random_pdu(10, 10, chr(0xFF), 2)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 1, 0)
        self._ampl_tool_bar = Qt.QToolBar(self)
        self._ampl_tool_bar.addWidget(Qt.QLabel("ampl"+": "))
        self._ampl_line_edit = Qt.QLineEdit(str(self.ampl))
        self._ampl_tool_bar.addWidget(self._ampl_line_edit)
        self._ampl_line_edit.returnPressed.connect(
        	lambda: self.set_ampl(eng_notation.str_to_num(self._ampl_line_edit.text().toAscii())))
        self.top_layout.addWidget(self._ampl_tool_bar)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.spectsensing_test_plot_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.spectsensing_test_plot_0, 0), (self.blocks_null_sink_0, 0))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.spectsensing_test_plot_0, "pdus", self.spectsensing_time_plot_0, "pdus")

# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "veausted")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_range_0_counter, "setValue", Qt.Q_ARG("double", self.variable_qtgui_range_0))
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_range_0_slider, "setValue", Qt.Q_ARG("double", self.variable_qtgui_range_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        Qt.QMetaObject.invokeMethod(self._freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.freq)))

    def get_ampl(self):
        return self.ampl

    def set_ampl(self, ampl):
        self.ampl = ampl
        Qt.QMetaObject.invokeMethod(self._ampl_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ampl)))

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
    tb = veausted()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

