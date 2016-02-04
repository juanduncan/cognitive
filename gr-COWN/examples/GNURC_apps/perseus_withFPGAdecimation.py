#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Perseus Spectrum Sensing
# Generated: Fri Jun 26 12:42:37 2015
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
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import DataConversion
import nutaq
import spectsensing
import sys

from distutils.version import StrictVersion
class perseus_withFPGAdecimation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Perseus Spectrum Sensing")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Perseus Spectrum Sensing")
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

        self.settings = Qt.QSettings("GNU Radio", "perseus_withFPGAdecimation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 20e6
        self.packet_size = packet_size = 8192
        self.oversampling = oversampling = 4
        self.nfft = nfft = 2**15
        self.decimation = decimation = 40
        self.amplitude = amplitude = 0.125
        self.RF_freq = RF_freq = 943e6
        self.PSD_averaging = PSD_averaging = 600

        ##################################################
        # Blocks
        ##################################################
        self.spectsensing_xs_plot_1 = spectsensing.xs_plot("")
        self._spectsensing_xs_plot_1_win = self.spectsensing_xs_plot_1;
        self.top_layout.addWidget(self._spectsensing_xs_plot_1_win)
        self.spectsensing_ss_pds_plot_0 = spectsensing.ss_pds_plot(nfft, samp_rate, 1024 )
        self.nutaq_rtdex_source_S_S_0 = nutaq.rtdex_source("nutaq_carrier_perseus_TX",gr.sizeof_short,1,0)
        self.nutaq_rtdex_source_S_S_0.set_type(0)
        self.nutaq_rtdex_source_S_S_0.set_packet_size(1300)
        self.nutaq_rtdex_source_S_S_0.set_channels("0")
        self.nutaq_rtdex_source_0_0_0 = nutaq.rtdex_source("nutaq_carrier_perseus_TX",gr.sizeof_short,1,7)
        self.nutaq_rtdex_source_0_0_0.set_type(0)
        self.nutaq_rtdex_source_0_0_0.set_packet_size(packet_size)
        self.nutaq_rtdex_source_0_0_0.set_channels("2")
        (self.nutaq_rtdex_source_0_0_0).set_min_output_buffer(16384)
        self.nutaq_rtdex_sink_0 = nutaq.rtdex_sink("nutaq_carrier_perseus_TX",gr.sizeof_short,1,7)
        self.nutaq_rtdex_sink_0.set_type(0)
        self.nutaq_rtdex_sink_0.set_packet_size(packet_size)
        self.nutaq_rtdex_sink_0.set_channels("1")
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_TX", 2, 1)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(RF_freq)
        self.nutaq_radio420_tx_0_0.set_default_reference(1)
        self.nutaq_radio420_tx_0_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_tx_0_0.set_default_calibrate(1)
        self.nutaq_radio420_tx_0_0.set_default_band(0)
        self.nutaq_radio420_tx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-10)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(15)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain3(3)
        self.nutaq_radio420_tx_0_0.set_default_tx_lpf_bandwidth(2)
        self.nutaq_radio420_tx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_tx_0 = nutaq.radio420_tx("nutaq_carrier_perseus_TX", 1, 0)
        self.nutaq_radio420_tx_0.set_default_enable(1)
        self.nutaq_radio420_tx_0.set_default_tx_freq(RF_freq)
        self.nutaq_radio420_tx_0.set_default_reference(0)
        self.nutaq_radio420_tx_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_tx_0.set_default_calibrate(1)
        self.nutaq_radio420_tx_0.set_default_band(0)
        self.nutaq_radio420_tx_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0.set_default_tx_vga1_gain(-4)
        self.nutaq_radio420_tx_0.set_default_tx_vga2_gain(15)
        self.nutaq_radio420_tx_0.set_default_tx_gain3(14)
        self.nutaq_radio420_tx_0.set_default_tx_lpf_bandwidth(2)
        self.nutaq_radio420_tx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0_0 = nutaq.radio420_rx("nutaq_carrier_perseus_TX", 2, 3)
        self.nutaq_radio420_rx_0_0.set_default_enable(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_freq(RF_freq)
        self.nutaq_radio420_rx_0_0.set_default_reference(1)
        self.nutaq_radio420_rx_0_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_0_0.set_default_calibrate(1)
        self.nutaq_radio420_rx_0_0.set_default_band(0)
        self.nutaq_radio420_rx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_vga1_gain(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain3(-8)
        self.nutaq_radio420_rx_0_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_lpf_bandwidth(2)
        self.nutaq_radio420_rx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0 = nutaq.radio420_rx("nutaq_carrier_perseus_TX", 1, 2)
        self.nutaq_radio420_rx_0.set_default_enable(1)
        self.nutaq_radio420_rx_0.set_default_rx_freq(RF_freq)
        self.nutaq_radio420_rx_0.set_default_reference(0)
        self.nutaq_radio420_rx_0.set_default_datarate(samp_rate*2)
        self.nutaq_radio420_rx_0.set_default_calibrate(1)
        self.nutaq_radio420_rx_0.set_default_band(0)
        self.nutaq_radio420_rx_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0.set_default_rx_lna_gain(2)
        self.nutaq_radio420_rx_0.set_default_rx_vga1_gain(2)
        self.nutaq_radio420_rx_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain3(-8)
        self.nutaq_radio420_rx_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0.set_default_rx_lpf_bandwidth(2)
        self.nutaq_radio420_rx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_custom_register_0_1_1 = nutaq.custom_register("nutaq_carrier_perseus_TX",9)
        self.nutaq_custom_register_0_1_1.set_index(6)
        self.nutaq_custom_register_0_1_1.set_default_value(PSD_averaging)
        self.nutaq_custom_register_0_1_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_1_0 = nutaq.custom_register("nutaq_carrier_perseus_TX",7)
        self.nutaq_custom_register_0_1_0.set_index(2)
        self.nutaq_custom_register_0_1_0.set_update_rate(1)
          
        self.nutaq_custom_register_0_1 = nutaq.custom_register("nutaq_carrier_perseus_TX",36)
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
        self.nutaq_custom_register_0.set_default_value(3)
        self.nutaq_custom_register_0.set_update_rate(1)
          
        self.nutaq_carrier_perseus_TX = nutaq.carrier(0,"nutaq_carrier_perseus_TX", "192.168.0.101")
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=oversampling,
        	bt=0.71,
        	verbose=False,
        	log=False,
        )
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=oversampling,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, "192.168.0.100", 1234, 1472, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, 2*4e3 + 0*samp_rate/40/(oversampling*8*2),True)
        self.blocks_short_to_float_0_1_0 = blocks.short_to_float(1, 2**11)
        self.blocks_short_to_float_0_0_0_0 = blocks.short_to_float(1, 2**11)
        self.blocks_multiply_const_vxx_0_3 = blocks.multiply_const_vff((2.0**(16*2), ))
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vcc((amplitude, ))
        self.blocks_multiply_const_vxx_0_1_1 = blocks.multiply_const_vff((2.0**(16*0), ))
        self.blocks_multiply_const_vxx_0_1_0_0 = blocks.multiply_const_vff((2.0**(16*1), ))
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        self.blocks_float_to_short_0_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 2**11-1)
        self.blocks_float_to_complex_0_0_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/juan/Music/de_mi.mp3", True)
        self.blocks_deinterleave_0_0_1 = blocks.deinterleave(gr.sizeof_short*1, 1)
        self.blocks_deinterleave_0_0_0 = blocks.deinterleave(gr.sizeof_short*1, 1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=8,
        		preamble="",
        		access_code="",
        		pad_for_usrp=True,
        	),
        	payload_length=128,
        )
        self.blks2_packet_decoder_1 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code="",
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_1.recv_pkt(ok, payload),
        	),
        )
        self.DataConversion_reint_short_float_0_3 = DataConversion.reint_short_float()
        self.DataConversion_reint_short_float_0_2_0 = DataConversion.reint_short_float()
        self.DataConversion_reint_short_float_0_1_0 = DataConversion.reint_short_float()
        self.DataConversion_reint_short_float_0_0_0 = DataConversion.reint_short_float()
        self.DataConversion_eaver_resynchronizer_0_0 = DataConversion.eaver_resynchronizer(1024)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.spectsensing_ss_pds_plot_0, 'psd_pdu'), (self.spectsensing_xs_plot_1, 'pdus'))    
        self.connect((self.DataConversion_eaver_resynchronizer_0_0, 0), (self.spectsensing_ss_pds_plot_0, 0))    
        self.connect((self.DataConversion_eaver_resynchronizer_0_0, 1), (self.spectsensing_ss_pds_plot_0, 1))    
        self.connect((self.DataConversion_reint_short_float_0_0_0, 0), (self.blocks_multiply_const_vxx_0_3, 0))    
        self.connect((self.DataConversion_reint_short_float_0_1_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0, 0))    
        self.connect((self.DataConversion_reint_short_float_0_2_0, 0), (self.blocks_multiply_const_vxx_0_1_1, 0))    
        self.connect((self.DataConversion_reint_short_float_0_3, 0), (self.DataConversion_eaver_resynchronizer_0_0, 0))    
        self.connect((self.blks2_packet_decoder_1, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gmsk_mod_0, 0))    
        self.connect((self.blocks_add_xx_0_0, 0), (self.DataConversion_eaver_resynchronizer_0_0, 1))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0_0, 0))    
        self.connect((self.blocks_deinterleave_0_0_0, 1), (self.blocks_short_to_float_0_0_0_0, 0))    
        self.connect((self.blocks_deinterleave_0_0_0, 0), (self.blocks_short_to_float_0_1_0, 0))    
        self.connect((self.blocks_deinterleave_0_0_1, 1), (self.DataConversion_reint_short_float_0_0_0, 0))    
        self.connect((self.blocks_deinterleave_0_0_1, 3), (self.DataConversion_reint_short_float_0_1_0, 0))    
        self.connect((self.blocks_deinterleave_0_0_1, 2), (self.DataConversion_reint_short_float_0_2_0, 0))    
        self.connect((self.blocks_deinterleave_0_0_1, 0), (self.DataConversion_reint_short_float_0_3, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.digital_gmsk_demod_0, 0))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 0))    
        self.connect((self.blocks_float_to_short_0_0_0, 0), (self.blocks_interleave_0, 1))    
        self.connect((self.blocks_interleave_0, 0), (self.nutaq_rtdex_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0, 0), (self.blocks_add_xx_0_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_1_1, 0), (self.blocks_add_xx_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_3, 0), (self.blocks_add_xx_0_0, 0))    
        self.connect((self.blocks_short_to_float_0_0_0_0, 0), (self.blocks_float_to_complex_0_0_0, 1))    
        self.connect((self.blocks_short_to_float_0_1_0, 0), (self.blocks_float_to_complex_0_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blks2_packet_encoder_0, 0))    
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_1, 0))    
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_multiply_const_vxx_0_2, 0))    
        self.connect((self.nutaq_rtdex_source_0_0_0, 0), (self.blocks_deinterleave_0_0_0, 0))    
        self.connect((self.nutaq_rtdex_source_S_S_0, 0), (self.blocks_deinterleave_0_0_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "perseus_withFPGAdecimation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(2*4e3 + 0*self.samp_rate/40/(self.oversampling*8*2))
        self.nutaq_custom_register_0_1_0.set_value(int(0/self.samp_rate*(2**32)))
        self.nutaq_custom_register_0_1.set_value(int((0)/self.samp_rate*(2**32)))

    def get_packet_size(self):
        return self.packet_size

    def set_packet_size(self, packet_size):
        self.packet_size = packet_size

    def get_oversampling(self):
        return self.oversampling

    def set_oversampling(self, oversampling):
        self.oversampling = oversampling
        self.blocks_throttle_0.set_sample_rate(2*4e3 + 0*self.samp_rate/40/(self.oversampling*8*2))

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.blocks_multiply_const_vxx_0_2.set_k((self.amplitude, ))

    def get_RF_freq(self):
        return self.RF_freq

    def set_RF_freq(self, RF_freq):
        self.RF_freq = RF_freq
        self.nutaq_radio420_rx_0.set_rx_gain(-8)
        self.nutaq_radio420_rx_0.set_rx_freq(self.RF_freq)
          
        self.nutaq_radio420_rx_0_0.set_rx_gain(-8)
        self.nutaq_radio420_rx_0_0.set_rx_freq(self.RF_freq)
          
        self.nutaq_radio420_tx_0_0.set_tx_gain(3)
        self.nutaq_radio420_tx_0_0.set_tx_freq(self.RF_freq)
          
        self.nutaq_radio420_tx_0.set_tx_gain(14)
        self.nutaq_radio420_tx_0.set_tx_freq(self.RF_freq)
          

    def get_PSD_averaging(self):
        return self.PSD_averaging

    def set_PSD_averaging(self, PSD_averaging):
        self.PSD_averaging = PSD_averaging
        self.nutaq_custom_register_0_1_1.set_value(self.PSD_averaging)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = perseus_withFPGAdecimation()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
