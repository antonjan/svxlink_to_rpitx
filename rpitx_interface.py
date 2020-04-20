#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SVxlink .... X Interface
# Author: zs6cmo
# Description: Interface for SVXlink
# Generated: Mon Apr 20 11:41:48 2020
##################################################


from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser


class rpitx_interface(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "SVxlink .... X Interface")

        ##################################################
        # Variables
        ##################################################
        self.tx_audo_level = tx_audo_level = 400

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=2,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	2, 48, 6, 250, firdes.WIN_HAMMING, 6.76))
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_short*1, '127.0.0.1', 1235, 4096, True)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 32767)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((400, ))
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_short*1, 1)
        self.blks2_tcp_sink_0 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr='127.0.0.1',
        	port=8011,
        	server=False,
        )
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=48,
        	quad_rate=96,
        	tau=75,
        	max_dev=10,
        	fh=-1.0,
                )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blks2_tcp_sink_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_deinterleave_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))

    def get_tx_audo_level(self):
        return self.tx_audo_level

    def set_tx_audo_level(self, tx_audo_level):
        self.tx_audo_level = tx_audo_level


def main(top_block_cls=rpitx_interface, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
