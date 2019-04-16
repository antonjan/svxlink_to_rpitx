#!/usr/bin/perl
#
# @file    nhrcx.pl
# @brief   Perl-script to link a NHRCx controller to SvxLink over
#          Linux pseudo tty's
# @author  Adi Bier / DL1HRC
# @date    2014-05-01
#
# Run this script after starting SvxLink. Do not configure the
# links in the /dev directory.
#
# SvxLink - A Multi Purpose Voice Services System for Ham Radio Use
# Copyright (C) 2004-2014  Tobias Blomberg / SM0SVX
# Adjusted PE2JKO to control RPITX

use Time::HiRes qw(usleep);
#use Device::SerialPort;
use IO::File;

$ptt_port   = "/home/pi/ptt";
$logfile    = "/tmp/nhrc-x.log";
$DEBUG      = 1;


$PTT = openPtty("$ptt_port"); #  ptt port from SvxLink

while (1) {

  $PTT->read($p, 1);
  if ($p gt ' ') {
    $message = $p;
    if ($p ne 'T') {
      system("/home/pi/rpitx/stop_tx.sh");
      &writelog("UIT");
    }

    if ($p ne 'R') {
      system("/home/pi/rpitx/start_tx.sh");
      &writelog("AAN");
    }

    &writelog("PTT-command: $p");
    undef $p;
  }

  usleep(10000);
}
close($PTT);
exit;

sub openPtty {
  my $fh = IO::File->new($_[0], O_NONBLOCK|O_RDWR);
  if (!(defined $fh)) {
    &writelog("Can not open $_[0]");
    print "Can not open $_[0]\n";
    return 0;
  }
  $fh->autoflush(1);
  &writelog("opening $_[0] OK");
  return $fh;
}

sub writelog {
  if ($DEBUG) {
    open(LOG,">>$logfile");
      print LOG $_[0],"\n";
    close(LOG);
  }
}
