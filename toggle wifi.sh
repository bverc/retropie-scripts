#!/bin/bash

wifi=$(rfkill -r -n -o soft list wifi)

if [ $wifi = "blocked" ] ; then
  rfkill unblock wifi
  echo "wifi unblock"
else
  rfkill block wifi
  echo "wifi block"
fi
