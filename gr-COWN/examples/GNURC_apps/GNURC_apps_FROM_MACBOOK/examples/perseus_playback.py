#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Perseus Playback
# Generated: Sun Jan 25 13:13:01 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import nutaq
import wx

class perseus_playback(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Perseus Playback")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.update_rate = update_rate = 100
        self.data_rate = data_rate = 10.24e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=data_rate,
        	fft_size=1024,
        	fft_rate=25,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.nutaq_rtdex_source_0 = nutaq.rtdex_source("nutaq_carrier_perseus_0",gr.sizeof_short,1,3)
        self.nutaq_rtdex_source_0.set_type(0)
        self.nutaq_rtdex_source_0.set_packet_size(8192)
        self.nutaq_rtdex_source_0.set_channels("4")
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 1, 0)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(943e6)
        self.nutaq_radio420_tx_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0.set_default_datarate(data_rate*2)
        self.nutaq_radio420_tx_0_0.set_default_calibrate(1)
        self.nutaq_radio420_tx_0_0.set_default_band(0)
        self.nutaq_radio420_tx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-10)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(15)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain3(3)
        self.nutaq_radio420_tx_0_0.set_default_tx_lpf_bandwidth(11)
        self.nutaq_radio420_tx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 1, 1)
        self.nutaq_radio420_rx_0_0.set_default_enable(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_freq(943e6)
        self.nutaq_radio420_rx_0_0.set_default_reference(0)
        self.nutaq_radio420_rx_0_0.set_default_datarate(data_rate*2)
        self.nutaq_radio420_rx_0_0.set_default_calibrate(1)
        self.nutaq_radio420_rx_0_0.set_default_band(0)
        self.nutaq_radio420_rx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_vga1_gain(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain2(16)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain3(5)
        self.nutaq_radio420_rx_0_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_lpf_bandwidth(11)
        self.nutaq_radio420_rx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_playback_0 = nutaq.playback("nutaq_carrier_perseus_0",2)
        self.nutaq_playback_0.set_filename("/opt/Nutaq/ADP6/ADP_MicroTCA/sdk/gnuradio/gr-nutaq/examples/playback_sinewave.bin")
        self.nutaq_playback_0.set_continuous_mode(1)
        self.nutaq_playback_0.set_type(0)
        self.nutaq_playback_0.set_packet_size(1024)
          
        self.nutaq_custom_register_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",5)
        self.nutaq_custom_register_0_0.set_index(4)
        self.nutaq_custom_register_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0 = nutaq.custom_register("nutaq_carrier_perseus_0",4)
        self.nutaq_custom_register_0.set_index(1)
        self.nutaq_custom_register_0.set_default_value(5)
        self.nutaq_custom_register_0.set_update_rate(1)
          
        self.nutaq_carrier_perseus_0 = nutaq.carrier(0,"nutaq_carrier_perseus_0", "192.168.0.102")
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 2047)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 2047)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_short*1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_short_to_float_0_0, 0))
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.nutaq_rtdex_source_0, 0), (self.blocks_deinterleave_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.wxgui_fftsink2_0, 0))


# QT sink close method reimplementation

    def get_update_rate(self):
        return self.update_rate

    def set_update_rate(self, update_rate):
        self.update_rate = update_rate

    def get_data_rate(self):
        return self.data_rate

    def set_data_rate(self, data_rate):
        self.data_rate = data_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.data_rate)

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
    tb = perseus_playback()
    tb.Start(True)
    tb.Wait()

