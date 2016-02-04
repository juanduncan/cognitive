#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Perseus MIMO
# Generated: Mon Aug 10 18:21:54 2015
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

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
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
        self.samp_rate = samp_rate = 40e6/2
        self.freq1 = freq1 = 500e3/40

        ##################################################
        # Blocks
        ##################################################
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
        	minimum=-samp_rate/2/40,
        	maximum=samp_rate/2/40,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq1_sizer)
        self.nutaq_rtdex_sink_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_0",gr.sizeof_short,1,4)
        self.nutaq_rtdex_sink_0.set_type(0)
        self.nutaq_rtdex_sink_0.set_packet_size(8192)
        self.nutaq_rtdex_sink_0.set_channels("1")
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 2, 2)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(943e6)
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
        self.nutaq_radio420_tx_0.set_default_tx_freq(943e6)
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
        self.nutaq_radio420_rx_0_0.set_default_rx_freq(943e6)
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
        self.nutaq_radio420_rx_0.set_default_rx_freq(943e6)
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
          
        self.nutaq_custom_register_0_1_1 = nutaq.custom_register("nutaq_carrier_perseus_0",9)
        self.nutaq_custom_register_0_1_1.set_index(6)
        self.nutaq_custom_register_0_1_1.set_default_value(600)
        self.nutaq_custom_register_0_1_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_1_0 = nutaq.custom_register("nutaq_carrier_perseus_0",7)
        self.nutaq_custom_register_0_1_0.set_index(2)
        self.nutaq_custom_register_0_1_0.set_update_rate(1)
          
        self.nutaq_custom_register_0_1 = nutaq.custom_register("nutaq_carrier_perseus_0",36)
        self.nutaq_custom_register_0_1.set_index(0)
        self.nutaq_custom_register_0_1.set_default_value(int((2e6)/samp_rate*(2**32)))
        self.nutaq_custom_register_0_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",8)
        self.nutaq_custom_register_0_0_0.set_index(3)
        self.nutaq_custom_register_0_0_0.set_default_value(7)
        self.nutaq_custom_register_0_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0 = nutaq.custom_register("nutaq_carrier_perseus_0",4)
        self.nutaq_custom_register_0.set_index(1)
        self.nutaq_custom_register_0.set_default_value(3)
        self.nutaq_custom_register_0.set_update_rate(1)
          
        self.nutaq_carrier_perseus_0d = nutaq.custom_register("nutaq_carrier_perseus_0",5)
        self.nutaq_carrier_perseus_0d.set_index(4)
        self.nutaq_carrier_perseus_0d.set_default_value(1)
        self.nutaq_carrier_perseus_0d.set_update_rate(1)
          
        self.nutaq_carrier_perseus_0 = nutaq.carrier(0,"nutaq_carrier_perseus_0", "192.168.0.101")
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vcc((0.125, ))
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        self.blocks_float_to_short_0_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate/40, analog.GR_COS_WAVE, freq1, 0.95, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_const_vxx_0_2, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0_0, 0))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 0))    
        self.connect((self.blocks_float_to_short_0_0_0, 0), (self.blocks_interleave_0, 1))    
        self.connect((self.blocks_interleave_0, 0), (self.nutaq_rtdex_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_complex_to_float_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.nutaq_custom_register_0_1.set_value(int((2e6)/self.samp_rate*(2**32)))
        self.nutaq_custom_register_0_1_0.set_value(int(0/self.samp_rate*(2**32)))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/40)

    def get_freq1(self):
        return self.freq1

    def set_freq1(self, freq1):
        self.freq1 = freq1
        self._freq1_slider.set_value(self.freq1)
        self._freq1_text_box.set_value(self.freq1)
        self.analog_sig_source_x_0.set_frequency(self.freq1)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = perseus_mimo()
    tb.Start(True)
    tb.Wait()
