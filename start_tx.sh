#!/bin/sh

echo "start"
/usr/bin/svxlink &
sleep 1
/home/pi/ptt.pl &
exit
