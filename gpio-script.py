#!/usr/bin/env python

from gpiozero import Button
from signal import pause
import subprocess

# Add GPIO, script pairs here
scripts = {
  'GPIO26': 'toggle mute.sh',
}

def call_script(button):
  print scripts[str(button.pin)] + " called"
  subprocess.call(['sh', scripts[str(button.pin)]])

for gpio, script in scripts.items():
  print (gpio, ">", script)
  b = Button(gpio)
  b.when_pressed = call_script

pause()
