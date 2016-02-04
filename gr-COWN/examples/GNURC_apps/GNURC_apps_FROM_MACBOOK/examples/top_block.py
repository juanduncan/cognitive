#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sat Nov 29 21:09:53 2014
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import vocoder
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_slider_2 = variable_slider_2 = 0
        self.variable_slider_0 = variable_slider_0 = 50000
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        _variable_slider_2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_2_sizer,
        	value=self.variable_slider_2,
        	callback=self.set_variable_slider_2,
        	label="label_variable_slider_0 NOise amplitude",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_2_sizer,
        	value=self.variable_slider_2,
        	callback=self.set_variable_slider_2,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_2_sizer)
        _variable_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	label="label_variable_slider_MULITIPLICACION_VOZ",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	minimum=0,
        	maximum=1e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_sizer)
        self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
        	self.GetWin(),
        	title="Constellation Plot",
        	sample_rate=samp_rate,
        	frame_rate=256,
        	const_size=4,
        	M=2,
        	theta=0,
        	loop_bw=6.28/100.0,
        	fmax=0.06,
        	mu=0.5,
        	gain_mu=0.005,
        	symbol_rate=samp_rate/4.,
        	omega_limit=0.005,
        )
        self.Add(self.wxgui_constellationsink2_0.win)
        self.vocoder_g723_40_encode_sb_0 = vocoder.g723_40_encode_sb()
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=4,
          mod_code="gray",
          differential=True,
          samples_per_symbol=256,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((variable_slider_0, ))
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.audio_source_0 = audio.source(samp_rate, "", True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, variable_slider_2, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_constellationsink2_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.vocoder_g723_40_encode_sb_0, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.vocoder_g723_40_encode_sb_0, 0), (self.digital_qam_mod_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.blocks_add_xx_0, 0))


# QT sink close method reimplementation

    def get_variable_slider_2(self):
        return self.variable_slider_2

    def set_variable_slider_2(self, variable_slider_2):
        self.variable_slider_2 = variable_slider_2
        self._variable_slider_2_slider.set_value(self.variable_slider_2)
        self._variable_slider_2_text_box.set_value(self.variable_slider_2)
        self.analog_noise_source_x_0.set_amplitude(self.variable_slider_2)

    def get_variable_slider_0(self):
        return self.variable_slider_0

    def set_variable_slider_0(self, variable_slider_0):
        self.variable_slider_0 = variable_slider_0
        self._variable_slider_0_slider.set_value(self.variable_slider_0)
        self._variable_slider_0_text_box.set_value(self.variable_slider_0)
        self.blocks_multiply_const_vxx_0.set_k((self.variable_slider_0, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate)

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
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    tb = top_block()
    tb.Start(True)
    tb.Wait()

