# svxlink_to_rpitx
This repository will have the code to use rtl_sdr dongle vir reception and rpitx as transmitter.
I got insperation from the code devloped here http://www.pg540.org/wiki/index.php/RPITX_interface_to_SVXlink_using_GNUradio
# Description
This project will run on a raspberry Pi and use rpitx Transmitter board from Giga Technology for TX and rtl_sdr dongle for reseption.<br>
Gnuradio will be used to interface between svxlink and rpitx and from rtl_sdr and svxlink<br>
Functional Description : The receiver side is all handled by allready existing functionality in SVXLink using Ddr receiver. All configuration is well documented in svxlink.conf. The transmitter part interface is made out of 3 components. The audio coming from SVXlink TX1 is routed via UDP port 1235 to GNUradio, the PTT is routed to PseudoTTY port /home/pi/ptt and the TCP output port 8011 of GNUradio IQ stream is routed to RPITX. When SVXlink wants to transmit it sends a charackter T to the PseudoTTY device ( PTT ON ), a perl script which is started after the start of SVXlink will monitor this PseudoTTY and once it will see the character T it will execute other script starting first RPITX snd then Python GNUradio script. This will switch on the transmitter and audio is routed to RPITX. When SVXlink need to stop transmitting then the character R is send by SVXlink to the PseudoTTY and received by the script monitoring the PTY. It will kill RPITX and Python GNUradio script. As it takes a bit of time to start RPITX ( initializing the PLL ) and starting the TCP listener and starting Python some extra delay is given to SVXLink in the configuration. 
# Dependinsies
1) rpitx<br>
2) rtl_sdr<br>
3) svxlink<br>
4) gnuradio<br>
# Usage
copy all repository files in the root pi directory.<br>
copy the svxlink.conf to the /etc/svxlink/ directory<br>
run the following scripts in the pi directory.<br>
sudo ./start_tx.sh<br>
sudo ./start_tx.sh<br>
Set the rx frequency in the svxlink.conf file.<br>
Set the tx frequency in the start_echo_test.sh script<br>
Set the Vox level in the svxlink.conf<br>
set the echolink audio level in the svxlink.conf<br>

# Gnuradio Block diagram
![gnuradio block diagram](images/Rpitx_grc.JPG?raw=true "Block diagram")<br>
# Hardware
1) Raspberry Pi hat from Giga Technology http://www.giga.co.za<br>
2) Raspberry Pi<br>
3) rtl SDR dongle<br>
![Hardware diagram](images/svxlink_to_rpitx.png?raw=true "Block diagram")<br>
# Project Status
Working SVX link system.

# SVX Configuration

SVXlink configuration changes are :<br>
The svxlink.conf in this repository has already have this config
In [RX1] of svxlink.conf configure TYPE=Ddr, SIGLEV_DET=DDR, SIGLEV_DET=2.61, SIGLEV_OFFSET=150, FQ=433540000, WBRX=WbRX1<br>
<br>
In [WbRX1] put TYPE=RtlUSB, DEV_MATCH=0, HOST=localhost, PORT=1234, CENTER_FQ=433540000, GAIN=3.7,PEAK_METER=1, SAMPLE_RATE=960000<br>

In [TX1] put TYPE=LOCAL, AUDIO_DEV=udp:127.0.0.1:1235, AUDO_CHANNEL=0, PTT_TYPE=PTY, PTT_PTY=/home/pi/ptt.pl<br> 
