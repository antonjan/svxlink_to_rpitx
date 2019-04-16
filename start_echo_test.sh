#!/bin/sh

echo test
nc -l 8011 | sudo /home/pi/rpitx/rpitx -i- -m IQFLOAT -f 438775 &
python /home/pi/rpitx_interface.py &
exit
