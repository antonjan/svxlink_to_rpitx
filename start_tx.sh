#!/bin/sh

echo "start"
/home/pi/reflector/src/build/bin/svxlink &
sleep 1
/home/pi/ptt.pl &
exit
