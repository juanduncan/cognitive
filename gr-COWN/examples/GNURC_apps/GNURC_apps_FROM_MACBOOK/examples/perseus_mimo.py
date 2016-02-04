#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Perseus MIMO
# Generated: Tue Dec  9 18:23:55 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import nutaq
import wx

class perseus_mimo(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Perseus MIMO")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 14.40e6/2
        self.freq2 = freq2 = 1e6
        self.freq1 = freq1 = 500e3

        ##################################################
        # Blocks
        ##################################################
        _freq2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq2_sizer,
        	value=self.freq2,
        	callback=self.set_freq2,
        	label='freq2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq2_sizer,
        	value=self.freq2,
        	callback=self.set_freq2,
        	minimum=-samp_rate/2,
        	maximum=samp_rate/2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq2_sizer)
        _freq1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq1_sizer,
        	value=self.freq1,
        	callback=self.set_freq1,
        	label='freq1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq1_sizer,
        	value=self.freq1,
        	callback=self.set_freq1,
        	minimum=-samp_rate/2,
        	maximum=samp_rate/2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq1_sizer)
        self.wxgui_fftsink_1 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        	size=(200,200),
        )
        self.GridAdd(self.wxgui_fftsink_1.win, 1, 1, 1, 1)
        self.wxgui_fftsink_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        	win=window.blackmanharris,
        	size=(200, 200),
        )
        self.GridAdd(self.wxgui_fftsink_0.win, 1, 2, 1, 1)
        self.nutaq_rtdex_source_0 = nutaq.rtdex_source("nutaq_carrier_perseus_0",gr.sizeof_short,2,5)
        self.nutaq_rtdex_source_0.set_type(0)
        self.nutaq_rtdex_source_0.set_packet_size(8192)
        self.nutaq_rtdex_source_0.set_channels("1,2")
        self.nutaq_rtdex_sink_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_0",gr.sizeof_short,2,4)
        self.nutaq_rtdex_sink_0.set_type(0)
        self.nutaq_rtdex_sink_0.set_packet_size(8192)
        self.nutaq_rtdex_sink_0.set_channels("1,2")
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 2, 2)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(953e6)
        self.nutaq_radio420_tx_0_0.set_default_reference(1)
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
        self.nutaq_radio420_tx_0.set_default_tx_freq(953e6)
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
        self.nutaq_radio420_rx_0_0.set_default_rx_freq(953e6)
        self.nutaq_radio420_rx_0_0.set_default_reference(1)
        self.nutaq_radio420_rx_0_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_rx_0_0.set_default_band(0)
        self.nutaq_radio420_rx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_vga1_gain(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain3(-8)
        self.nutaq_radio420_rx_0_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_lpf_bandwidth(6)
        self.nutaq_radio420_rx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 1, 1)
        self.nutaq_radio420_rx_0.set_default_enable(1)
        self.nutaq_radio420_rx_0.set_default_rx_freq(953e6)
        self.nutaq_radio420_rx_0.set_default_reference(0)
        self.nutaq_radio420_rx_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_0.set_default_calibrate(0)
        self.nutaq_radio420_rx_0.set_default_band(0)
        self.nutaq_radio420_rx_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0.set_default_rx_vga1_gain(1)
        self.nutaq_radio420_rx_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain3(-8)
        self.nutaq_radio420_rx_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0.set_default_rx_lpf_bandwidth(6)
        self.nutaq_radio420_rx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_custom_register_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_0.set_index(4)
        self.nutaq_custom_register_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0 = nutaq.custom_register("nutaq_carrier_perseus_0",6)
        self.nutaq_custom_register_0.set_index(1)
        self.nutaq_custom_register_0.set_default_value(6)
        self.nutaq_custom_register_0.set_update_rate(1)
          
        self.nutaq_carrier_perseus_0 = nutaq.carrier(0,"nutaq_carrier_perseus_0", "192.168.0.102")
        self.blocks_short_to_float_0_1 = blocks.short_to_float(1, 2**11-1)
        self.blocks_short_to_float_0_0_0 = blocks.short_to_float(1, 2**11-1)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 2**11-1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 2**11-1)
        self.blocks_interleave_0_0 = blocks.interleave(gr.sizeof_short*1)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1)
        self.blocks_float_to_short_0_0_1 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_short_0_0_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_short_0_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_deinterleave_0_0 = blocks.deinterleave(gr.sizeof_short*1)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_short*1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq2, 0.95, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq1, 0.95, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self.wxgui_fftsink_1, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.wxgui_fftsink_0, 0))
        self.connect((self.blocks_interleave_0, 0), (self.nutaq_rtdex_sink_0, 0))
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 0))
        self.connect((self.blocks_float_to_short_0_0_0, 0), (self.blocks_interleave_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.blocks_interleave_0_0, 0), (self.nutaq_rtdex_sink_0, 1))
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_short_to_float_0_0, 0))
        self.connect((self.nutaq_rtdex_source_0, 0), (self.blocks_deinterleave_0, 0))
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.nutaq_rtdex_source_0, 1), (self.blocks_deinterleave_0_0, 0))
        self.connect((self.blocks_deinterleave_0_0, 1), (self.blocks_short_to_float_0_0_0, 0))
        self.connect((self.blocks_deinterleave_0_0, 0), (self.blocks_short_to_float_0_1, 0))
        self.connect((self.blocks_short_to_float_0_1, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_short_to_float_0_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_float_to_short_0_0_0_0, 0), (self.blocks_interleave_0_0, 1))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_float_to_short_0_0_1, 0))
        self.connect((self.blocks_float_to_short_0_0_1, 0), (self.blocks_interleave_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_float_to_short_0_0_0_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.wxgui_fftsink_1.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink_0.set_sample_rate(self.samp_rate)

    def get_freq2(self):
        return self.freq2

    def set_freq2(self, freq2):
        self.freq2 = freq2
        self._freq2_slider.set_value(self.freq2)
        self._freq2_text_box.set_value(self.freq2)
        self.analog_sig_source_x_0_0.set_frequency(self.freq2)

    def get_freq1(self):
        return self.freq1

    def set_freq1(self, freq1):
        self.freq1 = freq1
        self._freq1_slider.set_value(self.freq1)
        self._freq1_text_box.set_value(self.freq1)
        self.analog_sig_source_x_0.set_frequency(self.freq1)

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
    tb = perseus_mimo()
    tb.Start(True)
    tb.Wait()

