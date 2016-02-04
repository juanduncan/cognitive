#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Transceiver Juan
# Generated: Wed Oct 14 17:04:57 2015
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

from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
from wifi_phy_hier import wifi_phy_hier  # grc-generated hier_block
import foo
import ieee802_11
import wx


class wifi_transceiver_juan(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Wifi Transceiver Juan")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 15
        self.samp_rate_0 = samp_rate_0 = 20e6
        self.samp_rate = samp_rate = 10e6
        self.rx_gain = rx_gain = 5
        self.oversampling = oversampling = 4
        self.mult = mult = 0.38
        self.lo_offset = lo_offset = 0
        self.freq = freq = 5.89e9
        self.encoding = encoding = 0

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.samp_rate,
        	callback=self.set_samp_rate,
        	label="Sample Rate",
        	choices=[5e6,10e6, 20e6],
        	labels=["5MHz", "10 MHz", "20 MHz"],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._samp_rate_chooser)
        _mult_sizer = wx.BoxSizer(wx.VERTICAL)
        self._mult_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_mult_sizer,
        	value=self.mult,
        	callback=self.set_mult,
        	label='mult',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._mult_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_mult_sizer,
        	value=self.mult,
        	callback=self.set_mult,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_mult_sizer)
        self._encoding_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.encoding,
        	callback=self.set_encoding,
        	label="Encoding",
        	choices=[0,1,2,3,4,5,6,7],
        	labels=["BPSK 1/2", "BPSK 3/4", "QPSK 1/2", "QPSK 3/4", "16QAM 1/2", "16QAM 3/4", "64QAM 2/3", "64QAM 3/4"],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._encoding_chooser)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=5000,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wifi_phy_hier_0 = wifi_phy_hier(
            chan_est=0,
            encoding=0,
        )
        _tx_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tx_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tx_gain_sizer,
        	value=self.tx_gain,
        	callback=self.set_tx_gain,
        	label='tx_gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tx_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tx_gain_sizer,
        	value=self.tx_gain,
        	callback=self.set_tx_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tx_gain_sizer)
        _rx_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rx_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rx_gain_sizer,
        	value=self.rx_gain,
        	callback=self.set_rx_gain,
        	label='rx_gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rx_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rx_gain_sizer,
        	value=self.rx_gain,
        	callback=self.set_rx_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rx_gain_sizer)
        self._lo_offset_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.lo_offset,
        	callback=self.set_lo_offset,
        	label="LO Offset",
        	choices=[0, 6e6, 11e6],
        	labels=['0 MHz', '6 MHz', '11 MHz'],
        )
        self.Add(self._lo_offset_chooser)
        self.ieee802_11_ofdm_mac_0 = ieee802_11.ofdm_mac(([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]), ([0x30, 0x14, 0x4a, 0xe6, 0x46, 0xe4]), ([0x42, 0x42, 0x42, 0x42, 0x42, 0x42]))
        self.ieee802_11_ether_encap_0 = ieee802_11.ether_encap(True)
        self._freq_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label="Channel",
        	choices=[2412000000.0, 2417000000.0, 2422000000.0, 2427000000.0, 2432000000.0, 2437000000.0, 2442000000.0, 2447000000.0, 2452000000.0, 2457000000.0, 2462000000.0, 2467000000.0, 2472000000.0, 2484000000.0, 5170000000.0, 5180000000.0, 5190000000.0, 5200000000.0, 5210000000.0, 5220000000.0, 5230000000.0, 5240000000.0, 5260000000.0, 5280000000.0, 5300000000.0, 5320000000.0, 5500000000.0, 5520000000.0, 5540000000.0, 5560000000.0, 5580000000.0, 5600000000.0, 5620000000.0, 5640000000.0, 5660000000.0, 5680000000.0, 5700000000.0, 5745000000.0, 5765000000.0, 5785000000.0, 5805000000.0, 5825000000.0, 5860000000.0, 5870000000.0, 5880000000.0, 5890000000.0, 5900000000.0, 5910000000.0, 5920000000.0],
        	labels=['  1 | 2412.0 | 11g', '  2 | 2417.0 | 11g', '  3 | 2422.0 | 11g', '  4 | 2427.0 | 11g', '  5 | 2432.0 | 11g', '  6 | 2437.0 | 11g', '  7 | 2442.0 | 11g', '  8 | 2447.0 | 11g', '  9 | 2452.0 | 11g', ' 10 | 2457.0 | 11g', ' 11 | 2462.0 | 11g', ' 12 | 2467.0 | 11g', ' 13 | 2472.0 | 11g', ' 14 | 2484.0 | 11g', ' 34 | 5170.0 | 11a', ' 36 | 5180.0 | 11a', ' 38 | 5190.0 | 11a', ' 40 | 5200.0 | 11a', ' 42 | 5210.0 | 11a', ' 44 | 5220.0 | 11a', ' 46 | 5230.0 | 11a', ' 48 | 5240.0 | 11a', ' 52 | 5260.0 | 11a', ' 56 | 5280.0 | 11a', ' 58 | 5300.0 | 11a', ' 60 | 5320.0 | 11a', '100 | 5500.0 | 11a', '104 | 5520.0 | 11a', '108 | 5540.0 | 11a', '112 | 5560.0 | 11a', '116 | 5580.0 | 11a', '120 | 5600.0 | 11a', '124 | 5620.0 | 11a', '128 | 5640.0 | 11a', '132 | 5660.0 | 11a', '136 | 5680.0 | 11a', '140 | 5700.0 | 11a', '149 | 5745.0 | 11a', '153 | 5765.0 | 11a', '157 | 5785.0 | 11a', '161 | 5805.0 | 11a', '165 | 5825.0 | 11a', '172 | 5860.0 | 11p', '174 | 5870.0 | 11p', '176 | 5880.0 | 11p', '178 | 5890.0 | 11p', '180 | 5900.0 | 11p', '182 | 5910.0 | 11p', '184 | 5920.0 | 11p'],
        )
        self.Add(self._freq_chooser)
        self.foo_packet_pad2_0 = foo.packet_pad2(False, False, 0.001, 10000, 10000)
        (self.foo_packet_pad2_0).set_min_output_buffer(100000)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=.5**.5,
        	frequency_offset=0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, "192.168.200.2", 1234, 100, True)
        self.blocks_tuntap_pdu_0 = blocks.tuntap_pdu("tap0", 440, False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, 2*4e3 + 0*samp_rate/40/(oversampling*8*2),True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((mult, ))
        (self.blocks_multiply_const_vxx_0).set_min_output_buffer(100000)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/media/juan/d6aba572-c85c-40cc-9258-ae1538dfb8c5/home/juan/Music/de_mi.mp3", True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tuntap_pdu_0, 'pdus'), (self.ieee802_11_ether_encap_0, 'from tap'))    
        self.msg_connect((self.ieee802_11_ether_encap_0, 'to tap'), (self.blocks_tuntap_pdu_0, 'pdus'))    
        self.msg_connect((self.ieee802_11_ether_encap_0, 'to wifi'), (self.ieee802_11_ofdm_mac_0, 'app in'))    
        self.msg_connect((self.ieee802_11_ofdm_mac_0, 'phy out'), (self.blocks_message_debug_0, 'print'))    
        self.msg_connect((self.ieee802_11_ofdm_mac_0, 'phy out'), (self.wifi_phy_hier_0, 'mac_in'))    
        self.msg_connect((self.wifi_phy_hier_0, 'mac_out'), (self.ieee802_11_ether_encap_0, 'from wifi'))    
        self.msg_connect((self.wifi_phy_hier_0, 'mac_out'), (self.ieee802_11_ofdm_mac_0, 'phy in'))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.foo_packet_pad2_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.wifi_phy_hier_0, 0))    
        self.connect((self.foo_packet_pad2_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.wifi_phy_hier_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.wifi_phy_hier_0, 1), (self.wxgui_scopesink2_0, 0))    


    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self._tx_gain_slider.set_value(self.tx_gain)
        self._tx_gain_text_box.set_value(self.tx_gain)

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self._samp_rate_chooser.set_value(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(2*4e3 + 0*self.samp_rate/40/(self.oversampling*8*2))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self._rx_gain_slider.set_value(self.rx_gain)
        self._rx_gain_text_box.set_value(self.rx_gain)

    def get_oversampling(self):
        return self.oversampling

    def set_oversampling(self, oversampling):
        self.oversampling = oversampling
        self.blocks_throttle_0.set_sample_rate(2*4e3 + 0*self.samp_rate/40/(self.oversampling*8*2))

    def get_mult(self):
        return self.mult

    def set_mult(self, mult):
        self.mult = mult
        self._mult_slider.set_value(self.mult)
        self._mult_text_box.set_value(self.mult)
        self.blocks_multiply_const_vxx_0.set_k((self.mult, ))

    def get_lo_offset(self):
        return self.lo_offset

    def set_lo_offset(self, lo_offset):
        self.lo_offset = lo_offset
        self._lo_offset_chooser.set_value(self.lo_offset)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_chooser.set_value(self.freq)

    def get_encoding(self):
        return self.encoding

    def set_encoding(self, encoding):
        self.encoding = encoding
        self._encoding_chooser.set_value(self.encoding)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = wifi_transceiver_juan()
    tb.Start(True)
    tb.Wait()
