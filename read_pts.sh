#!/bin/bash
#read X < /dev/pts/0 
#$ echo $X

while IFS= read -r -n1 char
do
if [ $char == "T" ]
  then
#    `rigctl -m 370 -r /dev/ttyUSB0 -s 19200 T 1`
echo " ptt is tx"
python /home/pi/start_gnuradio_ptt.py 
fi
if [ $char == "R" ]
  then
#    `rigctl -m 370 -r /dev/ttyUSB0 -s 19200 T 0`
echo " ptt is rx"
python /home/pi/stop_gnuradio_ptt.py 
fi

done < "${1:-/home/pi/ptt}"

