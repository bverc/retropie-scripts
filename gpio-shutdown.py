#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import subprocess

pin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(pin, GPIO.FALLING)
print "press detected, checking for longpress"
sleep(2)

if GPIO.input(pin) == 0:
  print "press still held, shutting down"
  subprocess.call(['sh', 'safe shutdown.sh'])
else:
  print "shutdown aborted"

