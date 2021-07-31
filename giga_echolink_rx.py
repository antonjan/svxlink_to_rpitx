#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Giga Echolink RX
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import osmosdr
import time

from gnuradio import qtgui

class giga_echolink_rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Giga Echolink RX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Giga Echolink RX")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "giga_echolink_rx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_range_4 = variable_qtgui_range_4 = 1e-4
        self.variable_qtgui_range_3 = variable_qtgui_range_3 = 144.312000e6
        self.variable_qtgui_range_2 = variable_qtgui_range_2 = -32
        self.variable_qtgui_range_1 = variable_qtgui_range_1 = 5000
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 1.2
        self.samp_rate_old = samp_rate_old = 1764000
        self.samp_rate = samp_rate = 1.2e6

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_4_range = Range(0.5e-4, 1e-3, 0.1, 1e-4, 200)
        self._variable_qtgui_range_4_win = RangeWidget(self._variable_qtgui_range_4_range, self.set_variable_qtgui_range_4, 'SQ delay', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_4_win)
        self._variable_qtgui_range_3_range = Range(144e6, 146e6, 0.1, 144.312000e6, 200)
        self._variable_qtgui_range_3_win = RangeWidget(self._variable_qtgui_range_3_range, self.set_variable_qtgui_range_3, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_3_win)
        self._variable_qtgui_range_2_range = Range(-100, 10, 0.1, -32, 200)
        self._variable_qtgui_range_2_win = RangeWidget(self._variable_qtgui_range_2_range, self.set_variable_qtgui_range_2, 'Squelch', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_2_win)
        self._variable_qtgui_range_1_range = Range(0, 30000, 0.1, 5000, 200)
        self._variable_qtgui_range_1_win = RangeWidget(self._variable_qtgui_range_1_range, self.set_variable_qtgui_range_1, 'FM diviasion', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_1_win)
        self._variable_qtgui_range_0_range = Range(0, 10, 0.1, 1.2, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, 'Audio Level', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=48000,
                decimation=1200000,
                taps=None,
                fractional_bw=None)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            441000, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ''
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(variable_qtgui_range_3, 0)
        self.osmosdr_source_0.set_freq_corr(46, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(True, 0)
        self.osmosdr_source_0.set_gain(60, 0)
        self.osmosdr_source_0.set_if_gain(60, 0)
        self.osmosdr_source_0.set_bb_gain(60, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                48000,
                15000,
                2000,
                firdes.WIN_HAMMING,
                6.76))
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(32, True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(variable_qtgui_range_0)
        self.audio_sink_0 = audio.sink(48000, 'hw:2,0,2', True)
        self.analog_pwr_squelch_xx_1 = analog.pwr_squelch_cc(variable_qtgui_range_2, variable_qtgui_range_4, 0, True)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=48000,
        	tau=75e-6,
        	max_dev=variable_qtgui_range_1,
          )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.analog_pwr_squelch_xx_1, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_pwr_squelch_xx_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "giga_echolink_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_range_4(self):
        return self.variable_qtgui_range_4

    def set_variable_qtgui_range_4(self, variable_qtgui_range_4):
        self.variable_qtgui_range_4 = variable_qtgui_range_4
        self.analog_pwr_squelch_xx_1.set_alpha(self.variable_qtgui_range_4)

    def get_variable_qtgui_range_3(self):
        return self.variable_qtgui_range_3

    def set_variable_qtgui_range_3(self, variable_qtgui_range_3):
        self.variable_qtgui_range_3 = variable_qtgui_range_3
        self.osmosdr_source_0.set_center_freq(self.variable_qtgui_range_3, 0)

    def get_variable_qtgui_range_2(self):
        return self.variable_qtgui_range_2

    def set_variable_qtgui_range_2(self, variable_qtgui_range_2):
        self.variable_qtgui_range_2 = variable_qtgui_range_2
        self.analog_pwr_squelch_xx_1.set_threshold(self.variable_qtgui_range_2)

    def get_variable_qtgui_range_1(self):
        return self.variable_qtgui_range_1

    def set_variable_qtgui_range_1(self, variable_qtgui_range_1):
        self.variable_qtgui_range_1 = variable_qtgui_range_1
        self.analog_nbfm_rx_0.set_max_deviation(self.variable_qtgui_range_1)

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.blocks_multiply_const_vxx_0.set_k(self.variable_qtgui_range_0)

    def get_samp_rate_old(self):
        return self.samp_rate_old

    def set_samp_rate_old(self, samp_rate_old):
        self.samp_rate_old = samp_rate_old

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)





def main(top_block_cls=giga_echolink_rx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
