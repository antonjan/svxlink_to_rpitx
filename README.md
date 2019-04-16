# svxlink_to_rpitx
This repository will have the code to use rtl_sdr dongle vir reception and rpitx as transmitter.
I got insperation from the code devloped here http://www.pg540.org/wiki/index.php/RPITX_interface_to_SVXlink_using_GNUradio
# Description
This project will run on a raspberry Pi and use rpitx Transmitter board from Giga Technology for TX and rtl_sdr dongle for reseption.<br>
Gnuradio will be used to interface between svxlink and rpitx and from rtl_sdr and svxlink
#Dependinsies
1) rpitx<br>
2) rtl_sdr
3) svxlink

# Project Status
Just started project not compleet yet.

# SVX Configuration

SVXlink configuration changes are :<br>

In [RX1] of svxlink.conf configure TYPE=Ddr, SIGLEV_DET=DDR, SIGLEV_DET=2.61, SIGLEV_OFFSET=150, FQ=433540000, WBRX=WbRX1<br>

In [WbRX1] put TYPE=RtlUSB, DEV_MATCH=0, HOST=localhost, PORT=1234, CENTER_FQ=433540000, GAIN=3.7,PEAK_METER=1, SAMPLE_RATE=960000<br>

In [TX1] put TYPE=LOCAL, AUDIO_DEV=udp:127.0.0.1:1235, AUDO_CHANNEL=0, PTT_TYPE=PTY, PTT_PTY=/home/pi/ptt<br> 
